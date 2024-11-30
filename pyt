import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Start with the lowercase set
    characters = lowercase

    # Add the selected character sets based on the options
    if use_uppercase:
        characters += uppercase
    if use_digits:
        characters += digits
    if use_special:
        characters += special_characters

    # Generate a random password by selecting random characters from the available pool
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example usage:
password = generate_password(length=16)  # You can change the length as needed
print("Generated Password:", password)
