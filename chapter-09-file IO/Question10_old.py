# This code reads the content of the "content.txt" file, prints it to the console, 
# and then opens the same file in write mode to delete its content. 
# Finally, it prints a message confirming that the content has been deleted.

with open("content.txt", "r") as file:
    c = file.read()
    print(c)
with open("content.txt", "w") as file:
    pass
    print("The content of the file has been deleted.")