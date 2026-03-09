num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if (num2 == 0):
    raise ZeroDivisionError("division by zero is not ment to happen here")
else:
    print(num1 / num2)