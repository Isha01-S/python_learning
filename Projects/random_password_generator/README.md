# Password Generator with Strength Meter
*Overview*

# This project is a Python-based password generator that creates strong, customizable passwords based on user preferences.
-It allows users to:
-Choose password length
-Include uppercase letters
-Include special characters
-Include digits
-It also includes a strength meter that evaluates the strength of the generated password based on its length and character      diversity.

# Features
`
✅ User-defined password length
✅ Option to include uppercase, digits, and special symbols
✅ Randomly generated password with at least one of each selected type
✅ Password strength indicator (Weak, Average, Good, Strong)
✅ Simple and clean console-based interface
`
# How It Works

*The program asks the user to specify:*
-Desired password length
-Whether to include uppercase letters, special characters, and digits
-It constructs a pool of characters based on the chosen options.
-Ensures at least one character of each selected type is included.
-Randomly shuffles and generates the password.
-Displays the password strength before showing the final password.
`
Enter the desired password length: 8
Include uppercase letter? (yes/no): yes
Include special character? (yes/no): yes
Include digits? (yes/no): yes
Strength = Strong
7@cCqVf9
`
# Requirements

`Python 3.x
(No external libraries required)
`
# How to Run

*Clone this repository*
`
git clone https://github.com/<your-username>/password-generator.git
cd password-generator
`

*Run the program*
`
python password_generator.py
`