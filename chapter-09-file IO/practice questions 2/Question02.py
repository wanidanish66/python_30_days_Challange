
def student_name(name):
    with open("content1.txt","a") as file:
        file.write(name+" : ")

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