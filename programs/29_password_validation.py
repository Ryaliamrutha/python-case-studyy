# Password Policy Validation Engine
# Python Activity-Based Learning

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
