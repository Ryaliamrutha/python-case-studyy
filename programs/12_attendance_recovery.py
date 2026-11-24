# Attendance Recovery Computation
# Python Activity-Based Learning

attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
required = float(input("Enter required attendance percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted or required < 0 or required > 100:
    print("Invalid input")
else:
    percentage = attended * 100 / conducted
    print("Current attendance:", round(percentage, 2), "%")

    needed = 0
    while (attended + needed) * 100 / (conducted + needed) < required:
        needed = needed + 1

    if needed == 0:
        print("You already meet the eligibility requirement.")
    else:
        print("Minimum consecutive classes to attend:", needed)
