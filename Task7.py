
# Advanced Numeric Pattern Generator

n = int(input("Enter diamond size (odd number): "))

if n <= 0 or n % 2 == 0:
    print("Invalid dimension! Enter a positive odd number.")
else:
    mid = n // 2

    for i in range(n):
        row = i if i <= mid else n - 1 - i
        spaces = mid - row

        print(" " * spaces, end="")

        for j in range(2 * row + 1):
            if j == 0 or j == 2 * row:
                print(row + 1, end="")
            else:
                print(" ", end="")

        print()
