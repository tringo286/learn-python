# module = a file containing code you want to include in your program 
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reuseable seperate files

# print(help('modules')) # Lists available modules

# print(help('math')) # Shows 'math' module documentation

import math
print(math.pi) # 3.141592653589793

import math as m 
print(m.pi) # 3.141592653589793

from math import pi # try to avoid due to name conflict
print(pi) # 3.141592653589793  

import my_modules

print(my_modules.pi) # 3.14159
print(my_modules.square(3)) # 9