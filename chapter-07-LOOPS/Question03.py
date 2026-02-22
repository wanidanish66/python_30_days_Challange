# this is a simple program to print table of given number by the user using while loop

num = int(input("enter your number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1