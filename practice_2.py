def has_conflict(schedule, target_slot, target_room):

    for booking in schedule:

        if booking["slot"] == target_slot and booking["room"] == target_room:
            return True

    return False    

current_schedule = [
    {"slot": "09:00 - 10:00", "room": "room 101"},
    {"slot": "10:00 - 11:00", "room": "lab 201"},
]

result1 = has_conflict(current_schedule, "09:00 - 10:00", "room 101")
print(f"{result1}")

result2 = has_conflict(current_schedule, "11:00 - 12:00", "room 101")
print(f"{result2}")