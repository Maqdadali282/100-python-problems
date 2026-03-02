import matplotlib.pyplot as plt
import datetime as dt

# -----------------------------
# WBS DATA (your project data)
# -----------------------------
tasks = [
    ("Scope Document", "2026-01-10", "2026-01-25"),
    ("SRC Document", "2026-01-25", "2026-02-05"),
    ("SDS Document", "2026-02-05", "2026-02-10"),
    ("Module 1: Problem Modeling & Configuration", "2026-02-10", "2026-03-06"),
    ("Module 2: Classical AI Solver Engine", "2026-03-06", "2026-03-30"),
    ("Module 3: Quantum Simulation Engine", "2026-03-30", "2026-04-25"),
    ("Module 4: Hybrid Execution Controller", "2026-04-25", "2026-05-15"),
    ("Module 5: Comparative Analytics Dashboard", "2026-09-05", "2026-09-25"),
    ("Module 6: Educational Walkthrough & Documentation", "2026-09-25", "2026-10-20"),
    ("Final Documentation & Submission Prep", "2026-10-20", "2026-10-30"),
    ("Final Presentation & Project Closure", "2026-10-30", "2026-11-10"),
]

# Convert string dates to datetime
task_names = []
start_dates = []
durations = []

for task, start, end in tasks:
    start_dt = dt.datetime.strptime(start, "%Y-%m-%d")
    end_dt = dt.datetime.strptime(end, "%Y-%m-%d")

    task_names.append(task)
    start_dates.append(start_dt)
    durations.append((end_dt - start_dt).days)

# Reverse tasks so first task appears at top
task_names.reverse()
start_dates.reverse()
durations.reverse()

# -----------------------------
# PLOT GANTT CHART
# -----------------------------
fig, ax = plt.subplots(figsize=(13, 6))

ax.barh(
    task_names,
    durations,
    left=start_dates,
    height=0.5,
)

# -----------------------------
# FORMATTING (to match image)
# -----------------------------
ax.set_title("Figure 1: Gantt Chart of FYP Project", fontsize=12, fontweight="bold")
ax.set_xlabel("Timeline")
ax.set_ylabel("Project Tasks")

# Show dates on TOP (important)
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')

# Date formatting
ax.xaxis_date()
fig.autofmt_xdate()

# Light vertical grid lines (like image)
ax.grid(axis="x", linestyle="--", alpha=0.4)

# Border around chart
for spine in ax.spines.values():
    spine.set_visible(True)

plt.tight_layout()
plt.show()
