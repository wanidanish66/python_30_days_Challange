# this programme stores the table of a number given by the user in "table.txt" file using list comprehension

n = int(input("enter your number: "))

table = [n * i for i in range(1,11)]
print(table)

with open("table.txt","a") as f:
    f.write(str(table) + "\n")