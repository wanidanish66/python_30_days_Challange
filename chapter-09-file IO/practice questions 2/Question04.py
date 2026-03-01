# this program takes the numbers from 1 to 20 and writes it to the file numbers.txt and reads the file
# and prints only the even numbers to the user

with open("numbers.txt","w") as file:
    for i in range(1,21):
        file.write(str(i)+ "\n")

with open("numbers.txt","r") as file:
    read = file.read()
    for i in read.split():
        if int(i) % 2 == 0:
            print(i)