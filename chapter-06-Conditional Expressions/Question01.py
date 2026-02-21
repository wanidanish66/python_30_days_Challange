# this program takes four numbers as input and finds the greatest number among them.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
num4 = input("Enter the fourth number: ")

if num1 > num2 and num1 > num3 and num1 >num4:
    print("num1 is the greatest number among the four numbers.")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("num2 is the greatest number among the four numbers.")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("num3 is the greatest number among the four numbers.")
else:    
    print("num4 is the greatest number among the four numbers.")