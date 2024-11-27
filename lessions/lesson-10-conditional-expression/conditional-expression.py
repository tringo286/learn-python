# conditional expression = A one-line shortcut for the if-else statement (tenary operator)
#                          Print or assgin one of two values based on a condition 
#                          X if condition else Y 

# Example #1
num = 5
print('Positive' if num > 0 else 'Negative') # Positive
print('Positive' if num < 0 else 'Negative') # Negative

# Example #2
result =  'Even' if num % 2 == 0 else 'Odd'
print(result) # Odd

# Example #3
a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num) # 7
print(min_num) # 6