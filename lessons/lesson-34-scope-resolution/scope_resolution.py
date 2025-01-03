# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
 
# Local scope 
def func1():
    a = 1
    print(a)

func1() # 1

# Enclosed scope
def func2():
    x = 2
    def func3():
        print(x)
    func3()

func2() # 2

# Global scope 
x = 3
def func3():
    print(x)

func3() # 3

# Built-in scope 
from math import pi

print(pi) # 3.141592653589793
