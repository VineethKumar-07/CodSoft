import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("Welcome to the Simple Password Generator!")
try:
    desired_length = int(input("Enter desired password length: "))
    if desired_length <= 0:
        print("Invalid length. Please enter a positive number.")
    new_password = generate_password(desired_length)
    print(f"Generated password: {new_password}")
except ValueError:
    print("Invalid input. Please enter a valid number.")

