# this program prints the hollow square

num = int(input("enter your number: "))
for i in range(num):           # if num is 5 this loops runs 5 times
    if i == 0 or i == num-1:   # this checks if i == 0 or i == num - 1
        print("* " * num)       # prints the first and last row
    else:
        print("*", (num - 1) * " ", "*")    # prints the middle rows
