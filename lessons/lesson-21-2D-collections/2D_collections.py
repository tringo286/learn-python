groceries = [
                ['apple', 'orange', 'banana', 'coconut'],
                ['chicken', 'fish', 'turkey']
            ]

print(groceries) # [['apple', 'orange', 'banana', 'coconut'], ['chicken', 'fish', 'turkey']]

print(groceries[0][1]) # orange
print(groceries[1][2]) # turkey

for collection in groceries:
    print(collection)
'''
['apple', 'orange', 'banana', 'coconut']
['chicken', 'fish', 'turkey']
'''

for collection in groceries:
    for food in collection:
        print(food, end=' ')
    print()
'''
apple orange banana coconut
chicken fish turkey
'''