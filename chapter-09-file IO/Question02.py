import random                 # imports random function to generate the random numbers
def game():                   # created a function called game
    score = random.randint(1,550)   # score as a variale takes random numbers from 1 to 550
    file = open("high-score.txt")   # opens the high-score.txt file present in the folder as read mode
    read = int(file.read())         # reads the file content to fetch the high score
    if read == "":                  # if the file is empty
        read == 0                   # read value set as 0
    else:
        read == int(read)           # read value is converted to integer
    file.close()
    print("this is your score: ", read)

    if score > read:             # if your score is greater than the high score
        print("you have a new high score: ",score)  # prints the new high score

        file = open("high-score.txt","w")    # opens the high-score.txt file in write mode to update the new high score
        file.write(str(score))               # writes the new high score in the file
        file.close()
    else:
        print("you dont have a high score")
game()