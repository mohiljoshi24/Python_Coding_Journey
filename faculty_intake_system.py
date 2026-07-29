
# Constants
MAX_WORK_HOURS = 5.0

# User Input
professor_name = input("Enter your name (e.g., Dr. Aditi Sharma): ")
professor_department = input("Enter your department (e.g., Computer Science): ")
professor_assigned_course = input("Enter your assigned course (e.g., CS 202 - Data Structures): ")
professor_assigned_hours = float(input("Enter your assigned work hours: "))

# Logic
remaining_hour = MAX_WORK_HOURS - professor_assigned_hours

# Formatted Output Card
print("\n" + "=" * 40)
print("       FACULTY WORKLOAD SUMMARY CARD       ")
print("=" * 40)
print(f"Name            : {professor_name}")
print(f"Department      : {professor_department}")
print(f"Assigned Course : {professor_assigned_course}")
print(f"Assigned Hours  : {professor_assigned_hours:.1f} hrs")
print(f"Remaining Hours : {remaining_hour:.1f} hrs / {MAX_WORK_HOURS:.1f} hrs")
print("=" * 40 + "\n")