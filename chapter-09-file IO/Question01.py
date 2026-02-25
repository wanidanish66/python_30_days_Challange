file = open("comment.txt", "r")
read = file.read()

word = input("Enter a word to search in the file: ")

if word in read:
    print(f"The word '{word}' is present in the file.")
else:
    print(f"The word '{word}' is not present in the file.")

file.close()
