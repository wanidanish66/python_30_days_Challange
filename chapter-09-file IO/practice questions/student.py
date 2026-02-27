# This program manages a list of students by allowing the user to add student names, remove duplicates, and perform various operations on the list of students.

with open("students.txt", "r") as file: # Open the file "students.txt" in read mode to load existing student names into a list.
    students =  file.read().splitlines() # Read the contents of the file and split it into lines, creating a list of student names.
    
    # this function adds a new student name to the list and appends it to the file "students.txt". 
    def add_student(name):
        students.append(name)
        with open("students.txt","a") as file:
            file.write(name + "\n")

# Prompt the user to enter student names and add them to the list and file.
add_student(input("Enter student name: "))
add_student(input("Enter student name: "))
add_student(input("Enter student name: "))
add_student(input("Enter student name: "))
add_student(input("Enter student name: "))

# Print all student names in uppercase.

with open("students.txt", "r") as file:
    students =  file.read().splitlines()
    for student in students:
        print(student.upper()) 

# Remove duplicate student names from the list and write the unique names back to the file "students.txt".

with open("students.txt", "w") as file:
    unique_students = set(students)
    for student in unique_students:         
        file.write(student + "\n")
    print("Duplicate students removed.")
    
    # Count the number of students whose names contain the letter "a" and print the result.
    count = 0
    for student in students:
        if student.__contains__("a"):
            count +=1 
    print(f"Number of students with 'a' in their name: {count}")

    # Find and print the student with the longest name from the list of students. 
    longest_name = ""
    for student in students:
        if len(student) > len(longest_name):
            longest_name = student
    print(f"the student with longest name: {longest_name}")