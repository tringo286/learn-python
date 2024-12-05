# for loops = excecute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etec. 

for x in range(1, 11):
    print(x)

# Loop in reverse order
for x in reversed(range(1,11)):
    print(x)

# Step = 2 
for x in range(1, 11, 2):
    print(x)

# Skip 13
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)

# Break the loop at 13
for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)