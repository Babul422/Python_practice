# Q8: Write a function that prints the multiplication table of a number

def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Example usage
multiplication_table(5)
