n=int(input("Enter a number: "))
result = 1
fact = 1
for i in range(1,n+1):
    fact = fact * i
    result = result + i/fact
print(result)