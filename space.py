
s = input("Enter a string: ")

space = 0
word = 1   

for ch in s:
  if ch == ' ':
        space = space + 1
        word = word + 1

print("Number of spaces:", space)
print("Number of words:", word)
