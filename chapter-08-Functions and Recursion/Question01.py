# this is a program using function to print greates of three numbers.

def greatest():
    num1 = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))
    num3 = int(input("enter your third number: "))

    if num1 > num2 and num1 > num3:
        print("num1 is greatest of all three numbers.")
    elif num2 > num1 and num2 > num3:
        print("num2 is greatest of all three numbers.")
    elif num3 > num1 and num3 > num2:
        print("num3 is greatest of all three numbers.")
    else:
        print("the numbers are equal")

greatest()