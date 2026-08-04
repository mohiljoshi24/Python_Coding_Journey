def is_room_available (requested_room, booked_room):

    for room in booked_room:

        if requested_room == booked_room:
          return "Occupied"

    return "available"


result1 = is_room_available("room 101", "room 101")
print(f"{result1}")

result2 = is_room_available("room 102", "room 101")
print(f"{result2}")