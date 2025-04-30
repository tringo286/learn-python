# Recursion in Python

# 1. Factorial 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 2. Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8

# 3. Sum of Natural Numbers
def sum_natural(n):
    if n == 1:
        return 1
    else: 
        return n + sum_natural(n-1)
    
print(sum_natural(5))  # Output: 15

# 4. Reverse String
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # Output: "olleh"