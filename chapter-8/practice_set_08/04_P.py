'''4. Write a recursive function to calculate the sum of first n natural numbers.'''
def sum_of_natural_nums(n):
    if n==0:
        return 0
    return n+sum_of_natural_nums(n-1)

number=int(input("Enter the number: "))
print(f"The sum is : {sum_of_natural_nums(number)}")