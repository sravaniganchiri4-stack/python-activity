
# Student Timetable Conflict Detection

# Timetable format: (day, start_time, end_time, room, course)

timetable = [
    ("Monday", 9, 11, "R101", "Python"),
    ("Monday", 10, 12, "R102", "Mathematics"),
    ("Tuesday", 9, 10, "R101", "English")
]

unavailable_rooms = ["R103", "R104"]

conflict = False

print("----- TIMETABLE VALIDATION -----")

for i in range(len(timetable)):
    day1, start1, end1, room1, course1 = timetable[i]

    if room1 in unavailable_rooms:
        print(course1, ": Room", room1, "is unavailable")
        conflict = True

    for j in range(i + 1, len(timetable)):
        day2, start2, end2, room2, course2 = timetable[j]

        if day1 == day2:
            # Check overlapping periods
            if start1 < end2 and start2 < end1:
                if room1 == room2:
                    print("Room conflict:", course1, "and", course2)
                    conflict = True
                else:
                    print("Schedule overlap:", course1, "and", course2)
                    conflict = True

if not conflict:
    print("Timetable is valid. No conflicts found.")
else:
    print("Proposed timetable is INVALID.")

