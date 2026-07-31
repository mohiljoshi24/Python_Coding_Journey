slot_time = input("enter a slot time: ")
total_room = int(input("enter total number of room: "))

for room_num in range(1, total_room + 1):

    print(f"is room 10{room_num} occupied?,")

    while True:
      room_occupancy = int(input("enter 1 for occupied and 0 for not occupied: "))  

      if room_occupancy == 0 or room_occupancy == 1:
         break

      else:
         print("[error] INVALID!, enter 1 or 0, nothing else")

    if room_occupancy == 1:
       print(f"[busy] room 10{room_num} is occupied. checking next room")
       continue

    if room_occupancy == 0:
       print(f"[success], room 10{room_num} is free!, assigning class for {slot_time}")      
       break

    else:
       print(f"[ALERT] All rooms are occupied! No free room found for {slot_time}.")
       