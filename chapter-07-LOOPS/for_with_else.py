l = [1,2,4,"mine", "micro"]

for item in l:
    print(item)
if item != "micro":
    print("hello")
else:
    print("done")             # for loop with else

    # the break statement 

    list = [3,6,3,23,54,66,43]   # this is a simple list with items
    for item in list:            # this for loops shows the items in the list
        print(item)              # this prints the items in the list

        if item == 23:           # this if statement instructs us if the item equals to 23 then 
            break                # break the statement and prints the item till break