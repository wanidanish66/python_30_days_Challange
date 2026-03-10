# printed the third fifth and seventh element present in the list using enumerate

list = [23, 54, 7, 2, 9, 43, 22, 99, 87, 43]

print(list)

for i, item in enumerate(list):
    if i == 2:
        print(i,item)  # this prints the third element present in the list with index
    elif i == 4:
        print(i,item)  # this prints the fifth element present in the list with index 
    elif i == 6:
        print(i,item)  # this prints the seventh element present in the list with index

