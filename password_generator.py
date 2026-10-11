import string
import secrets

print("===== RANDOM PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length: "))

    if length < 1:
        print("Password length must be greater than zero.")

    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = []

        for i in range(length):
            password.append(secrets.choice(characters))

        password = "".join(password)

        print("\nGenerated Password:", password)
        print("Password length:", len(password))

except ValueError:
    print("Invalid input. Please enter a whole number.")