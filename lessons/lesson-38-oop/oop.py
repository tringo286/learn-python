# object = A bundle of related attributes (variables) and methods (functions) 
#          Ex. phone, cup, book
#          You need a 'class' to create many objects

# class  = (blue print) used to design the structure and layout of an object 

from my_car import my_car

class Car:
    
    # Constructer method to construct object
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f'You drive the {self.model}')

    def stop(self):
        print(f'You stop the {self.model}')

car1 = Car('Mustang', 2024, 'red', False)

print(car1) # <__main__.Car object at 0x00000247AA675550> (memory addess of the car object)

print(car1.model) # Mustang
print(car1.for_sale) # False 

car2 = Car('Corvette', 2025, 'blue', True)

print(car2.color) # blue
print(car2.year) # 2025
car2.drive() # You drive the Corvette


car3 = my_car('Charger', 2026, 'yellow', True)

print(car3.model) # Charger
car3.stop() # Yoy stop the Charger