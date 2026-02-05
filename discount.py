
cost_price = float(input("Enter cost price of the book: "))
discount_percent = float(input("Enter discount percentage: "))
discount_amount = cost_price * discount_percent / 100
selling_price = cost_price - discount_amount
print("Cost Price:", cost_price)
print("Discount:", discount_percent, "%")
print("Selling Price:", selling_price)
