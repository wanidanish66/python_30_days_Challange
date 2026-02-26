# this code checks if the word python is present in the the log.txt and prints the line number where it is found.

with open("log.txt","r") as file:
    for lineNumber, line in enumerate(file,start = 1):
        if "python" in line.lower():
            print(f"python is present in line {lineNumber}")
        else:
            print(f"python is not present in line {lineNumber}")