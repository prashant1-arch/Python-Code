num = int(input("Enter a number: "))

if num > 0 and (num & (num - 1)) == 0:
    print("Number is a power of 2")
else:
    print("Number is NOT a power of 2")
