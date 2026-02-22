# this program prints the pyramid pattern  

num = int(input("enter your number: "))

for i in range(1,num + 1):                   # this loop starts from 1 to num 
    print(" " * (num-i), "*" * (2 * i - 1))  # in this print function there are two things ..first one prints spaces and second prints stars