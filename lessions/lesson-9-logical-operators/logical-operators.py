#logical opearators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True 
#                     and = both conditions msut be True
#                     not = inverts the condition (not False, not True)

temp = 25
is_rainning = False

if temp > 35 or temp < 0 or is_rainning:
    print('The outdoor event is cancelled')
else:
    print('The outdoor event is still scheduled')