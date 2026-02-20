# this is a program to demonstrate that tuples are immutable.

marks = (23, 45, 67, 89, 12, 34, 56)

print("The marks of the students are: ", marks)

marks(0) = 90 # this will give an error because tuples are immutable, which means we cannot change the values in the tuple after it has been created.