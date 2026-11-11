

from abc import ABC ,abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2

class square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

class triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.height*self.base*0.5

class paratha(circle):
    def __init__(self, name, radius):
        super().__init__(radius)
        self.name = name

shapes = [circle(2), square(3), triangle(4, 5), paratha("punjabi", 10)]

for shape in shapes:
    print(shape.area())