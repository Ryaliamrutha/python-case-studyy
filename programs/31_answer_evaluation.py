# String-Based Examination Answer Evaluation
# Python Activity-Based Learning

answer_key = input("Enter answer key (example: ABCD): ").upper()
responses = input("Enter student answers (use - for blank): ").upper()

if len(answer_key) != len(responses):
    print("Invalid input: answer strings must have equal length")
else:
    correct = 0
    incorrect = 0
    unanswered = 0

    for i in range(len(answer_key)):
        if responses[i] == "-":
            unanswered = unanswered + 1
        elif responses[i] == answer_key[i]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1

    score = correct - incorrect * 0.25

    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Unanswered questions:", unanswered)
    print("Final score:", score)
