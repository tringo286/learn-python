# if = Do some code only IF some condition is True 
#    ELSE do something else

# Example #1
age = int(input('Enter your age: '))

if age > 100:
    print("You're too old to sign up")
elif age >= 18:
    print('You are now signed up')
elif age < 0:
    print("You haven't been born yet")
else:
    print('You must be 18+ to sign up')

# Example #2
res = input('Would you like food? (Y/N):')

if res == "Y":
    print('Have some food!')
else:
    print('No food for you!')

# Example #3
name = input('Enter you name: ')

if name =="":
    print('You did not type in your name')
else:
    print(f'Hello {name}')

# Exmaple #4

for_sale = True

if for_sale:
    print('This item is for ')