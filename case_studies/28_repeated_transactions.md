# Case Study 28: Repeated Transaction Detection

## Problem Statement
Process a list of transaction identifiers and amounts, detect repeated identifiers and identify transactions whose amounts exceed a specified limit.

## Objectives
1. Store transaction identifiers and amounts in lists.
2. Detect duplicate transaction identifiers.
3. Identify transactions above a user-defined amount limit.

## Assumptions
- Transaction identifiers are entered as strings.
- Transaction amounts must be non-negative.
- The threshold is non-negative.
- A repeated identifier is reported for every occurrence after its first appearance.

## Algorithm
1. Start.
2. Read the number of transactions and the amount threshold.
3. Read each transaction identifier and amount into lists.
4. For each transaction, check whether its identifier appeared earlier.
5. Report duplicate identifiers and amounts above the threshold.
6. Stop.

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
INPUT n, threshold
FOR i = 0 TO n-1
  INPUT identifier, amount
  STORE identifier and amount
END FOR
FOR i = 0 TO n-1
  IF identifier appeared before i: REPORT duplicate
  IF amount > threshold: REPORT high amount
END FOR
STOP
```

## Python Source Code
```python
ids = []
amounts = []

n = int(input("Enter number of transactions: "))
threshold = float(input("Enter amount threshold: "))

for i in range(n):
    transaction_id = input("Enter transaction ID: ")
    amount = float(input("Enter transaction amount: "))
    ids.append(transaction_id)
    amounts.append(amount)

print("\nTransaction Audit")
duplicate_found = False
high_found = False

for i in range(n):
    if ids[i] in ids[:i]:
        print("Duplicate transaction ID:", ids[i])
        duplicate_found = True
    if amounts[i] > threshold:
        print("Amount above threshold:", ids[i], amounts[i])
        high_found = True

if not duplicate_found:
    print("No duplicate transaction IDs")
if not high_found:
    print("No transaction exceeds the threshold")
```

## Test Cases
- Test 1: A1=100, A2=600, A1=200; threshold=500 → A1 duplicate; A2 amount above threshold
- Test 2: B1=50; threshold=100 → No duplicates; no high amount
- Test 3: No transactions → No duplicates; no high amount

## Sample Output
```text
Enter number of transactions: 3
Enter amount threshold: 500
Enter transaction ID: A1
Enter transaction amount: 100
Enter transaction ID: A2
Enter transaction amount: 600
Enter transaction ID: A1
Enter transaction amount: 200

Transaction Audit
Duplicate transaction ID: A1
Amount above threshold: A2 600.0
```

## Conclusion
The program uses lists and conditional statements to identify repeated transaction identifiers and unusually large transaction amounts.
