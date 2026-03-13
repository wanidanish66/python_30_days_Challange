# this is a simple program to filter a list of numbers which are divisible by 5.

l = [3,76,10,40,56,35,64,65]

def func(n):
    if n % 5 == 0:
        return True
    return False

devFunc = filter(func,l)
print(list(devFunc))
