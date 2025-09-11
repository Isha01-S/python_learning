'''raising exceptions in Python'''

a = int(input("Enter the first number : "))
b = int(input("Enter the first number : "))

if b==0:
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero.")

else:
    print(f"the division a/b is {a/b}")

