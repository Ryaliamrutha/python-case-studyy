# Case Study 27: Advanced Numeric Pattern Generator

## Problem Statement
Generate a symmetric numeric diamond pattern using nested loops based on a user-specified positive size.

## Objectives
1. Use nested loops for pattern generation.
2. Apply spacing to align a symmetric pattern.
3. Validate the size entered by the user.

## Assumptions
- The size must be a positive integer.
- The pattern contains ascending numbers from 1 to the row number and then descending numbers.

## Algorithm
1. Start.
2. Read the size of the pattern.
3. If the size is not positive, display an error.
4. Use an outer loop for the upper half of the diamond.
5. Print leading spaces and ascending and descending numbers in each row.
6. Use another outer loop for the lower half.
7. Stop.

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
INPUT n
IF n <= 0: DISPLAY Invalid size
ELSE
  FOR row = 1 TO n
    PRINT leading spaces
    PRINT numbers 1 TO row
    PRINT numbers row-1 DOWN TO 1
  END FOR
  FOR row = n-1 DOWN TO 1
    PRINT leading spaces
    PRINT numbers 1 TO row
    PRINT numbers row-1 DOWN TO 1
  END FOR
END IF
STOP
```

## Python Source Code
```python
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
```

## Test Cases
- Test 1: Size=3 →   1 / 121 / 12321 / 121 / 1
- Test 2: Size=1 → 1
- Test 3: Size=0 → Invalid size

## Sample Output
```text
Enter diamond size: 3
  1
 121
12321
 121
  1
```

## Conclusion
The program demonstrates nested loops and conditional validation to generate a symmetric numeric diamond.
