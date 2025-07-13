# Q: Given a string like "abc123", separate and print the alphabets and digits.

# The input string
a = "abc123"

# Step 1: Create two empty strings to store alphabets and digits
alphabets = ""
digits = ""

# Step 2: Loop through each character in the string
for char in a:
    # Q: Is the character an alphabet (a-z or A-Z)?
    if char.isalpha():
        alphabets += char
    # Q: Is the character a digit (0-9)?
    elif char.isdigit():
        digits += char

# Step 3: Print the result
print("Alphabets:", alphabets)
print("Digits:", digits)
