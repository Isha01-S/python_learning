'''6. Write a program to calculate the factorial of a given number using for loop.'''
number=int(input("Enter the number: "))


facorial=1
for val in range(1,number+1):
    facorial*=val
print(facorial)