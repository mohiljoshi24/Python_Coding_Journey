MAX_WORKLOAD = 5 

professor_name = input("Name of professor: ")

current_hours = float(input("enter hours assigned today: "))

new_class_duration = float(input("Hours for the new lecture attempting to be added: "))

total_projected_hour = current_hours + new_class_duration


if current_hours < 0 or new_class_duration < 0:
    print("[HTTP 400 Bad Request] Invalid input: Hours cannot be negative!")


elif total_projected_hour > MAX_WORKLOAD:
 overage = total_projected_hour - MAX_WORKLOAD
 print(f"[HTTP 422 Unprocessable Entity] Assignment Rejected! {professor_name}'s daily workload would reach {total_projected_hour} hrs (Exceeds 5.0 hr cap by {overage} hrs).")


else: 
   remaining = MAX_WORKLOAD - total_projected_hour
   print(f"[HTTP 200 OK] Class Assigned Successfully! {professor_name}'s new total: {total_projected_hour} hrs. Remaining quota: {remaining} hrs.")