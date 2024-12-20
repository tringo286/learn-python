import random

low = 1
high = 100 

number = random.randint(low, high) 
print(number) # 23 

number = random.random()
print(number) # 0.567132808340675

options = ('rock', 'paper', 'scissors')
option = random.choice(options)
print(option) # rock 

cards = ['2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(cards)
print(cards) # ['7', '8', '3', '2', '9', '6', '4', '5']