# collection = single variable used to store multiple values 
#       list = [] orderd and changeable. Duplicates OK
#       set = {} unordered and immutalbe, but Add/Remove OK. No duplicates 
#       tuple = () ordered and unchangeable. Duplicates OK. Faster

fruits = ('apple', 'orange', 'banana', 'coconut') 

print(len(fruits)) # 4

print('apple' in fruits) # True
print('pineaple' in fruits) # False
print(fruits.index('apple')) # 0
print(fruits.count('apple')) # 1

for fruit in fruits:
    print(fruit) 
'''
apple
orange
banana
coconut
'''