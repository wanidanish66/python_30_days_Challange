try:
    a = int(input("enter your number: "))
    b = int(input("enter your number: "))
    div = a/b
    print(div)

except ZeroDivisionError as e:
    print("infinite")