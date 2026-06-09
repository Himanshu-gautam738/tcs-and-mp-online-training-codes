# Fibonacci Sequence using Dynamic Programming (Memoization)

def fibonacci(n, memo={}):
    # If value already computed, return it
    if n in memo:
        return memo[n]
    
    # Base cases
    if n <= 1:
        return n
    
    # Recursive relation with memoization
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Example usage
n = 10
result = fibonacci(n)
print(f"fib({n}) =", result)
