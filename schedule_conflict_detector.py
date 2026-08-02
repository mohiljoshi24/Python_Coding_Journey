def has_schedule_conflict(schedule_list, target_slot, target_room):
  
    for booking in schedule_list:
       
        if booking["slot"] == target_slot and booking["room"] == target_room:
            
            return True
            
    return False


current_schedule = [
    {"slot": "09:00 - 10:00", "room": "Lab 201", "subject": "DBMS Lab"},
    {"slot": "10:00 - 11:00", "room": "Room 101", "subject": "Data Structures"},
    {"slot": "11:00 - 12:00", "room": "Lab 202", "subject": "Python Lab"}
]

print("=== CHECKING SCHEDULE CONFLICTS ===")

req_slot_1 = "09:00 - 10:00"
req_room_1 = "Lab 201"

conflict_1 = has_schedule_conflict(current_schedule, req_slot_1, req_room_1)

if conflict_1:
    print(f"[ALERT] Conflict detected! {req_room_1} is already booked at {req_slot_1}.")
else:
    print(f"[SUCCESS] Slot approved! {req_room_1} is free at {req_slot_1}.")


req_slot_2 = "11:00 - 12:00"
req_room_2 = "Lab 201"

conflict_2 = has_schedule_conflict(current_schedule, req_slot_2, req_room_2)

if conflict_2:
    print(f"[ALERT] Conflict detected! {req_room_2} is already booked at {req_slot_2}.")
else:
    print(f"[SUCCESS] Slot approved! {req_room_2} is free at {req_slot_2}.")