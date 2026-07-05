#!/usr/bin/env python3
"""Bootstrap Light skills into common agent-client discovery directories.

Canonical source stays in ``skills/``. This helper creates project-local
mirrors for clients that discover Agent Skills from:

- ``.agents/skills``  : Codex / OpenCode open-standard path
- ``.claude/skills``  : Claude Code project skills, also read by OpenCode
- ``.opencode/skills``: OpenCode native project skills

The default ``--mode auto`` tries directory symlinks first and falls back to
copying when the OS refuses symlinks (common on Windows without Developer Mode).
Copied mirrors are marked with ``.light_generated_link`` so ``--force`` can
refresh generated copies without touching user-owned directories.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

TARGETS = {
    "agents": Path(".agents") / "skills",
    "claude": Path(".claude") / "skills",
    "opencode": Path(".opencode") / "skills",
}
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")
GENERATED_MARKER = ".light_generated_link"


@dataclass
class SkillMeta:
    directory: str
    name: str
    description_len: int
    ok: bool
    issues: list[str]


@dataclass
class TargetResult:
    target: str
    skill: str
    status: str
    path: str
    mode: str | None = None
    message: str | None = None


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_frontmatter(skill_md: Path) -> tuple[dict[str, str], str]:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    fm = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    lines = fm.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" not in line or line.startswith((" ", "\t")):
            i += 1
            continue
        key, raw = line.split(":", 1)
        key = key.strip()
        value = raw.strip()
        if value in {">", ">-", "|", "|-"}:
            block: list[str] = []
            i += 1
            while i < len(lines) and (not lines[i] or lines[i].startswith((" ", "\t"))):
                block.append(lines[i].strip())
                i += 1
            data[key] = " ".join(part for part in block if part)
            continue
        data[key] = value.strip("\"'")
        i += 1
    return data, body


def iter_skills(skills_dir: Path) -> Iterable[Path]:
    if not skills_dir.exists():
        return []
    return sorted(p for p in skills_dir.iterdir() if p.is_dir() and (p / "SKILL.md").exists())


def validate_skill(skill_dir: Path) -> SkillMeta:
    fm, _ = parse_frontmatter(skill_dir / "SKILL.md")
    issues: list[str] = []
    name = fm.get("name", "")
    description = fm.get("description", "")
    if not name:
        issues.append("missing frontmatter name")
    elif not NAME_RE.fullmatch(name):
        issues.append("name must be lowercase kebab-case, <=64 chars")
    if name and name != skill_dir.name:
        issues.append(f"directory name '{skill_dir.name}' != frontmatter name '{name}'")
    if "claude" in name or "anthropic" in name:
        issues.append("name contains reserved Claude/Anthropic token")
    if not description:
        issues.append("missing frontmatter description")
    elif len(description) > 1024:
        issues.append(f"description too long for Claude/OpenCode metadata ({len(description)} > 1024)")
    return SkillMeta(
        directory=skill_dir.name,
        name=name,
        description_len=len(description),
        ok=not issues,
        issues=issues,
    )


def _safe_remove_generated(path: Path) -> bool:
    """Remove only symlinks or Light-generated copy mirrors."""
    if path.is_symlink():
        path.unlink()
        return True
    if path.is_dir() and (path / GENERATED_MARKER).exists():
        shutil.rmtree(path)
        return True
    if path.is_file() and path.name == GENERATED_MARKER:
        path.unlink()
        return True
    return False


def _copy_skill(src: Path, dest: Path, source_root: Path) -> None:
    shutil.copytree(src, dest)
    marker = {
        "generated_by": "Light-Skills/scripts/bootstrap_agent_skills.py",
        "source": str(src.resolve()),
        "canonical_root": str(source_root.resolve()),
        "note": "Generated mirror. Re-run bootstrap with --force after editing canonical skills/.",
    }
    (dest / GENERATED_MARKER).write_text(json.dumps(marker, ensure_ascii=False, indent=2), encoding="utf-8")


def _link_skill(src: Path, dest: Path) -> None:
    os.symlink(src.resolve(), dest, target_is_directory=True)


def bootstrap_one(
    src: Path,
    target_root: Path,
    target_name: str,
    mode: str,
    force: bool,
    source_root: Path,
) -> TargetResult:
    dest = target_root / src.name
    if dest.exists() or dest.is_symlink():
        if not force:
            return TargetResult(target_name, src.name, "exists", str(dest), message="use --force to refresh generated mirror")
        if not _safe_remove_generated(dest):
            return TargetResult(target_name, src.name, "skipped", str(dest), message="existing path is not Light-generated; left untouched")

    target_root.mkdir(parents=True, exist_ok=True)
    if mode in {"auto", "symlink"}:
        try:
            _link_skill(src, dest)
            return TargetResult(target_name, src.name, "created", str(dest), mode="symlink")
        except OSError as exc:
            if mode == "symlink":
                return TargetResult(target_name, src.name, "failed", str(dest), mode="symlink", message=str(exc))

    try:
        _copy_skill(src, dest, source_root)
        return TargetResult(target_name, src.name, "created", str(dest), mode="copy")
    except OSError as exc:
        return TargetResult(target_name, src.name, "failed", str(dest), mode="copy", message=str(exc))


def run(repo_root: Path, targets: list[str], mode: str, force: bool, check_only: bool) -> tuple[list[SkillMeta], list[TargetResult]]:
    skills_dir = repo_root / "skills"
    skills = list(iter_skills(skills_dir))
    metas = [validate_skill(p) for p in skills]
    results: list[TargetResult] = []
    if check_only:
        for target in targets:
            root = repo_root / TARGETS[target]
            for skill in skills:
                dest = root / skill.name
                status = "present" if dest.exists() or dest.is_symlink() else "missing"
                results.append(TargetResult(target, skill.name, status, str(dest)))
        return metas, results

    for target in targets:
        root = repo_root / TARGETS[target]
        for skill, meta in zip(skills, metas):
            if not meta.ok:
                results.append(TargetResult(target, skill.name, "invalid", str(root / skill.name), message="; ".join(meta.issues)))
                continue
            results.append(bootstrap_one(skill, root, target, mode, force, skills_dir))
    return metas, results


def run_selftest(repo_root: Path) -> int:
    base = repo_root / ".upgrade" / "_e2e" / "bootstrap_agent_skills_selftest"
    resolved = base.resolve()
    guard = (repo_root / ".upgrade" / "_e2e").resolve()
    if guard not in resolved.parents and resolved != guard:
        raise RuntimeError(f"unsafe selftest path: {resolved}")
    if base.exists():
        shutil.rmtree(base)
    (base / "skills" / "light-demo").mkdir(parents=True)
    (base / "skills" / "light-second").mkdir(parents=True)
    for name in ["light-demo", "light-second"]:
        (base / "skills" / name / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Test skill for bootstrap.\n---\n\n# {name}\n",
            encoding="utf-8",
        )
    metas, results = run(base, ["agents", "claude", "opencode"], "copy", False, False)
    assert all(m.ok for m in metas), metas
    assert len(results) == 6, results
    for target in TARGETS:
        for name in ["light-demo", "light-second"]:
            p = base / TARGETS[target] / name / "SKILL.md"
            marker = base / TARGETS[target] / name / GENERATED_MARKER
            assert p.exists(), p
            assert marker.exists(), marker
    _, check = run(base, ["agents", "claude", "opencode"], "copy", False, True)
    assert all(r.status == "present" for r in check), check
    print("[selftest] bootstrap_agent_skills ALL PASS")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Mirror Light skills into Codex/Claude/OpenCode discovery paths.")
    parser.add_argument("--repo-root", default=str(repo_root_from_script()), help="repository root; defaults to this script's repo")
    parser.add_argument("--targets", nargs="+", choices=sorted(TARGETS), default=sorted(TARGETS), help="client targets to prepare")
    parser.add_argument("--mode", choices=["auto", "copy", "symlink"], default="auto", help="mirror strategy")
    parser.add_argument("--force", action="store_true", help="refresh generated mirrors; never overwrites user-owned directories")
    parser.add_argument("--check-only", action="store_true", help="report validation and missing mirrors without writing")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--selftest", action="store_true", help="run an isolated selftest under .upgrade/_e2e")
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    if args.selftest:
        return run_selftest(repo_root)

    metas, results = run(repo_root, args.targets, args.mode, args.force, args.check_only)
    payload = {"skills": [asdict(m) for m in metas], "results": [asdict(r) for r in results]}
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        bad = [m for m in metas if not m.ok]
        print(f"[Light bootstrap] skills={len(metas)} invalid={len(bad)} check_only={args.check_only}")
        for m in bad:
            print(f"  [INVALID] {m.directory}: {'; '.join(m.issues)}")
        for r in results:
            mode = f" mode={r.mode}" if r.mode else ""
            msg = f" ({r.message})" if r.message else ""
            print(f"  [{r.status.upper()}] {r.target}/{r.skill}{mode}: {r.path}{msg}")
    return 1 if any(not m.ok for m in metas) or any(r.status in {"failed", "invalid", "missing"} for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
