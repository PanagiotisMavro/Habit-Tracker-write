# Habit Tracker

A Python-based habit tracker that allows users to track their daily habits, and view their progress by year, month, and week. The tracker generates PDF reports summarizing your habit progress.

## Features

- **Track Habits by Year, Month, and Week**: Record habits and mark them as done on specific days. View your progress by year, month, or week.
- **PDF Export**: Generate detailed progress reports in PDF format, showing how many days each habit has been completed across weeks and months.
- **Store Progress Locally**: All habit tracking data is saved in a local JSON file (`habits.json`), so your progress is preserved between sessions.
- **Simple Interface**: The program provides a simple text-based menu for managing habits and viewing progress.

## Requirements

To run this script, you need the following:

- Python 3.x
- `reportlab` library for PDF generation

You can install the `reportlab` library using pip:

```bash
pip install reportlab

git clone https://github.com/panagiotismayro/habit-tracker.git
cd habit-tracker

python3 habit_tracker.py
```

# Example
After running the script, you'll be able to choose from the following options:
```bash
1️⃣ Add Habit
2️⃣ Mark as Done
3️⃣ View Progress
4️⃣ Export to PDF
5️⃣ Exit

```





