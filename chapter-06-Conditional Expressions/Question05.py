# this program checks if the name entered by the user is in the list or not.

list = ["apple", "banana", "cherry", "date", "fig", "grape"]

name = input("enter the name you want to check: ")

if name in list:
    print("the name you entered is in the list.")
else:
    print("the name you entered is not in the list.")