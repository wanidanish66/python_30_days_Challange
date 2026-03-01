# Simple calculator program that performs basic arithmetic operations based on user input.

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))



aval_operations = {   # Dictionary mapping user commands to corresponding functions
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

command = input("Enter your command: ")

if command in aval_operations:
    aval_operations[command](num1, num2)  # Call the corresponding function based on user input
    result = aval_operations[command](num1, num2)
    print(f"The result of {num1} {command} {num2} is: {result}")
else:
    print("Invalid command. Please select a valid operation.")