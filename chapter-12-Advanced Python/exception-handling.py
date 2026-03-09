# this is an example of exception handling in python

try :
    a = int(input("enter a number: "))   # this code gets executed and asks for a number if you enter a number the code runs smoothly
    print(a)

except Exception as e:   # if you enter somthing else instead of number this will not show error but this block of code gets executed
    print(e)

print("thank you")