# this is a random guess game

import random

bot = random.randint(1,40)
user = -1

guesses = 0

while (user != bot):
    guesses += 1
    user = int(input("guess the number: "))

    if user > bot:
        print("the number you guessed is higher please guess the lower number: ")
    elif user < bot:
        print("the number you guessed is lower please guess the higher number: ")
    else:
        print("invalid number")

print(f"you haver guessed the number {bot} correctly in {guesses} attempts")