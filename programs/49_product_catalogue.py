# Tuple-Based Product Catalogue Audit
# Python Activity-Based Learning

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
