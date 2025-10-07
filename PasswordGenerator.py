import secrets
import string

print("Welcome to the Pypassword Generator!")

while True:
    try:
        letters = int(input("How many letters would you like in your password?\n"))
        symbols = int(input("How many symbols would you like in your password?\n"))
        numbers = int(input("How many numbers would you like in your password?\n"))
    except ValueError:
        print("Please enter numbers only.")
        continue
    password = (
        ''.join(secrets.choice(string.ascii_letters) for _ in range(letters)) +
        ''.join(secrets.choice(string.punctuation) for _ in range(symbols)) +
        ''.join(secrets.choice(string.digits) for _ in range(numbers))
    )

    password = ''.join(secrets.SystemRandom().sample(password, len(password)))

    print(f"Your generated password is:{password}")
    break