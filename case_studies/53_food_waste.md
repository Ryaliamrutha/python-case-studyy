# Case Study 53: Food Waste Monitoring System

## Problem Statement
Compare meals prepared, meals served and leftovers across several days, calculate the wastage percentage and identify days that exceed an acceptable wastage limit.

## Objectives
1. Store daily meal information in lists.
2. Calculate leftover meals and wastage percentages.
3. Identify days exceeding a given wastage threshold.

## Assumptions
- Meals prepared and served are non-negative integers.
- Meals served cannot exceed meals prepared.
- The acceptable wastage percentage is between 0 and 100.
- Wastage is calculated as leftovers divided by meals prepared multiplied by 100.

## Algorithm
1. Start.
2. Read the number of days and acceptable wastage percentage.
3. For each day, read meals prepared and served.
4. Validate that served meals do not exceed prepared meals.
5. Calculate leftovers and wastage percentage.
6. Compare wastage percentage with the acceptable limit.
7. Display daily results and identify days exceeding the limit.

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
INPUT number of days, acceptable percentage
FOR each day
  INPUT prepared, served
  IF prepared < 0 OR served < 0 OR served > prepared: REPORT invalid
  ELSE
    leftovers = prepared - served
    IF prepared > 0: waste_percent = leftovers * 100 / prepared
    ELSE: waste_percent = 0
    DISPLAY leftovers and waste_percent
    IF waste_percent > acceptable: REPORT high wastage
  END IF
END FOR
STOP
```

## Python Source Code
```python
days = int(input("Enter number of days: "))
limit = float(input("Enter acceptable wastage percentage: "))

for day in range(1, days + 1):
    prepared = int(input("Meals prepared on day " + str(day) + ": "))
    served = int(input("Meals served on day " + str(day) + ": "))

    if prepared < 0 or served < 0 or served > prepared:
        print("Invalid meal details")
    else:
        leftovers = prepared - served
        if prepared == 0:
            percentage = 0
        else:
            percentage = leftovers * 100 / prepared

        print("Leftover meals:", leftovers)
        print("Wastage percentage:", round(percentage, 2), "%")

        if percentage > limit:
            print("Alert: Wastage exceeds acceptable limit")
        else:
            print("Wastage is within acceptable limit")
```

## Test Cases
- Test 1: Prepared=100, served=80, limit=15 → 20 leftovers; 20%; alert
- Test 2: Prepared=50, served=45, limit=15 → 5 leftovers; 10%; within limit
- Test 3: Prepared=20, served=25 → Invalid meal details

## Sample Output
```text
Enter number of days: 1
Enter acceptable wastage percentage: 15
Meals prepared on day 1: 100
Meals served on day 1: 80
Leftover meals: 20
Wastage percentage: 20.0 %
Alert: Wastage exceeds acceptable limit
```

## Conclusion
The program uses loops, arithmetic operators and conditional statements to monitor daily food waste and flag days exceeding the acceptable limit.
