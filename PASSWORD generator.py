import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special=True):
    # Define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special = string.punctuation if include_special else ''
    
    if not (uppercase or digits or special):
        print("Error: At least one character type must be included.")
        return None
    
    characters = lowercase + uppercase + digits + special
    
    # Ensure at least one character from each selected set is included
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_digits:
        password.append(random.choice(digits))
    if include_special:
        password.append(random.choice(special))
    
    # Fill the rest of the password length with random characters
    password += [random.choice(characters) for _ in range(length - len(password))]
    
    # Shuffle to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def main():
    # Ask the user for the desired length and options for the password
    try:
        length = int(input("Enter the length of the password: "))
        if length < 8:
            print("Password length should be at least 8 characters.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    # Generate and display the password
    password = generate_password(length, include_uppercase, include_digits, include_special)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
