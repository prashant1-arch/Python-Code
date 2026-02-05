
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a == b and b == c:
    print("Triangle is Equilateral")
elif a == b or b == c or a == c:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")
