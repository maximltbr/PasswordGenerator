import random
import string


def generate_password(length=8):
    # Define the character set: lowercase letters, digits, and special characters
    characters = string.ascii_lowercase + string.digits + string.punctuation

    # Randomly choose 'length' characters from the character set
    password = ''.join(random.choices(characters, k=length))
    return password


# Generate and print an 8-character password
random_password = generate_password()
print("Generated Password:", random_password)
