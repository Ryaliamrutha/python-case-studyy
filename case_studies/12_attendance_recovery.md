# Case Study 12: Attendance Recovery Computation

## Problem Statement
Calculate a student's current attendance percentage and determine the minimum number of consecutive classes the student must attend to reach a required eligibility percentage.

## Objectives
1. Calculate attendance percentage from attended and conducted classes.
2. Check whether the student already meets the eligibility threshold.
3. Use a loop to find the minimum future classes that must be attended.

## Assumptions
- Attended classes and conducted classes are non-negative integers.
- Conducted classes must be greater than zero.
- The student attends every future class without absence.
- The eligibility threshold is entered as a percentage between 0 and 100.

## Algorithm
1. Start.
2. Read attended classes, conducted classes and required percentage.
3. Validate the inputs.
4. Calculate current attendance percentage.
5. If current attendance meets the requirement, display that no additional classes are needed.
6. Otherwise, repeatedly add one attended class and one conducted class until the percentage reaches the requirement.
7. Display the minimum classes required and stop.

## Flowchart
```text
START
  |
INPUT AND VALIDATE DATA
  |
PROCESS USING LOOPS / CONDITIONS
  |
DISPLAY RESULTS
  |
STOP
```

## Pseudocode
```text
START
INPUT attended, conducted, required
IF conducted <= 0 OR attended < 0 OR attended > conducted: DISPLAY Invalid input
ELSE
  percentage = attended * 100 / conducted
  IF percentage >= required: needed = 0
  ELSE
    needed = 0
    WHILE (attended + needed) * 100 / (conducted + needed) < required
      needed = needed + 1
    END WHILE
  END IF
  DISPLAY percentage, needed
END IF
STOP
```

## Python Source Code
```python
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
```

## Test Cases
- Test 1: Attended=60, Conducted=75, Required=75 → 80.0%; 0 classes needed
- Test 2: Attended=50, Conducted=80, Required=75 → 62.5%; 40 classes needed
- Test 3: Attended=0, Conducted=0, Required=75 → Invalid input

## Sample Output
```text
Enter classes attended: 50
Enter total classes conducted: 80
Enter required attendance percentage: 75
Current attendance: 62.5 %
Minimum consecutive classes to attend: 40
```

## Conclusion
The program calculates current attendance and uses iteration to determine the minimum number of future classes that must be attended to reach the required percentage.
