# Exercise 2 Area Circle Calc
# Area = pi x (radius)^2  

import math

radius = float(input('Enter the radius of a circle: ' ))

area = math.pi * pow(radius, 2)

print(f'The area of the circle is: {round(area, 2)}cm^2')