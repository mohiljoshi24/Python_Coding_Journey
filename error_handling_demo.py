import json

def safe_load_json(file_path):
    try:
        with open(file_path,"r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"file {file_path} missing! returning empty list.")
        return[]     

    except json.JSONDecodeError:
        print(f"[error]'{file_path}' contains broken/corrupted json!")
        return[]


# test_demo: 1,
missing_data = safe_load_json("fake_rooms.json")
print(f"missing file result: {missing_data}")

print("-" * 40)

# test_demo: 2,
real_data = safe_load_json("rooms.json")
print(f"real file items count: {len(real_data)}")