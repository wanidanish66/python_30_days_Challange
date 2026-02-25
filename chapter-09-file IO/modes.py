f = open("comment.txt", "r") # open is a built in function to open a file which opens the file, "r" is for read mode
read = f.read() # read is a variable which stores the content of the file which is read by the readlines() method of the file object
print(read) # print is a built in function to print the content of the variable read which contains the content of the file that was read using the read method of the file object f.

f = open("file1.txt", "w") # open is a built in function to open a file which opens the file, "w" is for write mode
f.write("This is a new file") # write is a method of the file object f which writes a string to the file, it takes a string as an argument and writes it to the file, if the file does not exist it creates a new file with the name specified in the open function, if the file already exists it overwrites the existing content of the file with the new content provided in the write method.

f = open("file2.txt", "a") # open is a built in function to open a file which opens the file, "a" is for append mode
f.write("This is an appended line \n") # write is a method of the file object f which writes a string to the file, it takes a string as an argument and writes it to the file, if the file does not exist it creates a new file with the name specified in the open function, if the file already exists it appends the new content provided in the write method to the existing content of the file without overwriting it.

f.close() # close is a method of the file object f which closes the file after it is used, it is important to close the file after it is used to free up system resources and avoid potential data loss or corruption.

file = open("file1.txt", "r")
r = file.read()
print(r)
file.close()

file = open("file2.txt", "r") # open is a built in function to open a file which opens the file, "r" is for read mode
r = file.read() # readline is a method of the file object file which reads one line from the file and returns it as a string, it is used to read the content of the file line by line, it returns an empty string when the end of the file is reached.
print(r) # print is a built in function to print the content of the variable r which contains the content of the file that was read using the readline method of the file object file.
file.close() # close is a method of the file object file which closes the file after it is used, it is important to close the file after it is used to free up system resources and avoid potential data loss or corruption.