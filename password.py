import random
import string

def generate_password(length):
    # Define the character set
    characters = string.digits + string.digits + string.digits
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage
password_length = 5
print("Generated Password:", generate_password(password_length))