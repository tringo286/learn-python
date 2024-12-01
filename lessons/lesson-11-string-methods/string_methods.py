name = "tri Ngo "

print(len(name)) # 8
print(name.find("N")) # 4
print(name.find("q")) # -1 (no result)
print(name.rfind(' ')) # 8 (reverse find)
print(name.capitalize()) # Tri ngo
print(name.upper()) # TRI NGO
print(name.lower()) # tri ngo
print(name.isdigit()) # False (number only)
print(name.isalpha()) # False (alphabetic character only)
print(name.count(' ')) # 2
print(name.replace(' ', '-')) # tri-Ngo-