# Write a recursive function print_reverse(n) that prints numbers from 1 to n in reverse order. For example, print_reverse(3) prints: 3, 2, 


def print_reverse(n):
    if n <= 0:
        return
    print(n)
    print_reverse(n - 1)

# Example usage:
print_reverse(3)
