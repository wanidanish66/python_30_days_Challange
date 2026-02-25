import random
def game():
    number = random.randint(1, 100)

    file = open("high-score.txt", "r")
    high_score = file.read()
    if high_score != "":
        high_score = int(high_score)
    else:
        high_score = 0
    file.close()

    print("your high score is: ", high_score)
    if number > high_score:
        print("Congratulations! You have a new high score!", number)
        file = open("high-score.txt", "w")
        file.write(str(number)) 
        file.close() 
    else:
        print("Sorry! You did not beat the high score. Better luck next time!")
    return number

game() 

