# Student Marks Matrix Analysis
# Python Activity-Based Learning

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
