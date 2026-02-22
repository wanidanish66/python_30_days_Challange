# this is a simple program to print right trangle using stars

num = int(input("enter your number: "))

for i in range(1, num+1):              # this loop runs from 1 to n 
    print("* " * i)                    # the star multiplies by i which means every time the value of i increased by 1
                                       # gets multiplied by "*" returns the stars in every row in increased order