# 1. Take two numbers from the user and print their sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# 2. Check if a number is even or odd
num = int(input("Enter a number to check even or odd: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Swap two variables without using a third variable
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
x, y = y, x
print("After swapping: x =", x, ", y =", y)

# 4. Find the square of a number
n = int(input("Enter a number to find its square: "))
print("Square:", n * n)

# 5. Take a string input and print its length
text = input("Enter a string: ")
print("Length of string:", len(text))
