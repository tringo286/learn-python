#Typecasting = the process of converting a variable from one data type to another 
#              str(), int(), float, bool()

name = "Tri Ngo"
age = 25 
gpa = 3.5
is_student = True

print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(gpa))  # <class 'float'>
print(type(is_student))  # <class 'bool'>

gpa = int(gpa)
print(gpa) # 3 

age = float(age)
print(age) # 25.0

age = str(age)
print(age) # 25.0
print(type(age)) # <class 'str'>

name = bool(name)
print(name) # True

name = ''
name = bool(name)
print(name) # False