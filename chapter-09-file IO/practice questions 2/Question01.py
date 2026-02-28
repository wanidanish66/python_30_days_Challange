with open("content.txt") as file:
    text = file.read()
    words = text.split()
    print("the number of words present in the file is: ",len(words))

with open("content.txt") as file:
    lines = file.readlines()
    print("the number of lines present in the file is: ", len(lines))

with open("content.txt") as file:
    text = file.read()
    length = text.count("")
        # words = text.split()
    print("the number of characters present in the file is: ",length)

