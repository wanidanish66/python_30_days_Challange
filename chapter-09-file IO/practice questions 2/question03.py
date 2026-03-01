# this program will read the content of a file named content.txt and write it to another file named output.txt and then 
# count the number of times the word "micro" appears in the text and print it to the user

with open("content.txt") as file:
    text = file.read()
    
with open("output.txt", "w") as file:
    file.write(text)

print("Content has been copied to output.txt", len(text), "characters copied")

with open("output.txt") as file:
    text = file.read().split()
counter = 0
for i in text:
    if i == "micro":
        counter += 1
print("The word 'micro' appears", counter, "times in the text.")