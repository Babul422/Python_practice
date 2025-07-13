# Take a sentence from the user
sentence = input("Enter a sentence: ")

# Initialize the vowel counter
count = 0

# Define all vowels
vowels = "aeiouAEIOU"

# Loop through each character in the sentence
for letter in sentence:
    if letter in vowels:
        count += 1

# Print the total number of vowels
print("Total vowels is:", count)
