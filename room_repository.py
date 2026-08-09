from room_model import room
from storage_manager import load_data, save_data

DATA_FILE = "rooms.json"

def load_rooms_as_objects():
    raw_dicts = load_data(DATA_FILE)
    room_objects = []

    for d in raw_dicts:
        # Convert dictionary keys into Room class parameters
        room_obj = room(d["id"], d.get("name", d.get("room")), int(d["capacity"]))
        room_objects.append(room_obj)

    return room_objects

def save_room_object(new_room_obj):
    # Load existing objects
    rooms = load_rooms_as_objects()
    rooms.append(new_room_obj)

    # Convert all Room objects back into dictionaries for JSON
    dict_list = [room.to_dict() for room in rooms]

    save_data(DATA_FILE, dict_list)
    print(f"[SUCCESS] Room '{new_room_obj.name}' persisted to disk via Object Model!")

    # Test 1: Load rooms as live objects
loaded_rooms = load_rooms_as_objects()
print(f"Loaded {len(loaded_rooms)} Room objects from disk.\n")

# Test 2: Use class methods on loaded objects
print("=== Capacity Check (Testing 50 people) ===")
for r in loaded_rooms:
    fits = r.is_suitable_for(50)
    print(f"- {r.name} (Capacity {r.capacity}): Suitable? {fits}")

# Test 3: Create and save a new Room instance
new_seminar_room = room("R501", "Executive Seminar Hall", 80)
save_room_object(new_seminar_room)