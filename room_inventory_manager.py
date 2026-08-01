lab_count = 0

rooms = [
    {"id": "r101", "name": "room 101", "type": "lecture_hall", "capacity": "60"},
    {"id": "r201", "name": "lab  201", "type": "computer_lab", "capacity": "30"},
    {"id": "r102", "name": "room 102", "type": "lecture_hall", "capacity": "60"},
    {"id": "r202", "name": "lab  202", "type": "computer_lab", "capacity": "30"},
]

for singal_room in rooms:

    if singal_room["type"] == "computer_lab":
        print(f"found a lab!, name: {singal_room['name']}")
        lab_count = lab_count + 1

print(f"total labs found: {lab_count}")
