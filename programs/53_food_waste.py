# Food Waste Monitoring System
# Python Activity-Based Learning

days = int(input("Enter number of days: "))
limit = float(input("Enter acceptable wastage percentage: "))

for day in range(1, days + 1):
    prepared = int(input("Meals prepared on day " + str(day) + ": "))
    served = int(input("Meals served on day " + str(day) + ": "))

    if prepared < 0 or served < 0 or served > prepared:
        print("Invalid meal details")
    else:
        leftovers = prepared - served
        if prepared == 0:
            percentage = 0
        else:
            percentage = leftovers * 100 / prepared

        print("Leftover meals:", leftovers)
        print("Wastage percentage:", round(percentage, 2), "%")

        if percentage > limit:
            print("Alert: Wastage exceeds acceptable limit")
        else:
            print("Wastage is within acceptable limit")
