import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """Generate a random password based on user-defined criteria."""
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type (letters, numbers, symbols) must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_to_file(filename, passwords):
    """Save generated passwords to a file."""
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')
    print(f"Passwords saved to {filename}")

def main():
    print("Welcome to the Password Generator!")

    # Prompt user for number of passwords to generate
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                print("Error: Number of passwords must be a positive integer.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid integer.")

    # Prompt user for password length
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Error: Password length must be a positive integer.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid integer.")

    # Prompt user for character set preferences
    use_letters = input("Include letters (y/n)? ").lower() == 'y'
    use_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    use_symbols = input("Include symbols (y/n)? ").lower() == 'y'

    # Generate passwords
    passwords = [generate_password(length, use_letters, use_numbers, use_symbols) for _ in range(num_passwords)]

    # Display generated passwords
    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password {idx}: {password}")

    # Prompt user to save passwords to a file
    save_file = input("\nDo you want to save the passwords to a file? (y/n): ").lower()
    if save_file == 'y':
        filename = input("Enter the filename to save passwords to (include extension, e.g., passwords.txt): ")
        save_to_file(filename, passwords)

if __name__ == "__main__":
    main()
