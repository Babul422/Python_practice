# Q9: Write a function that takes a list and returns a new list with only even numbers

def filter_even(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# Example usage
result = filter_even([1, 2, 3, 4, 5, 6])
print("Even numbers:", result)  # Output: [2, 4, 6]
