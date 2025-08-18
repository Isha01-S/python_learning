'''Write a program to input 8 numbers from the user and display all the unique numbers once.'''

s = set()

n=(input("Enter the first number:"))
s.add(int(n))
n=(input("Enter the second number:"))
s.add(int(n))
n=(input("Enter the third number:"))
s.add(int(n))
n=(input("Enter the fourth number:"))
s.add(int(n))
n=(input("Enter the fifth number:"))
s.add(int(n))
n=(input("Enter the sixth number:"))
s.add(int(n))
n=(input("Enter the seventh number:"))
s.add(int(n))
n=(input("Enter the eighth number:"))
s.add(int(n))

print(s)