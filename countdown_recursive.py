
 
# Write a recursive function countdown(n) that prints numbers from n down to 0. 
# For example, if n = 5, it should print: 5, 4, 3, 2, 1, 0.

def countdown(n):
    if n < 0:
        return  # base case to stop recursion
    print(n)
    countdown(n - 1)

# Calling the function
countdown(5)

 
