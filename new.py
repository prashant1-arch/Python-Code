a=int(input("Enter a number: "))
for i in range(3):
    c= a%10
    a =a//10
    print(c, end=" ")