# Case Study 49: Tuple-Based Product Catalogue Audit

## Problem Statement
Store product identifiers, prices and stock quantities in tuples, identify invalid records, calculate inventory values and list products that need replenishment.

## Objectives
1. Represent product records using tuples.
2. Validate prices and stock quantities.
3. Calculate inventory value and identify low-stock products.

## Assumptions
- Each product tuple contains (product_id, price, quantity).
- Price and quantity must be non-negative.
- A product needs replenishment when quantity is below 5.
- Product identifiers should be unique.

## Algorithm
1. Start.
2. Read the number of products.
3. Read each product identifier, price and quantity.
4. Store each record as a tuple in a list.
5. Check for duplicate identifiers and invalid values.
6. For valid records, calculate price multiplied by quantity.
7. Report total inventory value and products with stock below 5.
8. Stop.

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
INPUT number of products
FOR each product
  INPUT id, price, quantity
  STORE (id, price, quantity) as tuple
END FOR
SET total_value = 0
FOR each product tuple
  UNPACK id, price, quantity
  CHECK duplicate id and invalid values
  IF valid
    total_value += price * quantity
    IF quantity < 5: REPORT replenishment
  END IF
END FOR
DISPLAY total_value
STOP
```

## Python Source Code
```python
products = []
n = int(input("Enter number of products: "))

for i in range(n):
    product_id = input("Enter product ID: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter stock quantity: "))
    product = (product_id, price, quantity)
    products.append(product)

total_value = 0
print("\nProduct Catalogue Audit")

for i in range(len(products)):
    product_id, price, quantity = products[i]

    if product_id in [p[0] for p in products[:i]]:
        print("Duplicate product ID:", product_id)

    if price < 0 or quantity < 0:
        print("Invalid product record:", product_id)
    else:
        value = price * quantity
        total_value = total_value + value
        print(product_id, "Inventory value:", value)
        if quantity < 5:
            print("Replenishment required for:", product_id)

print("Total inventory value:", total_value)
```

## Test Cases
- Test 1: P1: price 10, qty 3; P2: price 5, qty 10 → P1 replenishment; total value 80
- Test 2: P1 repeated twice → Duplicate product ID reported
- Test 3: P1 price=-2 → Invalid product record

## Sample Output
```text
Enter number of products: 2
Enter product ID: P1
Enter price: 10
Enter stock quantity: 3
Enter product ID: P2
Enter price: 5
Enter stock quantity: 10

Product Catalogue Audit
P1 Inventory value: 30.0
Replenishment required for: P1
P2 Inventory value: 50.0
Total inventory value: 80.0
```

## Conclusion
The program uses tuples, tuple unpacking and lists to audit product records, calculate stock value and identify products requiring replenishment.
