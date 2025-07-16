# Write a recursive function factorial(n) that calculates the factorial of a non-negative integer n. For example, factorial(5) should return 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
    if n==0 or n==1:
     return 1
    return n*factorial (n-1)
print(factorial(5))
