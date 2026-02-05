#reverse number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
print(reverse_number(12345)) 

#reverse three digit number using for loop
for i in range(3):
    print(i, end='')
    if i> 3:
    print(i, end='')
    