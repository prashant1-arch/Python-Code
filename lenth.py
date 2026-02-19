

s = input("Enter a string: ")

words = s.split()

print("Even length words are:")

for w in words:
    if len(w) % 2 == 0:
        print(w)
