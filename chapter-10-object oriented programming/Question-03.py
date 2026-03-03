# this is a simple programme that shows creating object with direct value doesnot changes the class attribute
class Demon:
    a = 4

do = Demon()   
print(do.a)   # prints the class attribute because the instance attribute is not present

do.a = 0      # object attribute is set
print(do.a)   # prints the instance attribute because the instance attribute is present

print(Demon.a) # prints the class attribute