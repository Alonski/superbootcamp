class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point: ({}, {})".format(self.x, self.y)

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __add__(self, other):
        return self.add(other)

    def sub(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __sub__(self, other):
        return self.sub(other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

p3 = Point(2,5)
p3 += Point(3, 4)
print(p3)

