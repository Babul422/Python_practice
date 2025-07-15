# Q7: Write a function that checks if a string is a palindrome

def is_palindrome (text):
    return text == text[::-1]
 #example uses
print(is_palindrome("madam")) #true
print(is_palindrome("papa")) #false
