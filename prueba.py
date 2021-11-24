# CLASES EJERCICIO 2
class Vectores:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vectores(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vectores(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vectores(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Vectores(self.x / other.x, self.y / other.y, self.z / other.z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)
   
vector1 = Vectores(2, 3, 8)
vector2 = Vectores(4, 5, 6)
print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * vector2)
print(vector1 / vector2)
# --------------------------------------------------