def closest_palindrome(word):
    """
    Generate the closest palindrome for a given word by adjusting characters.
    """
    # Convert the word into a list of characters to modify it
    chars = list(word)
    n = len(chars)

    # Adjust characters to make the string a palindrome
    for i in range(n // 2):
        chars[n - i - 1] = chars[i]

    # Return the resulting palindrome as a string
    return ''.join(chars)

# Input: Word to convert to the closest palindrome
input_word = input("Enter a word: ")

# Generate and display the closest palindrome
result = closest_palindrome(input_word)
print(f"The closest palindrome is: {result}")
