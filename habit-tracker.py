import json
import os
from datetime import date
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from collections import defaultdict
import calendar

FILE = "habits.json"

def load_habits():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_habits(habits):
    with open(FILE, "w") as f:
        json.dump(habits, f, indent=2)

def mark_habit(habits):
    today = str(date.today())
    year, month, day = today.split('-')
    week = f"Week {((int(day)-1) // 7) + 1}"

    print("\nYour Habits:")
    for idx, habit in enumerate(habits.keys(), 1):
        print(f"{idx}. {habit}")
    
    choice = int(input("\nWhich habit did you complete today? (number): "))
    habit = list(habits.keys())[choice - 1]
    
    if year not in habits[habit]:
        habits[habit][year] = defaultdict(lambda: defaultdict(list))
    
    if month not in habits[habit][year]:
        habits[habit][year][month] = defaultdict(list)

    habits[habit][year][month][week].append(today)
    print(f"✅ Marked '{habit}' for {today}!")

def view_progress(habits):
    # Generate PDF with progress details
    generate_pdf(habits)

    # Print progress in the console
    for habit, years in habits.items():
        for year, months in years.items():
            for month, weeks in months.items():
                for week, dates in weeks.items():
                    print(f"\n📌 {habit} — {year}-{month}-{week} — {len(set(dates))} days tracked")

def generate_pdf(habits):
    today = str(date.today())
    pdf_filename = f"habit_progress_{today}.pdf"
    
    # Create a canvas object to build the PDF
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.setFont("Helvetica", 12)
    
    # Title and metadata
    c.drawString(100, 750, f"Habit Tracking Progress - {today}")
    c.drawString(100, 730, f"Here is your progress on the habits:")
    
    y_position = 710  # starting position for habit details

    # Loop through habits, years, months, and weeks
    for habit, years in habits.items():
        for year, months in years.items():
            for month, weeks in months.items():
                c.drawString(100, y_position, f"{habit} - {year}-{month}:")
                y_position -= 20
                for week, dates in weeks.items():
                    c.drawString(120, y_position, f"  {week}: {len(set(dates))} days")
                    y_position -= 20

                y_position -= 10  # extra space between months
    # Save the PDF
    c.save()
    print(f"📄 PDF generated: {pdf_filename}")

def main():
    habits = load_habits()
    
    while True:
        print("\n1️⃣ Add Habit\n2️⃣ Mark as Done\n3️⃣ View Progress\n4️⃣ Export to PDF\n5️⃣ Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            new_habit = input("Enter new habit: ")
            habits[new_habit] = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
            print(f"🎯 Added new habit: {new_habit}")

        elif choice == "2":
            mark_habit(habits)

        elif choice == "3":
            view_progress(habits)

        elif choice == "4":
            generate_pdf(habits)

        elif choice == "5":
            break

        else:
            print("⚠️ Invalid option")

        save_habits(habits)

if __name__ == "__main__":
    main()
