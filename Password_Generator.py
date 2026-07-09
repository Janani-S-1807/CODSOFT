import random
import string

try:
    length = int(input("Enter the password length: "))

    if length <= 0:
        print("Please enter a positive number.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")