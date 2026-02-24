# this is a mini project of rock paper scissors game, 
# where you play against the computer. 
# The computer will randomly choose rock, paper, or scissors, and you will input your choice. 
# The program will then determine the winner based on the rules of the game.

import random         # to generate random choices for the computer

Micro = random.choice([1,2,3])      # 1 for rock, 2 for paper, 3 for scissors

youstr = input("Enter your choice (rock, paper, scissors): " ).lower()   # get user input and convert it to lowercase for consistency

youDict = ({"rock": 1, "paper": 2, "scissors": 3})       # created a dictionary to map user input to numbers for easier
                                                         # comparison with computer's choice
revDict = {1: "rock", 2: "paper", 3: "scissors"}         # created a reverse dictionary to map computer's choice back to string for display purposes
reverse = revDict[Micro]                                 # used the reverse dictionary to get the computer's choice in string format for display

you = youDict[youstr]                                    # used the user input to get the corresponding number for comparison with computer's choice
print(f"Micro chose: {reverse}")                         # displayed the computer's choice to the user
if you == Micro:
    print("It's a tie!")
elif you == 1 and Micro == 3 or you == 2 and Micro == 1 or you == 3 and Micro == 2:
    print("You win!")
else:
    print("Micro wins!") 