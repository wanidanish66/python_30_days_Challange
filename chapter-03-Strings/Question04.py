# this code replace the double space in the string with a single space and prints the string after replacing the double space

letter = "hello my  name is micro"

find = letter.find("  ") #finds the double space in the string and returns the index of the first occurrence
print(find) #prints the index of the first occurrence of the double space in the string

find = letter.replace("  ", " ") #replaces the double space with a single space
print(find) #prints the string after replacing the double space with a single space