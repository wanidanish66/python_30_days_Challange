# This code checks if the word "python" is present in the content of the "log.txt" file and prints a message accordingly.

with open("log.txt", "r") as file:             # opens the log.txt file in read mode to read its content
    content = file.read()                         # reads the content of the file and stores it in the variable content

    if "python" in content.lower():                     # checks if the word "python" is present in the content of the file
        print("python is present in the file")    # checks if the word "python" is present in the content of the file and prints a message if it is found
    else:
        print("python is not present in the file") # checks if the word "python" is not present in the content of the file and prints a message if it is not found