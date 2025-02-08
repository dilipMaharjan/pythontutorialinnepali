from turtle import circle


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Usage
rectangle = Rectangle(5,5)
circle = Circle(4)

shapes = [Rectangle(4, 5), Circle(3)]

print(rectangle.area())
print(circle.area())


for shape in shapes:
    print(f"Area: {shape.area()}")
# Output:
# Area: 20
# Area: 28.26
