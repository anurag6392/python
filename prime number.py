import string

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def words_with_prime_length(passage):
    """Find words with lengths equal to a prime number."""
    words = passage.translate(str.maketrans('', '', string.punctuation)).split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return prime_length_words

passage = input("Enter a passage: ")

result = words_with_prime_length(passage)
print("Words with prime lengths:", " ".join(result))
