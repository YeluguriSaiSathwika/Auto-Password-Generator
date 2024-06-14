import random
import string

def generate_password(length, use_upper, use_digits, use_special):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    # Ensure at least one type is selected
    if not any([use_upper, use_digits, use_special]):
        print("Error: At least one character type must be selected.")
        return None
    
    # Combine all selected character sets
    all_characters = lower + upper + digits + special
    
    if length < 4:
        print("Error: Length must be at least 4 to include one of each selected type.")
        return None
    
    # Generate password
    password = [random.choice(lower)]
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))
    
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length-len(password))
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

print("Welcome to the Password Generator!")
length = int(input("Enter the desired length for the passwords (minimum 4): "))
count = int(input("Enter the number of passwords to generate: "))

if count>0:
    use_upper = input("Include uppercase letters? (Y/N): ").lower() == 'y'
    use_digits = input("Include digits? (Y/N): ").lower() == 'y'
    use_special = input("Include special characters? (Y/N): ").lower() == 'y'

    print()
    if count==1:
        print(count,'new generated password is -')
    if count>1:
        print(count,'new generated passwords are -')
    
    for _ in range(count):
        password = generate_password(length, use_upper, use_digits, use_special)
        if password:
            print(password)

else:
    print()
    print('No password is generated')

print()
