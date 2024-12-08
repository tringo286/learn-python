# collection = single variable used to store multiple values 
#       list = [] orderd and changeable. Duplicates OK
#       set = {} unordered and immutalbe, but Add/Remove OK. No duplicates 
#       tuple = () ordered and unchangeable. Duplicates OK. Faster

fruits = ['apple', 'orange', 'banana', 'coconut']

print(fruits[:3]) # ['apple', 'orange', 'banana']
print(fruits[::2]) # ['apple', 'banana']
print('apple' in fruits) # True
print('pineapple' in fruits) # False
print(len(fruits)) # 5 

# iterate thru a list
for fruit in fruits:
    print(fruit) 

fruits.append('cherry')
print(fruits) # ['apple', 'orange', 'banana', 'coconut', 'cherry']

fruits_copy = fruits.copy()
print(fruits_copy) # ['apple', 'orange', 'banana', 'coconut', 'cherry']

fruits.remove('apple')
print(fruits) # ['orange', 'banana', 'coconut', 'cherry']

fruits.insert(0, 'pineapple')
print(fruits) # ['pineapple', 'orange', 'banana', 'coconut', 'cherry']

fruits.sort()
print(fruits) # ['banana', 'cherry', 'coconut', 'orange', 'pineapple']

fruits.reverse() # reserve based on origin order
print(fruits) # ['pineapple', 'orange', 'coconut', 'cherry', 'banana']

fruits.clear()
print(fruits) # []

print(fruits.index('cherry')) # 1
print(fruits.count('banana')) # 1