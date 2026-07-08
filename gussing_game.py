#gussing game
import random
jecko = random.randint(1, 100)
print("Welcome to the guessing game!")
while True:
    guess = int(input("Enter your guess (between 1 and 100): "))
    if guess < jecko:
        print("Too low! Try again.")
    elif guess > jecko:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
    