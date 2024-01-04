# Recursion

# fibonacci series
def fibonacci(n):
    # base case
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 10):
    print(fibonacci(i))
    