# this programme prints the table of a number given by the user using list comprehension

n = int(input("enter your number: "))

table = [n * i for i in range(1,11)]
print(table)