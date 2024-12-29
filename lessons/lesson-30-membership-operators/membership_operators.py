# Membership operators = used to test whelther a value of variable is found in a sequence
#                        (string, list, tuple, set, dictionnary)
#                        1. in 
#                        2. not in

# Example 1
word = 'APPLE'

letter = input('Guess a letter in the secret word: ')

if letter in word:
    print('f{letter} was not found')
else: 
    print(f'There is a {letter}')

# Example 2
students = {'Tri', 'Ngo'}

student = input('Enter the name of a student: ')

if student not in students:
    print(f'{student} was not found')
else:
    print(f'{student} is a student')

# Example 3
email = 'tringo@gmail.com'

if '@' in email and '.' in email:
    print('Valid email')
else:
    print('Invalid email')