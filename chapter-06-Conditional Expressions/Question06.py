# this program checks the marks entered by the user and prints the grade according to the marks.

StMarks = int(input("enter your marks:"))

if StMarks > 90 and StMarks <= 100:
        print("your grade is EXCELLENT")
elif StMarks > 80 and StMarks <= 90:
        print("your grade is A")
elif StMarks > 70 and StMarks <= 80:
        print("your grade is B")
elif StMarks > 60 and StMarks <= 70:
        print("your grade is C")
elif StMarks > 50 and StMarks <= 60:
        print("your grade is D")
elif StMarks > 40 and StMarks <= 50:
        print("your grade is F")