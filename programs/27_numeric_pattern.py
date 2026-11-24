# Advanced Numeric Pattern Generator
# Python Activity-Based Learning

n = int(input("Enter diamond size: "))

if n <= 0:
    print("Invalid size")
else:
    for row in range(1, n + 1):
        for space in range(n - row):
            print(" ", end="")
        for number in range(1, row + 1):
            print(number, end="")
        for number in range(row - 1, 0, -1):
            print(number, end="")
        print()

    for row in range(n - 1, 0, -1):
        for space in range(n - row):
            print(" ", end="")
        for number in range(1, row + 1):
            print(number, end="")
        for number in range(row - 1, 0, -1):
            print(number, end="")
        print()
