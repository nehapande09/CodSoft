# TASK3: PASSWORD GENERATOR
import random
import string

def generate_password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "difficult":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose from 'easy', 'medium', or 'difficult'.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))

    complexity = input("Choose the complexity level (easy, medium, difficult): ").lower()

    generated_password = generate_password(length, complexity)

    if generated_password:
        print("Generated Password: " + generated_password)

if __name__ == "__main__":
    main()
