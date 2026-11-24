# Case Study 42: Student Marks Matrix Analysis

## Problem Statement
Analyse a matrix of student marks across subjects, calculate each student's average, calculate subject averages, identify the top-performing student and find the subject with the lowest average.

## Objectives
1. Represent marks using a nested list.
2. Calculate row-wise and column-wise averages.
3. Identify the top student and lowest-average subject.

## Assumptions
- At least one student and one subject are entered.
- All marks are between 0 and 100.
- Every student has marks for the same subjects.

## Algorithm
1. Start.
2. Read the number of students and subjects.
3. Read subject names.
4. Read marks into a nested list.
5. Calculate each student's average and identify the highest average.
6. Calculate each subject's average using nested loops.
7. Identify the subject with the lowest average.
8. Display the report.

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
INPUT student_count, subject_count
INPUT subject names
FOR each student
  INPUT marks for every subject
  STORE marks in nested list
END FOR
CALCULATE each student's average
CALCULATE each subject's average
FIND highest student average and lowest subject average
DISPLAY report
STOP
```

## Python Source Code
```python
students = []
subjects = []

student_count = int(input("Enter number of students: "))
subject_count = int(input("Enter number of subjects: "))

for j in range(subject_count):
    subjects.append(input("Enter subject name: "))

for i in range(student_count):
    row = []
    print("Enter marks for student", i + 1)
    for j in range(subject_count):
        mark = float(input("Enter " + subjects[j] + " marks: "))
        row.append(mark)
    students.append(row)

if student_count > 0 and subject_count > 0:
    top_average = -1
    top_student = 0

    for i in range(student_count):
        total = 0
        for j in range(subject_count):
            total = total + students[i][j]
        average = total / subject_count
        print("Student", i + 1, "average:", round(average, 2))
        if average > top_average:
            top_average = average
            top_student = i + 1

    lowest_average = 101
    lowest_subject = ""
    for j in range(subject_count):
        total = 0
        for i in range(student_count):
            total = total + students[i][j]
        average = total / student_count
        print(subjects[j], "average:", round(average, 2))
        if average < lowest_average:
            lowest_average = average
            lowest_subject = subjects[j]

    print("Top student:", top_student)
    print("Lowest-average subject:", lowest_subject)
else:
    print("Invalid matrix size")
```

## Test Cases
- Test 1: 2 students, Maths/Science; rows [80,70], [60,90] → Student averages 75,75; Maths avg 70; Science avg 80; top student 1 (tie policy: first)
- Test 2: 1 student, 1 subject, mark 95 → Average 95; top student 1
- Test 3: 0 students → Invalid matrix size

## Sample Output
```text
Enter number of students: 2
Enter number of subjects: 2
Enter subject name: Maths
Enter subject name: Science
Enter marks for student 1
Enter Maths marks: 80
Enter Science marks: 70
Enter marks for student 2
Enter Maths marks: 60
Enter Science marks: 90
Student 1 average: 75.0
Student 2 average: 75.0
Maths average: 70.0
Science average: 80.0
Top student: 1
Lowest-average subject: Maths
```

## Conclusion
The program demonstrates nested lists and nested loops to calculate row-wise and column-wise statistics from student marks.
