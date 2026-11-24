# Case Study 29: Password Policy Validation Engine

## Problem Statement
Evaluate a sample password against basic rules such as minimum length, uppercase letter, lowercase letter, digit and special character, and report which rules are not satisfied.

## Objectives
1. Apply string operations to examine characters.
2. Check multiple password conditions.
3. Display each failed condition and the final result.

## Assumptions
- The minimum length is 8 characters.
- At least one uppercase letter, lowercase letter, digit and special character is required.
- This is an educational validation example, not a secure password-storage system.

## Algorithm
1. Start.
2. Read a sample password.
3. Check its length.
4. Loop through each character and identify uppercase, lowercase, digit and special character categories.
5. Display every failed rule.
6. Display whether the sample satisfies all rules.
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
INPUT password
SET category flags to false
FOR each character in password
  CHECK uppercase, lowercase, digit or special character
END FOR
CHECK length >= 8
DISPLAY failed rules
IF all rules pass: DISPLAY Valid
ELSE: DISPLAY Not valid
STOP
```

## Python Source Code
```python
password = input("Enter a sample password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

valid = True

if len(password) < 8:
    print("Failed: Minimum 8 characters required")
    valid = False
if not has_upper:
    print("Failed: At least one uppercase letter required")
    valid = False
if not has_lower:
    print("Failed: At least one lowercase letter required")
    valid = False
if not has_digit:
    print("Failed: At least one digit required")
    valid = False
if not has_special:
    print("Failed: At least one special character required")
    valid = False

if valid:
    print("Password satisfies the sample policy")
else:
    print("Password does not satisfy the sample policy")
```

## Test Cases
- Test 1: Sample: Abcdef1! → All rules pass
- Test 2: Sample: abc123 → Length, uppercase and special character fail
- Test 3: Sample: ABCDEFGH → Lowercase, digit and special character fail

## Sample Output
```text
Enter a sample password: abc123
Failed: Minimum 8 characters required
Failed: At least one uppercase letter required
Failed: At least one special character required
Password does not satisfy the sample policy
```

## Conclusion
The program demonstrates string traversal and character-checking methods to evaluate a sample password against a defined policy.
