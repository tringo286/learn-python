# keyword arguments = an argument preceded by an indentifier 
#                    helps with readability
#                    order of arguments doesn't matter
#                    1. positional 2. default 3. KEYWORD 3. arbitrary 

# Example #1
def hello(greeting, title, first, last):
    print(f'{greeting} {title}{first} {last}')

hello('Hello', 'Mr.', 'Sponge', 'Bob') # Hello Mr.Sponge Bob
hello('Hello', title='Mr.',last='Bob', first='Sponge') # Hello Mr.Sponge Bob

# Example 2
for x in range(1, 11):
    print(x, end=' ') # 1 2 3 4 5 6 7 8 9 10

print('1', '2', '3', sep='-') # 1-2-3

# Example 3
def get_phone(country, area, first, last):
    return f'{country}-{area}-{first}-{area}'

phone_num = get_phone(country=1, area='123', first='456', last='7890')
print(phone_num) # 1-123-456-123