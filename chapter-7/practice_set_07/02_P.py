'''2. Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Isha", "Soham", "Sachin", "Rahul"]'''

l = ["Isha", "Soham", "Sachin", "Rahul"]

for name in l:
    if name.startswith('S'):
        print(f"Hi {name}")
        