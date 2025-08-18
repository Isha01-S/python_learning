"""4. Write a program to find whether a given username contains less than 10
characters or not."""

username=input("enter the username: ")

n=len(username)

if n<10:
    print("Username contains less than 10 characters.", n)
else:
    print(f"username contains {n} characters.")