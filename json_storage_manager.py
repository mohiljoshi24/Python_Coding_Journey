import json


def load_rooms_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def add_room_to_json(file_path, new_room):
    rooms = load_rooms_from_json(file_path)
    rooms.append(new_room)
    
    with open(file_path, "w") as file:
        json.dump(rooms, file, indent=4)
    print(f"[SUCCESS] Added {new_room['name']} to {file_path}")


json_file = "rooms_data.json"


current_rooms = load_rooms_from_json(json_file)
print("=== CURRENT ROOMS FROM FILE ===")
for r in current_rooms:
    print(f"- {r['name']} ({r['type']})")


new_lab = {
    "id": "L202",
    "name": "AI Lab 202",
    "type": "COMPUTER_LAB",
    "capacity": 35
}

add_room_to_json(json_file, new_lab)