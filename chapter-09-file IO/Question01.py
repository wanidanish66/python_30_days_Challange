# this is a program which checks if the word is present in the file {comment.txt} or not

file = open("comment.txt", "r")      #this opens the comment.txt file in read mode
read = file.read()                   # reads the content of the file

word = input("Enter a word to search in the file: ")        # tells you to enter the word you want to search

if word in read:                                            # checks if the word you enterd is in the read (comment.txt) file
    print(f"The word '{word}' is present in the file.")     # if yes then prints the yes
else:
    print(f"The word '{word}' is not present in the file.") # if no then this statement prints

file.close()
