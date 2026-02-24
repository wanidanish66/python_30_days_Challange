def table():
    num = int(input("Enter a number to display its multiplication table: "))
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
table()