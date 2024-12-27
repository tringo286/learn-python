# *args    = allows you pass multiple non-key argumnets (tuple)
# **kwargs = allow you pass multiple keyword-arguments (dictionary)
#          * unpacking operator
#          1. postional 2. default 3. keyword 4. ARBITRARY 

# Example 1
def add(*nums):
    total = 0
    for num in nums:
        total += num    
    return total

print(add(1,2,3)) # 6 

# Example 2
def display_name(*args):
    for arg in args:
        print(arg, end=' ')

display_name('Dr.','Sponge','Bob') # Dr. Sponge Bob

# Example 3
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_address(street='123 Fake St.',
              City='Detroit',
              state='MI',
              zip='54321')

'''
City: Detroit
state: MI
zip: 54321
'''

# Example 4
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    for key, value in kwargs.items():
        print(f'{key}: {value}')

shipping_label('Dr.', 'Spongebob', 
                street='123 Fake St.',
                City='Detroit',
                state='MI',
                zip='54321')
'''
Dr. Spongebob
street: 123 Fake St.
City: Detroit
state: MI
zip: 54321
'''