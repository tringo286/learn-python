# function = a block of reusable code 
#            place () after the function name to invoke it

# return   = statement used to end a function 
#            and send a result back to the caller 

def happy_birthday(name):
    print(f'Happy birthday to {name}!')
    print()

happy_birthday('tri') # Happy birthday to tri!

def display_invoice(username, amount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${amount:.2f} is due: {due_date}')

display_invoice('Joe', 99.99, '12/23')
'''
Hello Joe
Your bill of $99.99 is due: 12/23
'''

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last

full_name = create_name('sponge', 'bob')
print(full_name)