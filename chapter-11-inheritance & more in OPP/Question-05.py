# this is a programm to represent a vector of n dimentions. overloads + and * operator which calculates sum and "." product

class Vectors:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vectors(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"Vectors({self.x}, {self.y}, {self.z})"
    
v1 = Vectors(1,2,3)
v2 = Vectors(4,5,6)
v3 = Vectors(7,8,9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)