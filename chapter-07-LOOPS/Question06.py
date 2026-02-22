# this program prints the factoraial of a number given by the user

num = int(input("enter your number: "))

i = 1                # put value of i = 1
mul = 1              # put value of mul = 1
     
while i <= num:      # checks if i is less or equal to number if yes then the loop continues
    mul *= i         # this line of code multiples the i with mul and returns the value
    i += 1           # this increases the size of i by 1 first i is equal to 1 then it increases and becomes 2 and so on
print(mul)    

# this is the same program with for loop

mult = 1                     # puts the value of mult equal to 1
for i in range (1, num+1):   # this for loop gives the range of numbers from 1 to num+1
    mult *= i                # this line of code multiples the i with mul and returns the value
print(mult)                  # prints the end result
