MAX_DAILY_HOURS = 5

assigned_hours = float(input("enter todays's assigned hour: "))

if assigned_hours > MAX_DAILY_HOURS: 
 print("invalid answer, since max workload cant be greater than 5 hours")

elif assigned_hours < MAX_DAILY_HOURS:
 print("invalid input, since workload cant be negative")

else:
  remaining_hours = MAX_DAILY_HOURS - assigned_hours

  print(f"success!, total remaining hours left is {remaining_hours}")