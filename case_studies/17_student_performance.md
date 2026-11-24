# Case Study 17: Student Performance Trend Analysis

## Problem Statement
Compare a student's marks in multiple examinations, calculate improvements or declines, and identify the subject with the lowest average performance.

## Objectives
1. Store subject names and marks using lists.
2. Calculate average marks for each subject.
3. Compare the first and last examination marks to identify trends.

## Assumptions
- The same subjects are evaluated in every examination.
- Marks are between 0 and 100.
- At least two examinations are entered.
- The number of subjects is positive.

## Algorithm
1. Start.
2. Read the number of subjects and examination marks.
3. Store subject names and marks in lists.
4. For each subject, calculate the average across examinations.
5. Compare the first and last marks to identify improvement, decline or no change.
6. Find the subject with the lowest average.
7. Display averages, trends and the weakest subject.

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
INPUT number of subjects and examinations
FOR each subject
  INPUT subject name and marks in every examination
  CALCULATE average
  COMPARE last mark with first mark
  CLASSIFY trend
END FOR
FIND subject with lowest average
DISPLAY averages, trends and lowest-average subject
STOP
```

## Python Source Code
```python
subjects = []
first_marks = []
last_marks = []
averages = []

n = int(input("Enter number of subjects: "))
if n <= 0:
    print("Invalid number of subjects")
else:
    for i in range(n):
        name = input("Enter subject name: ")
        first = float(input("Enter first exam mark: "))
        last = float(input("Enter latest exam mark: "))

        if first < 0 or first > 100 or last < 0 or last > 100:
            print("Invalid marks")
        else:
            subjects.append(name)
            first_marks.append(first)
            last_marks.append(last)
            averages.append((first + last) / 2)

    if len(subjects) > 0:
        print("\nPerformance Report")
        for i in range(len(subjects)):
            print(subjects[i], "Average:", round(averages[i], 2))
            if last_marks[i] > first_marks[i]:
                print("Trend: Improved")
            elif last_marks[i] < first_marks[i]:
                print("Trend: Declined")
            else:
                print("Trend: No change")

        lowest = averages[0]
        index = 0
        for i in range(1, len(averages)):
            if averages[i] < lowest:
                lowest = averages[i]
                index = i
        print("Lowest average subject:", subjects[index])
```

## Test Cases
- Test 1: Maths: 60,80; Science: 70,65 → Maths improved; Science declined; lowest average Science
- Test 2: Maths: 75,75 → No change
- Test 3: Number of subjects=0 → Invalid number of subjects

## Sample Output
```text
Enter number of subjects: 2
Enter subject name: Maths
Enter first exam mark: 60
Enter latest exam mark: 80
Enter subject name: Science
Enter first exam mark: 70
Enter latest exam mark: 65

Performance Report
Maths Average: 70.0
Trend: Improved
Science Average: 67.5
Trend: Declined
Lowest average subject: Science
```

## Conclusion
The program uses lists, loops and conditional statements to summarize marks, show subject-wise trends and identify the subject needing attention.
