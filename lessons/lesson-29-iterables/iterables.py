# Iterables = A object/collection that can return its elements one at a time
#            allowing it to be iterated over in a loop 

# Example 1
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number, end=' ') # 5 4 3 2 1 

# Example 2
name = 'Tri Ngo'

for char in name:
    print(char, end=' ') # T r i   N g o

# Example 3
my_dictionary = {'A' : 1, 'B': 2, 'C': 3}
for key, value in my_dictionary.items():
    print(f'{key}: {value}', end=' ') #  A: 1 B: 2 C: 3 