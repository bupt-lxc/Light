args <- commandArgs(trailingOnly = FALSE)
file_arg <- args[grep("^--file=", args)]
script_path <- if (length(file_arg)) sub("^--file=", "", file_arg[[1]]) else "scripts/r_gallery_panels.R"
root <- normalizePath(file.path(dirname(script_path), ".."), winslash = "/", mustWork = TRUE)
panel_dir <- file.path(root, "figures", "panels")
dir.create(panel_dir, recursive = TRUE, showWarnings = FALSE)

required <- c("ggplot2", "scales")
missing <- required[!vapply(required, requireNamespace, logical(1), quietly = TRUE)]
if (length(missing)) {
  stop("Missing R packages: ", paste(missing, collapse = ", "), ". Install them before rendering the R demo panels.", call. = FALSE)
}

library(ggplot2)
library(scales)

theme_panel <- function() {
  theme_minimal(base_size = 9) +
    theme(
      plot.title = element_text(face = "bold", size = 11.5, color = "#0F172A"),
      axis.title = element_text(size = 8.5, color = "#64748B"),
      axis.text = element_text(size = 8, color = "#475569"),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "#E2E8F0", linewidth = 0.35),
      legend.position = "none",
      plot.margin = margin(8, 8, 8, 8)
    )
}

save_panel <- function(plot, filename) {
  ggsave(file.path(panel_dir, filename), plot, width = 4.5, height = 3.35, dpi = 220, bg = "white")
}

set.seed(2001)

# F: event-study style stage shift
stage <- factor(c("baseline", "search", "critique", "analysis", "writing"), levels = c("baseline", "search", "critique", "analysis", "writing"))
estimate <- c(0.0, 0.18, 0.37, 0.51, 0.44) + rnorm(5, 0, 0.018)
half_width <- c(0.08, 0.10, 0.12, 0.11, 0.13)
df_f <- data.frame(stage, estimate, lo = estimate - half_width, hi = estimate + half_width)
p_f <- ggplot(df_f, aes(stage, estimate)) +
  geom_hline(yintercept = 0, color = "#94A3B8", linewidth = 0.45) +
  geom_col(width = 0.58, fill = "#6D5BA6", alpha = 0.82) +
  geom_errorbar(aes(ymin = lo, ymax = hi), width = 0.16, linewidth = 0.75, color = "#3F3B67") +
  geom_point(size = 2.1, color = "white") +
  labs(title = "F  Stage shift", x = "checkpoint", y = "standardized gain") +
  theme_panel() +
  theme(axis.text.x = element_text(angle = 18, hjust = 1))
save_panel(p_f, "panel_f_quality_trajectory.png")

# G: distribution comparison
df_g <- data.frame(
  protocol = rep(c("baseline", "retrieval", "critique", "full stack"), each = 90),
  score = c(
    rnorm(90, 61, 7),
    rnorm(90, 67, 6),
    rnorm(90, 70, 6.4),
    rnorm(90, 76, 5.8)
  )
)
p_g <- ggplot(df_g, aes(protocol, score, fill = protocol)) +
  geom_violin(trim = FALSE, alpha = 0.62, linewidth = 0.2) +
  geom_boxplot(width = 0.16, outlier.shape = NA, color = "#0F172A", alpha = 0.72) +
  scale_fill_manual(values = c("#CBD5E1", "#67E8F9", "#A78BFA", "#34D399")) +
  labs(title = "G  Distribution shift", x = NULL, y = "score") +
  theme_panel() +
  theme(axis.text.x = element_text(angle = 18, hjust = 1))
save_panel(p_g, "panel_g_distribution_shift.png")

# H: Pareto bubble frontier
n <- 72
time_cost <- runif(n, 18, 88)
quality <- 86 - 0.014 * (time_cost - 56)^2 + rnorm(n, 0, 3.6)
quality <- pmin(pmax(quality, 48), 88)
compute <- runif(n, 0.5, 3.8)
family <- sample(c("fast", "balanced", "robust"), n, replace = TRUE, prob = c(0.32, 0.42, 0.26))
df_h <- data.frame(time_cost, quality, compute, family)
frontier <- df_h[order(df_h$time_cost), ]
keep <- rep(FALSE, nrow(frontier))
best <- -Inf
for (i in seq_len(nrow(frontier))) {
  if (frontier$quality[i] > best) {
    keep[i] <- TRUE
    best <- frontier$quality[i]
  }
}
frontier <- frontier[keep, ]
p_h <- ggplot(df_h, aes(time_cost, quality)) +
  geom_point(aes(size = compute, fill = family), shape = 21, color = "white", stroke = 0.35, alpha = 0.82) +
  geom_step(data = frontier, aes(time_cost, quality), inherit.aes = FALSE, color = "#0F766E", linewidth = 0.9, direction = "vh") +
  scale_fill_manual(values = c(fast = "#8FB7C5", balanced = "#9C8FC3", robust = "#7DAA8D")) +
  scale_size_continuous(range = c(1.8, 6.0)) +
  labs(title = "H  Pareto frontier", x = "time cost", y = "quality") +
  theme_panel()
save_panel(p_h, "panel_h_tradeoff_curve.png")

# I: risk budget stack
stage <- rep(c("idea", "plan", "code", "paper"), each = 4)
risk <- rep(c("novelty", "validity", "reproducibility", "communication"), times = 4)
value <- c(0.34, 0.28, 0.22, 0.16, 0.18, 0.36, 0.31, 0.15, 0.10, 0.24, 0.45, 0.21, 0.12, 0.22, 0.20, 0.46)
df_i <- data.frame(stage, risk, value)
p_i <- ggplot(df_i, aes(stage, value, fill = risk)) +
  geom_col(width = 0.68, color = "white", linewidth = 0.35) +
  scale_y_continuous(labels = percent_format(accuracy = 1), expand = expansion(mult = c(0, 0.04))) +
  scale_fill_manual(values = c("#5E8C9A", "#6D5BA6", "#7DAA8D", "#B08A4F")) +
  labs(title = "I  Risk budget", x = "stage", y = "share") +
  theme_panel()
save_panel(p_i, "panel_i_risk_budget.png")

cat("Wrote R gallery panels to", panel_dir, "\n")
