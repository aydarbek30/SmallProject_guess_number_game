import random


low = 1
high = 100
guesses = 0

number = random.randint(low, high)

while True:
    guesses += 1
    guess = int(input("Enter your number: "))

    if guess > number:
        print(f"{guess} is too high")
    elif guess < number:
        print(f"{guess} is too low")
    else:
        print(f"{guess} correct!")
        break

print(f"Total guesses: {guesses}")
