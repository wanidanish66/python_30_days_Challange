# This is a program to take marks of 7 students in a list and sort them in ascending order.

list = []

list.append(int(input("Enter the marks of the 1st student: ")))
list.append(int(input("Enter the marks of the 2nd student: ")))
list.append(int(input("Enter the marks of the 3rd student: ")))
list.append(int(input("Enter the marks of the 4th student: ")))
list.append(int(input("Enter the marks of the 5th student: ")))
list.append(int(input("Enter the marks of the 6th student: ")))
list.append(int(input("Enter the marks of the 7th student: ")))

list.sort() # sorts the list in ascending order
print("The marks of the students are: ", list)