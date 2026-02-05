import math

# Input values
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
# Calculate discriminant
D = b*b - 4*a*c

# Check nature of roots
if D > 0:
    r1 = (-b + math.sqrt(D)) / (2*a)
    r2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are real and different")
    print("Root 1 =", r1)
    print("Root 2 =", r2)

elif D == 0:
    r = -b / (2*a)
    print("Roots are real and equal")
    print("Root =", r)

else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print("Roots are complex")
    print("Root 1 =", real, "+", imag, "i")
    print("Root 2 =", real, "-", imag, "i")
        
