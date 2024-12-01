# format specifiers = :{flags} format a vlaue based on what 
#                              flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces 
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate a positive value
# := = place sign to leftmost position
# :  = insert before a positive numbers
# :, = comma separtor

price1 = 3.141591
princ2 = -987.65
price3 = 12.3

print(f'Price 1 is {price1:.2f}') # 3.14
print(f'Price 2 is {princ2:.1f}') # -987.6
print(f'Price 3 is {price3:.3f}') # 12.300

print(f'Price 1 is {price1:10}')  #    3.141591 (10 spaces)
print(f'Price 1 is {price1:010}') # 0003.14159 

# Right justify
print(f'Price 1 is {price1:>10}') # Price 1 is 3.141591
print(f'Price 2 is {princ2:>10}') # Price 2 is -987.6
print(f'Price 3 is {price3:>10}') # Price 3 is 12.3

# Ceter align
print(f'Price 1 is {price1:^10}') # Price 1 is  3.141591
print(f'Price 2 is {princ2:^10}') # Price 2 is  -987.65
print(f'Price 3 is {price3:^10}') # Price 3 is    12.3

# Display plus sign of positive value
print(f'Price 1 is {price1:+}') # Price 1 is +3.141591
print(f'Price 2 is {princ2}') # Price 2 is -987.65

# Comma separators
print(f'Price 1 is {10000:,}') # Price 1 is 10,000

# Mix and match 
print(f'Price 1 is {10000.1234:+,.2f}') # Price 1 is +10,000.12