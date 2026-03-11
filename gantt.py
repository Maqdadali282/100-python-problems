import matplotlib.pyplot as plt
import datetime as dt

# -----------------------------
# WBS DATA (your project data)
# -----------------------------
tasks = [
    ("Custom Simulation Kernel", "2026-02-02", "2026-02-22"),
    ("SFOD Model Comparison Suite", "2026-02-26", "2026-03-22"),
    ("Educational Quantum Simulator", "2026-03-20", "2026-04-07"),
    ("Real-World Data & Architecture Recommender", "2026-04-04", "2026-04-26"),
    ("Classical to Quantum Logic Transformer", "2026-04-22", "2026-05-20"),
    ("Neural Angle Optimizer", "2026-05-14", "2026-06-02"),
    ("QNN Converter", "2026-06-03", "2026-06-13"),
    ("Interactive Performance Dashboard", "2026-06-15", "2026-06-27"),
    ("Integration Testing", "2026-06-28", "2026-07-12"),
    ("Final Documentation & Submission Prep", "2026-09-29", "2026-10-19"),
    ("Final Presentation & Project Closure", "2026-10-20", "2026-11-08"),
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
