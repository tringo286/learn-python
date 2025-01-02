# Match-case statement (switch): An alternative to using many elif statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readalbe

# Example 1
def day_of_week(day):
    match day:
        case 1:
            return 'Sunday'
        case 2: 
            return 'Monday'
        case 3:
            return 'Tuesday'
        case _:
            return 'Not a valid day'

print(day_of_week(1)) # Sunday 

# Example 2
def is_weekend(day):
    match day:
        case 'Sunday' | 'Saturday':
            return True       
        case _:
            return False
        
print(is_weekend('Monday')) # False 