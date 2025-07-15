#"Write a function that takes a number and returns whether it is even or odd."
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

print(check_even_odd(7))  # Output: odd
