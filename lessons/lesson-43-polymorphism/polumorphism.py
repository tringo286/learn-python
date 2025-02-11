# Polymorphism = Greek word that means to 'have many forms or faces'
#                Poly = Many 
#                Morphe = Form 

#                Two ways to achieve polymorphism
#                1. Inheritance = an object could be treated of the same type as a parent class
#                2. "Duck typign" = Object must have necessary attributes/methods

class Shape:
    @classmethod
    def area(self):
        pass    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius 

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2  

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5  
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping     

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza('cheese', 8)]

for shape in shapes:
    print(shape.area())

        


