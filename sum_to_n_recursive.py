# Write a recursive function sum_to_n(n) that returns the sum of all numbers from 1 to n. For example, sum_to_n(4) should return 1 + 2 + 3 + 4 = 10.

def sum_to_n(n):
    if n <= 0:
        return 0  # Base case: sum of numbers up to 0 is 0
    return n + sum_to_n(n - 1)  # Recursive case

# Example usage:
print(sum_to_n(4))  # Output: 10
