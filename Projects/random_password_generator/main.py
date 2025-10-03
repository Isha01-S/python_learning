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
    include_uppercase = input("Include uppercase letter? (yes/no):").strip().lower()
    include_special = input("Include special character? (yes/no):").strip().lower()
    include_digits = input("Include digits? (yes/no):").strip().lower()
    
    if length < 4:
        print("Password length must be at least 4 characters.")
        return
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase=="yes" else "" #inline if statement
    special = string.punctuation if include_special=="yes" else ""
    digits = string.digits if include_digits=="yes" else ""
    
    all_characters = lowercase+uppercase+special+digits
    
    required_characters =[]


generate_password()


