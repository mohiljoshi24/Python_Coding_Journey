# Day 7 - Python Built-in Modules & Environment Inspection
# Demonstrates using sys, os, math, and datetime for backend system operations.

import sys
import os
import math
from datetime import datetime

# ---------------------------------------------------------
# 1. SYSTEM & ENVIRONMENT INSPECTION
# ---------------------------------------------------------
print("=== SYSTEM & ENVIRONMENT INFO ===")
print(f"Python Version: {sys.version.split()[0]}")
print(f"Operating System: {os.name.upper()}")
print(f"Current Working Directory: {os.getcwd()}")


# ---------------------------------------------------------
# 2. SCHEDULING MATH CALCULATIONS
# ---------------------------------------------------------
print("\n=== CAPACITY & ROOM ALLOCATION MATH ===")
total_students = 125
room_capacity = 30

# Calculate required rooms (rounding up)
rooms_needed = math.ceil(total_students / room_capacity)
print(f"Total Students: {total_students}")
print(f"Room Capacity: {room_capacity}")
print(f"Rooms Required (Ceiling Rounding): {rooms_needed}")


# ---------------------------------------------------------
# 3. TIMESTAMP GENERATOR FOR TIMETABLE LOGS
# ---------------------------------------------------------
print("\n=== SYSTEM AUDIT LOG TIMESTAMPS ===")
current_time = datetime.now()
formatted_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

print(f"Audit Log Timestamp: [{formatted_timestamp}]")
print(f"Log Message: System environment successfully initialized.")