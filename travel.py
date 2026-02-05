total_amount = 0

# Input ticket price per person
ticket_price = float(input("Enter ticket price per person: "))

# Loop for 5 people
for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))

    if age < 12:
        fare = ticket_price - (ticket_price * 30 / 100)
    elif age >= 59:
        fare = ticket_price - (ticket_price * 50 / 100)
    else:
        fare = ticket_price

    total_amount += fare

print("Total ticket amount for 5 people =", total_amount)
