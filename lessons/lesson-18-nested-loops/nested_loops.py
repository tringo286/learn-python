# nest loop = A loop within another loop (outer, inner)
#             outer loop:
#                  inner loop:

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()

# 123456789
# 123456789
# 123456789