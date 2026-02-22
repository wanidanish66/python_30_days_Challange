# this is a simple program to print inverted right trangle using stars

num = int(input("enter the number: "))   # takes the integer value from the user

for i in range(num,0,-1):                # this loop runs from the num to 0 
    print("* " * i)                      # the star multiplies by i which means every time the value of i decreased by 1
                                         # gets multiplied by "*" returns the stars in every row in decreased order