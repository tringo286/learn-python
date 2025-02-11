# super() = Function used in a child class to methods from a parent class (superclass)
#           Allows you to extend the fucntionality of the inherited methods 

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height 

circle = Circle('red', True, 5)
print(circle.color) # red

square = Square('red', False, 6)
print(square.is_filled) # False