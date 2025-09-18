'''4. Write a program to filter a list of numbers which are divisible by 5.'''
numbers =[5,6,7,8,9,10,13,14,15]

def divisible_by_5(n):
    if (n%5==0):
        return True
    return False

only_divisible_by_5= filter(divisible_by_5,numbers)
print(list(only_divisible_by_5))