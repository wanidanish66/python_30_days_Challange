# this program will take the name and marks of 3 students and write it to a file and then read the file and print the content

def student_name(name):     # this fumction will take the name of the student and write it to the file content1.txt
    with open("content1.txt","a") as file:  # "a" is used to append the content to the file instead of overwriting it
        file.write(name+" : ")            # this will write the name of the student followed by a colon and a space to the file content1.txt

def student_marks(mark):
    with open("content1.txt","a") as file:
        file.write(str(mark) + "\n")
student_name(input("enter your name: "))
student_marks(int(input("enter your marks: ")))

student_name(input("enter your name: "))
student_marks(int(input("enter your marks: "))) 

student_name(input("enter your name: "))
student_marks(int(input("enter your marks: ")))

with open("content1.txt","r") as file:
    read = file.read()
    print(read)