# Student Performance Trend Analysis
# Python Activity-Based Learning

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
