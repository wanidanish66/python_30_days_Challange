# this is a basic student management system that allows you to add student info (name, age, grade) to a text file called
#  "student_info.txt".
# you can also search for a student's information by their name, 
# and open the student information to see all the students' information stored in the text file. 
# The student information is stored in a dictionary for easy access.

def add_student_info(name, age, grade):
    with open("student_info.txt", "a") as file:
        file.write(name + " : " + str(age) + " : " + grade + "\n")
        store_student_info = {}            # this dictionary will be used to store the student information
        store_student_info[name] = {"age": age, "grade": grade}      # the name of the student will be the key and the age and grade will be the value in the dictionary
        return store_student_info

def open_student_info():
    with open("student_info.txt", "r") as file:
        student_info = {}
        for line in file:      
            name, age, grade = line.strip().split(" : ")  # the line is stripped of any leading or trailing whitespace and then split into name, age, and grade using the " : " delimiter
            student_info[name] = {"age": age, "grade": grade}
        return student_info
def search_student_info(name):
    student_info = open_student_info()
    if name in student_info:
        return student_info[name]
    else:
        return "Student not found"
print("welcome to the student management system")
print("choose an option: \n" \
"1. Add student information \n" \
"2. Search student information \n"
"3. open student information \n")
option = input("enter the option number: ")
if option == "1":
    add_student_info(input("enter the name of the student: "), input("enter the age of the student: "), input("enter the grade of the student: "))
elif option == "2":    
    print(search_student_info(input("enter the name of the student: ")))
elif option == "3":    
    print(open_student_info())
else:    
    print("invalid option")