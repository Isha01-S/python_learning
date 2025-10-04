#collect user preferences
#the length of the password
#should contain uppercase
#should contain special character
#should contain digits

#get all available characters
#randomly pick characters upto the length
#ensure we have one of each character types
#ensure length is valid

import random
import string

def generate_password():
    length = int(input("Enter the desired password length:").strip()) #.strip() to remove any of the spaces
    if length < 4:
        print("Password length must be at least 4 characters.")
        return
    include_uppercase = input("Include uppercase letter? (yes/no):").strip().lower()
    include_special = input("Include special character? (yes/no):").strip().lower()
    include_digits = input("Include digits? (yes/no):").strip().lower()
    
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase=="yes" else "" #inline if statement
    special = string.punctuation if include_special=="yes" else ""
    digits = string.digits if include_digits=="yes" else ""
    
    all_characters = lowercase+uppercase+special+digits
    
    required_characters =[]
    if include_uppercase=="yes":
        required_characters.append(random.choice(uppercase))
    if include_special=="yes":
        required_characters.append(random.choice(special))
    if include_digits=="yes":
        required_characters.append(random.choice(digits))

    if include_uppercase=="yes" and include_special=="yes" and include_digits=="yes":
        if length<=5:
            strength="average"
        elif(length<=7):
            strength="good"
        elif(length>=8):
            strength="strong"
    else:
        if(length<=5):
            strength="weak"
        elif(length<=7):
            strength="average"
        elif(length<10):
            strength="good"
        elif(length>=10):
            strength="strong"
    print(f"Strength = {strength.capitalize()}")
    remaining_length = length-len(required_characters)
    password = required_characters

    for _ in range (remaining_length):
        character = random.choice(all_characters)
        password.append(character)
    random.shuffle(password)

    string_password = "".join(password)
    return string_password

password1 = generate_password()

print(password1)


