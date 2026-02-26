# this code reads the content of the "donkey.txt" file, 
# replaces all occurrences of the word "donkey" with "monkey", 
# and then writes the modified content back to the file if the user confirms.

with open("donkey.txt", "r") as file:
    content = file.read()
    # print(content)

conten = content.replace("donkey", "#####")  # replaces all occurrences of "donkey" with "monkey"
# print(conten)

yes = ""
fi = print("Do you want to replace all occurrences of 'donkey' with 'monkey' in the file? (yes/no)")
yes = input("Enter your choice: ")
if yes == "yes":
    with open("donkey.txt", "w") as file:
        file.write(conten)  # writes the modified content back to the file

print("All occurrences of 'donkey' have been replaced with 'monkey' in the file.")