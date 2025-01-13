# multiple inheritance = inherit from more than one parent class 
#                        C(A, B) C inherits from A and B 
# multilevel inheritance inherit from a parent which inherits from another parent 
#                        C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('This animal is eating')

    def sleep(self):
        print('This animal is sleeping')

class Prey(Animal):
    def flee(self):
        print('This animal is fleeing')

class Predator(Animal):
    def hunt(self):
        print('This animal is hunting')  

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
rabbit.flee() # This animal is fleeing
# rabbit.hunt() # AttributeError: 'Rabbit' object has no attribute 'hunt'

hawk = Hawk()
hawk.hunt() # This animal is hunting
hawk.sleep() # This animal is sleeping

fish = Fish()
fish.flee() # This animal is fleeing
fish.hunt() # This animal is hunting