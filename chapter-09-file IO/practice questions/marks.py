with open("marks.txt","r") as file:
    marks = file.read().splitlines()

def add_mark(mark):
    marks.append(mark) 
    with open("marks.txt", "a")as file:
        file.write(f"{mark}\n")


add_mark(int(input("Enter student 1 marks: ")))
add_mark(int(input("Enter student 2 marks: ")))
add_mark(int(input("Enter student 3 marks: ")))
add_mark(int(input("Enter student 4 marks: ")))

 
with open("marks.txt","r") as file:
    marks = file.read().splitlines()
    for mark in marks:
        average = sum(int(mark) for mark in marks) / len(marks)
    print(f"Average marks: {average}")
    
    highest_marks = 0
    for mark in marks:
        if int(mark) > highest_marks:
            highest_marks = int(mark)
    print(f"Highest marks: {highest_marks}")

    count = 0
    for mark in marks:
        if int(mark) > average:
            count += 1
    print(f"Number of students with marks above average: {count}")

    low_marks = int(marks[0])
    for mark in marks:
        if int(mark) < low_marks:
            low_marks = int(mark)
    print(f"Lowest marks: {low_marks}")

    with open("marks1.txt", "w") as dest:
        for mark in marks:
            dest.write(f"{mark}\n")

    with open("grades.txt","w") as file:
       grade = ""
       for mark in marks:
        if int(mark) > 90:
            grade = "A"
        elif int(mark) > 70:
            grade = "B"
        elif int(mark) > 50:
            grade = "C"
        elif int(mark) < 50:
            grade = "D"

        file.write(f"{mark} - {grade}\n")
