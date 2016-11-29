class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ";" + str(self.y) + ")"
class Vector :
    def __init__(self, x, y):
        if isinstance(x, Point) :
            self.begin = x
            self.end = y
            self.x = self.end.x - self.begin.x
            self.y = self.end.y - self.begin.y
        if isinstance(x, int) :
            self.x = x
            self.y = y
            self.begin = Point(0, 0)
            self.end = Point(x, y)
    def length2(self) :
        return self.x**2 + self.y**2
    def __add__ (self, other) :
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__ (self, other) :
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__ (self, other) :
        return self.x * other.x + self.y * other.y 
    def __eq__ (self, other) :
        return (self.x == other.x) and (self.y == other.y)
    def __str__(self):
        return "[" + str(self.x) + ";" + str(self.y) + "]"