# this is a simple programme to create a class calculator capable of finding square cube and square root of a number

import math
n = int(input("enter your number: "))
class Calculator:
    s = n * n
    c = n * n * n
    # sq = n ** 0.5
    sqR = math.sqrt(n)
    
    def square(self):
        print(f"the square of n is {self.s}")
    def cube(self):
        print(f"the cube of n is {self.c}")
    def squareRoot(self):
        print(f"the square root of n is {self.sqR}")

f = Calculator()
f.square()
f.cube()
f.squareRoot()