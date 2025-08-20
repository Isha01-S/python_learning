'''5. Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*  '''

def star_pattern(n):
    if n==0:
        return
    print("*"*n)
    star_pattern(n-1)

number=int(input("Enter the number : "))
star_pattern(number)