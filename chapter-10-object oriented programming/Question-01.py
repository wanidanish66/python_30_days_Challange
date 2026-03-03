# this is a simple programme to store name of empoloyees in a class programmer working on a company microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin_code):
        self.name = name
        self.salary = salary
        self.pin_code = pin_code
        
print("company : "+Programmer.company)
m = Programmer("micro",120000,19113)
print(m.name, m.salary, m.pin_code)

m = Programmer("joy",100000,19113)
print(m.name, m.salary, m.pin_code)

m = Programmer("roy",13500,19113)
print(m.name, m.salary, m.pin_code)