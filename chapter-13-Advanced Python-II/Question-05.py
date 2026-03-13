# this is a program  to find the maximum of the numbers in a list using the reduce function

from functools import reduce

l = [3,76,10,40,56,35,64,65]

def greater(a,b):
    if a > b:
        return a 
    return b

print(reduce(greater, l))