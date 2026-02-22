# this program prints the inverted pyramid shape

num = int(input("enter your number: "))

for i in range(num, 0, -1):                    # this loop starts from num to 1
    print(" " * (num - i), "*" * (2 * i - 1))  # in this print statement there are two things the first one prints the spaces
                                               # like " " * num - i == if num is 5 then num - i => 0 * spaces equal 0 spaces
                                               # second is "*"(2*i-1) => 2 * 5 - 1 => 10 -1 => 9