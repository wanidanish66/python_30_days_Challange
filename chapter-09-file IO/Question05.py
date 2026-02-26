# This code reads the content of the "donkey.txt" file, 
# replaces all occurrences of certain censored words with "*****", 
# and then writes the modified content back to the same file. 

censored = ["donkey", "little","love", "tall"]    #created a list of censored words to be replaced in the file
with open("donkey.txt", "r") as file:             # opens the donkey.txt file in read mode to read its content
    content = file.read()                         

for word in censored:                             # iterates through each word in the censored list and replaces it with ***** in the content of the file
    content = content.replace(word,"*****")       # replaces all occurrences of the censored words with ***** in the content of the file
 
with open("donkey.txt", "w") as file:             # opens the donkey.txt file in write mode to write the modified content back to the file
    file.write(content)                           # writes the modified content back to the file
print("All occurrences of the censored words have been replaced with ***** in the file.")