customer = int(input("Input (Number of customers): "))
code = input("Input (Discount code): ")
discount = 0
if customer > 6:
    price = 599
elif customer > 3:
    price = 499
else:
    price = 399
subtotal = customer * price
if code == "CASH":
    discount = 0.05
elif code == "BIRTHDAY":
    discount = 0.1
elif code == "COVID":
    discount = 0.3
subtotal = customer * price
print("%d person x %.2f baht" %(customer, price))
print("On-top discount %.0f%%" %(discount * 100))
print("A total price is %.2f baht" %(subtotal * (1-discount)))