from functools import cache

@cache
def fibonacci(n):
    if n <= 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])