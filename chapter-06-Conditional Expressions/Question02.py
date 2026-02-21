# this program will take marks of three subjects as input and calculates the average and total marks and checks if the student has passed or failed the exam. 
# the passing criteria is that the average marks should be greater than or equal to 40 and the marks of each subject should be greater than or equal to 33.

sub1 = input("Enter the marks of subject 1: ")
sub2 = input("Enter the marks of subject 2: ")
sub3 = input("Enter the marks of subject 3: ")

total = int(sub1) + int(sub2) + int(sub3)
average = total / 3

if average >= 40 and int(sub1) >= 33 and int(sub2) >= 33 and int(sub3) >= 33:
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry, You have failed the exam.")    