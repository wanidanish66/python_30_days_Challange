# this is a simple program of multilevel inheritance

class Animals:
    a = "Dog"
    b = "cat"
    def an(self):
        print(f"i have two animals {self.a} and {self.b}")
class Pets(Animals):
    @staticmethod
    def pet():
        print(f"both are pets")

class Dogs(Pets):
    def bark(self):
        print(f"the {self.a} is barking")

A = Animals()
P = Pets()
D = Dogs()

D.bark()
D.pet()
P.an()