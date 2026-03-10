# this code wants to open file which is not present so this will give an error 
# but with try method it gives a  message (no such file or directory)

try:
    with open("1.txt","r") as f:
        read = f.read
        print(read)
        
except Exception as e:
    print(e)

try:
    with open("2.txt","r") as f:
        read = f.read
        print(read)

except Exception as e:
    print(e)

try:
    with open("3.txt","r") as f:
        read = f.read
        print(read)

except Exception as e:
    print(e)

