
# Nested Loop Examination Seating Generator

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
capacity = int(input("Enter classroom capacity: "))

reserved = [(1, 2), (2, 3)]  # Reserved positions
students = int(input("Enter number of students: "))

if rows <= 0 or cols <= 0 or capacity <= 0 or students < 0:
    print("Invalid input")
else:
    seats = []
    count = 0

    print("\n----- SEATING ARRANGEMENT -----")

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):

            # Skip reserved positions
            if (r, c) in reserved:
                print(" [RESERVED]", end="")
                continue

            # Alternate seating: use odd-numbered columns only
            if c % 2 == 0:
                print(" [EMPTY]   ", end="")
                continue

            if count < students and count < capacity:
                seat = "S" + str(count + 1)
                seats.append((seat, r, c))
                print(" " + seat, end="")
                count += 1
            else:
                print(" [EMPTY]   ", end="")

        print()

    print("\nStudents seated:", count)
    print("Classroom capacity:", capacity)

    if students > capacity:
        print("Warning: Students exceed classroom capacity!")
    elif count < students:
        print("Warning: Not enough eligible seats!")
    else:
        print("Seating arrangement generated successfully.")
