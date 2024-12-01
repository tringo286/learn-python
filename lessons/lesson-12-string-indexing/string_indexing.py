# indexing = accessing elements of a sequence using [] (indexing operator,
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[1]) # 2
print(credit_number[:4]) # 1234
print(credit_number[5:]) # 5678-9012-3456
print(credit_number[-1]) # 6
print(credit_number[0:4:2]) # 13
print(credit_number[::2]) # 13-6891-46

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXXX-{last_digits}") # 3456

credit_number_reversed = credit_number[::-1]
print(credit_number_reversed) # 6543-2109-8765-4321
