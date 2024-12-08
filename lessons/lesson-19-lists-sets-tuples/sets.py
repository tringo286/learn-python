# collection = single variable used to store multiple values 
#       list = [] orderd and changeable. Duplicates OK
#       set = {} unordered and immutalbe, but Add/Remove OK. No duplicates 
#       tuple = () ordered and unchangeable. Duplicates OK. Faster

fruits = {'apple', 'orange', 'banana', 'coconut'}

print(len(fruits)) # 4 
print('apple' in fruits) # True
print('Pineapple' in fruits) # False

fruits.add('cherry')
print(fruits) # {'coconut', 'banana', 'apple', 'cherry', 'orange'}

fruits.remove('apple')
print(fruits) # {'banana', 'cherry', 'coconut', 'orange'}

fruits.pop()
print(fruits) # {'coconut', 'banana', 'cherry'}

fruits.add('cherry')
print(fruits) # No duplicates: {'coconut', 'cherry', 'banana'} 

fruits.clear() # set()