# This code reads the content of the "log.txt" file and writes it into a new file called "log2.txt".

with open("log.txt", "r") as file:
    content = file.read()

with open("log2.txt", "w") as d:    # opens the log2.txt file in write mode to write the content of log.txt into it
    d.write(content)
