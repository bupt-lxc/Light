# -*- coding: utf-8 -*-
"""_shared 包的命令行入口:`python -m _shared [--selftest]`。

__init__.py 用相对 import,需包上下文,故包级 selftest 通过本入口跑
(而非 `python _shared/__init__.py`,后者无包上下文会断相对 import)。
"""
import sys
from _shared import _selftest

if __name__ == "__main__":
    sys.exit(_selftest())
