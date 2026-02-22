# this program checks if the number entered by the user is prime or not

num = int(input("enter your number: "))

if num < 2:
    print("the number is not prime")
else:
 for i in range(2,num):
    if(num % i) == 0:
        print("number is not prime")
        break
    else:
        print("number is prime")
        break