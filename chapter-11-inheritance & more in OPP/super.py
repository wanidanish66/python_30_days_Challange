class Employee:
    def __init__(self):
        print("constructor of Emoloyee")
    a = 2
class Programmer(Employee):
    def __init__(self):
        print("constructor of Programmer")
    b = 3
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("constructor of Manager")
    c = 5

# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.b,o.a)

o = Manager()
print(o.a,o.b,o.c)