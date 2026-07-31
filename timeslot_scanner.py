MAX_HOURS = 5
current_wordload = 0

for hour in range(9, 15):
    print(f"time slot: {hour}:00 to {hour + 1}:00")
    print(f"tell if professor is teaching in this timeslot or not")

    while True:
        teaching = int(input("enter 1 for yes, 0 for no:  "))

        if teaching == 0 or teaching == 1:
         break

        else:
         print("[error] invalid! please try again")
      
    if teaching == 1:
        current_wordload = current_wordload + 1

    if current_wordload == MAX_HOURS:
        print("ALERT THE PROFESSOR HAVE REACHED TODAY'S MAX LIMIT AND CANT BE ASSIGNED MORE THEN THIS!!")
        break


print(f"all time slots for today is done and today's assigned hours for professor is going to be: {current_wordload}")
