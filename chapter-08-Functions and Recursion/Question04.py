# this is a python program to print star patterns using functions

def pattern():
    n = int(input("enter the number: "))
    for i in range(n,0,-1):
        print("*" * i)

def pattern1():
    n = int(input("ente the number: "))
    for i in range(1, n + 1):
        print(" "* (n - i), "*"* (i * 2 -1))
def diamond():
    n = int(input("enter the number: "))
    for i in range(1,n):
        print(" "* (n - i), "*" * (i * 2 - 1))
    for i in range(n, 0, -1):
        print(" "*(n - i), "*" * (i * 2 - 1))

diamond()