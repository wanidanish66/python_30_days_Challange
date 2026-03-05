# class Employee:
#     a = 1

#     def show(self):
#         print(f"this is a class attribute {self.a}")

# e = Employee()
# e.a =43

# e.show()  # this prints a = 43 because the object attribute is present  now we will use class method decorator on same problem

class Employee:
    a = 4

    @classmethod
    def show(slf):
        print(f"this is a class attribute {slf.a}")

e = Employee()
e.a =43

e.show() # now this will print the class attribute because we use class method