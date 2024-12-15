# dictionnary = a collection of {key:value} pairs 
#               ordered and changeable. No duplicates 

captials = {
            'USA': 'Washington D.C',
            'India': 'New Delhi',
            'China': 'Beijing'
            }

print(captials) # {'USA': 'Washington D.C', 'India': 'New Delhi', 'China': 'Beijing'}
print(captials.get('USA')) # Washington D.C
print(captials.get('Japan')) # None

captials.update({'Germany': 'Berlin'})
print(captials) #{'USA': 'Washington D.C', 'India': 'New Delhi', 'China': 'Beijing', 'Germany': 'Berlin'} 

captials.update({'USA': 'Detroit'})
print(captials) #{'USA': 'Detroit', 'India': 'New Delhi', 'China': 'Beijing', 'Germany': 'Berlin'} 

captials.pop('China')
print(captials) #{'USA': 'Detroit', 'India': 'New Delhi', 'Germany': 'Berlin'} 

captials.popitem()
print(captials) # {'USA': 'Detroit', 'India': 'New Delhi'}

# captials.clear()
# print(captials) # {}

keys = captials.keys()
for key in keys:
    print(key, end=' ') # USA India

values = captials.values()
for value in values:
    print(value, end=' ') # Detroit New Delhi

items = captials.items()
for key, value in items:
    print(f'{key}: {value}') 
'''
USA: Detroit
India: New Delhi
'''