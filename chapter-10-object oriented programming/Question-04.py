# this is a simple programme to create a class calculator capable of finding square cube and square root of a number
# this is Question 2 using static method
import math
n = int(input("enter your number: "))
class Calculator:
    s = n * n
    c = n * n * n
    # sq = n ** 0.5
    sqR = math.sqrt(n)
    
    @staticmethod
    def square():
        print(f"Hello Micro the square of n is {Calculator.s}")
    def cube(self):
        print(f"Hello Micro the cube of n is {Calculator.c}")
    def squareRoot(self):
        print(f"Hello Micro the square root of n is {Calculator.sqR}")

f = Calculator()
f.square()
f.cube()
f.squareRoot()