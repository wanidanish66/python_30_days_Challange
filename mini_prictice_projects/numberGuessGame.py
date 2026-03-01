#  this is a simple number guessing game 

import random
def number_guess():
    guess = random.randint(1,50)      # the computer will pick a random number between 1 and 50
    count = 0                         # this variable will keep track of the number of attempts the user has made
    attempted_guess = False           # this variable will be used to check if the user has guessed the number correctly or not

    print("i have picked the number now you have to guess it")
    while not attempted_guess:        # this loop will continue until the user has guessed the number correctly
        user_guess = int(input("enter your guess: "))
        count += 1
        if user_guess < guess:
            print("the number you guessed is lower then the number i picked try again")
        elif user_guess > guess:
            print("the number you guessed is higher then the number i picked try again")
        elif user_guess == guess:
            attempted_guess = True
            print("congratulations you guessed the number in {} attempts".format(count))
        else:
            print("enter a valid input")

number_guess()