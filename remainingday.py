# Input total days
days = int(input("Enter total number of days: "))

# Calculate years, weeks, and remaining days
years = days // 365
days = days % 365

weeks = days // 7
remaining_days = days % 7

# Output
print("Years =", years)
print("Weeks =", weeks)
print("Remaining Days =", remaining_days)
print("Total Days =", years * 365 + weeks * 7 + remaining_days)
print("Verification Complete")  
print("Thank you for using the program!")
