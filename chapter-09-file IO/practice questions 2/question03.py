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