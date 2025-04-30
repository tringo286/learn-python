# Recursion in Python

## Basic Structure of Recursive Function

```python
def recursive_function(parameters):
    if base_case_condition:
        return base_result
    else:
        return recursive_function(modified_parameters)
```

## Base Case and Recursive Case

**Base Case:**  
This is the condition under which the recursion stops. It is crucial to prevent infinite loops and to ensure that each recursive call reduces the problem in some manner.  
In the factorial example, the base case is when `n == 0`.

**Recursive Case:**  
This is the part of the function that includes the call to itself. It must eventually lead to the base case.  
In the factorial example, the recursive case is the function calling itself with `n - 1`.

Example:

```py
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 120
```

## Advantages of Using Recursion

**Simplicity:**  
Recursive code is generally simpler and cleaner, especially for problems inherently recursive in nature (e.g., tree traversals, dynamic programming problems).

**Reduced Code Length:**  
Recursion can reduce the length of the code since the repetitive tasks are handled through repeated function calls.

## Disadvantages of Using Recursion

**Memory Overhead:**  
Each recursive call adds a new layer to the stack, which can result in significant memory use, especially for deep recursion.

**Performance Issues:**  
Recursive functions may lead to slower responses due to overheads like function calls and returns.

**Risk of Stack Overflow:**  
Excessive recursion can lead to a stack overflow error if the recursion depth exceeds the stack limit.
