# list comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# Example 1
doubles = [x * 2 for x in range(1, 11)]
print(doubles) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Example 2
fruits = ['apple', 'banaca', 'coconut']
fruits = [fruit.upper() for fruit in fruits]
print(fruits) # ['APPLE', 'BANACA', 'COCONUT']

# Example 3 
numbers = [1 ,2, -3, 4, -5]
positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers) # [1, 2, 4] 