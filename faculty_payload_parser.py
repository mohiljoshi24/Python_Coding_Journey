faculty_data = {
    "id": "f101",
    "prof_name": "mohil joshi",
    "max_workload": 5,
    "assigned_class": [
        {"subject": "dsa", "duration": 2},
        {"subject": "alorithms lab", "duration": 2},
        {"subject": "dbms", "duration": 1.5}
     ]
}

prof_name = faculty_data["prof_name"]
max_limit = faculty_data["max_workload"]
total_hour = 0

for classes in faculty_data["assigned_class"]:
   subject_name = classes["subject"]
   class_duration = classes["duration"]
   total_hour = total_hour + class_duration

   print(f" {subject_name}: {class_duration} hrs ")

print(f"\n  total assigned hour: {total_hour} hrs")

if total_hour > max_limit:
   overage = total_hour - max_limit
   print(f"alert workload limit is breached by {overage} hours!")

else:
   remaining = max_limit - total_hour
   print(f"success worload approved! remaining qouta: {remaining} hrs")