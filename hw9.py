class Shape:
    def __init__(self, color):
        self.color = color

    def howManySides(self):
        print("This shape has multiple sides or a curved boundary")


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def howManySides(self):
        print("Rectangle has 4 sides")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def howManySides(self):
        print("Circle has no straight sides")


rect = Rectangle("Red", 10, 5)
circle = Circle("Blue", 7)

print("Rectangle color:", rect.color)
rect.howManySides()

print("Circle color:", circle.color)
circle.howManySides()