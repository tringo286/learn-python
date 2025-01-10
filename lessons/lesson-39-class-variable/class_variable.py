# class variable = Shared among all instances of a class 
#                  Defined outside the constructor
#                  Allow you to share data among all objects created from that class 


class Student:

    class_year = 2024 # class variable
    num_student = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student('Tri', 20)

student2 = Student('Ngo', 30)
print(student1.name) # Tri
print(student2.age) # 30 

print(student1.class_year) # 2024
print(Student.class_year) # 2024

print(Student.num_student) # 2