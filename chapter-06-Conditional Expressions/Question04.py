# this program checks if the username entered by the user is less than 10 characters or not.

name = input("Enter your username: ")

length = len(name)
if length < 10:
    print("your username is less than 10 characters.")
elif length >= 10:
    print("your username is not less than 10 characters.")