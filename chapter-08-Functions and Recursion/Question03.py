# this is a program to print the sum of numbers  using functions

def sum(n):
    if n == 1:
        return(1)
    else:
        return n + sum(n-1)
n = int(input("enter your number: "))
print(sum(n))