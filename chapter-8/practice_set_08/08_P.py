'''8. Write a python function to print multiplication table of a given number.'''

def multiplication_table(n):
    for i in range(11):
        print(f"{n}x{i}={n*i}")

n= int(input("Enter the number : "))
multiplication_table(n)