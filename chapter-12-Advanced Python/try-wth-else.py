# sometimes we want to run a piece of code when try was successful we use else:

try:
    a = int(input("enter your number: "))
    print(a)

except Exception as e:          # this gets executed only if try was unsuccessful
    print(e)       

else:
    print("i am inside else")   # this gets executed only if try was successful