def validate_room_type(required_type, available_room_type):
    if required_type == available_room_type:
        return {"valid": True, "message": "Room type match successful."}
    
    else:
        return {"valid": False, "message": "Room type mismatch! Required room type not met."}


def validate_faculty_workload(current_hours, new_class_duration, max_limit):
    proposed_hours = current_hours + new_class_duration
    
    if proposed_hours <= max_limit:
        return {
            "valid": True, 
            "total_hours": proposed_hours, 
            "message": "Workload approved."
        }
    
    else:
        return {
            "valid": False, 
            "total_hours": proposed_hours, 
            "message": "Workload limit breached!"
        }


print("=== TESTING ROOM TYPE VALIDATION ===")

room_test_1 = validate_room_type("computer_lab", "computer_lab")
print(f"Test 1 (Match): {room_test_1}")

room_test_2 = validate_room_type("computer_lab", "lecture_hall")
print(f"Test 2 (Mismatch): {room_test_2}")

print("\n=== TESTING FACULTY WORKLOAD VALIDATION ===")
max_allowed_hours = 5.0

workload_test_1 = validate_faculty_workload(4.0, 1.0, max_allowed_hours)
print(f"Test 3 (Approved): {workload_test_1}")

workload_test_2 = validate_faculty_workload(4.0, 2.0, max_allowed_hours)
print(f"Test 4 (Breached): {workload_test_2}")