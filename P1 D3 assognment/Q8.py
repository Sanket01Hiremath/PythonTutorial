def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage:
number = 6
fact = factorial(number)
print(f"The factorial of {number} is {fact}")  # Output: The factorial of 5 is 120
