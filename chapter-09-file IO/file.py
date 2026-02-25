f = open("comment.txt", "r")     #open is a built in function to open a file which opens the file, "r" is for read mode
read= f.read()                   #read is a variable which stores the content of the file which is read by the readlines() method of the file object 
print(read)
r = f.readline()                 #readline is a method of the file object f which reads one line from the file and returns it as a string,
f.close()                        #close is a method of the file object f which closes the file after it is read, 
# it is important to close the file after it is used 
# to free up system resources and avoid potential data loss or corruption.