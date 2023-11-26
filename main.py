class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

v1 = Vector(10, 20)
v2 = Vector(30, 40)
print(v1 + v2)