import json

def load_room(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

rooms_lists = load_room("rooms.json")

print("=== LOADED ROOMS FROM JSON ===")

for room in rooms_lists:
    print(f"room name: {room['room']} | capacity: {room['capacity']}")


new_room = {"id": "l203", "room": "cloud lab 203", "capacity": 45}
rooms_lists.append(new_room)

with open("rooms.json", "w") as file:
    json.dump(rooms_lists, file, indent=4)

    print("successfully updated rooms.json!")