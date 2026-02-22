# this program prints the table of any number entered by the user in reversed order

num = int(input("enter your number: "))

for i in range(10, 0, -1):            # in this for loop the loop starts from 10 and stops befire 0 and -1 number to go backword
    print(num, " x ", i,"=", num*i)   # this line of code prints the table from backword