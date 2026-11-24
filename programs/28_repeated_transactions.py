# Repeated Transaction Detection
# Python Activity-Based Learning

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
