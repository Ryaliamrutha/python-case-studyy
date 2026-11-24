# Case Study 31: String-Based Examination Answer Evaluation

## Problem Statement
Compare a student's answer string with a supplied answer key, count correct, incorrect and unanswered responses, and calculate a score using negative marking.

## Objectives
1. Compare answer strings position by position.
2. Count correct, incorrect and unanswered answers.
3. Calculate the final score using a specified marking scheme.

## Assumptions
- Each answer is a single character A, B, C or D; a blank answer is unanswered.
- Each correct answer carries 1 mark.
- Each incorrect answer carries a penalty of 0.25 marks.
- The answer key and student response have equal lengths.

## Algorithm
1. Start.
2. Read the answer key and student responses.
3. Validate that both strings have equal length.
4. Initialize correct, incorrect and unanswered counters.
5. Compare each response with the key.
6. Update the relevant counter.
7. Calculate score as correct marks minus incorrect penalties.
8. Display the result summary.

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
INPUT answer_key, responses
IF lengths differ: DISPLAY Invalid input
ELSE
  SET correct, incorrect, unanswered = 0
  FOR each position
    IF response is blank: unanswered += 1
    ELSE IF response matches key: correct += 1
    ELSE: incorrect += 1
  END FOR
  score = correct - incorrect * 0.25
  DISPLAY counters and score
END IF
STOP
```

## Python Source Code
```python
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
```

## Test Cases
- Test 1: Key=ABCD; Response=AB-D → 2 correct, 1 incorrect, 1 unanswered; score 1.75
- Test 2: Key=ABC; Response=ABC → 3 correct; score 3
- Test 3: Key=AB; Response=A → Invalid input

## Sample Output
```text
Enter answer key (example: ABCD): ABCD
Enter student answers (use - for blank): AB-D
Correct answers: 2
Incorrect answers: 1
Unanswered questions: 1
Final score: 1.75
```

## Conclusion
The program compares strings using loops and conditions, counts response categories and calculates a score with negative marking.
