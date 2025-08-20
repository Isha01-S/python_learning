'''1. Write a program using functions to find greatest of three numbers.'''
def greatest_number(a, b, c):
    if a>b and a>c:
        print(f"{a} is the greatest")
    elif b>a and b>c:
        print(f"{b} is the greatest")
    elif c>a and c>b:
        print(f"{c} is the greatest")
    else:
        print("all are equal")

greatest_number(1,2,3)
greatest_number(3,2,1)
greatest_number(1,3,2)
greatest_number(1,1,1)