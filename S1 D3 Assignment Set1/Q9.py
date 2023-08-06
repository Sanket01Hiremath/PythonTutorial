def generate_fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)
    return fib_series

# Example usage:
n = 10
fibonacci_series = generate_fibonacci_series(n)
print(fibonacci_series)
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
