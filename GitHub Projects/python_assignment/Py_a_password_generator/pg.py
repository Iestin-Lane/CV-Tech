import random
import string


def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Random Password Generator!")
    try:
        # Collect user input for number of passwords and their lengths
        num_passwords = int(input("How many passwords would you like to generate? "))
        password_length = int(input("Enter the desired length of each password: "))

        # Generate the passwords
        passwords = [generate_password(password_length) for _ in range(num_passwords)]

        # Output the generated passwords
        print("\nGenerated Passwords:")
        for i, pwd in enumerate(passwords, start=1):
            print(f"{i}: {pwd}")

    except ValueError:
        print("Please enter valid integers for the number of passwords and their lengths.")


if __name__ == "__main__":
    main()