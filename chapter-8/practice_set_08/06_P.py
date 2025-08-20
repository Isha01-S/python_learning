'''6. Write a python function which converts inches to cms
1 inch= 2.54 cm'''

def inch_to_cm(inch):
    return inch*2.54

number=float(input("Enter the number : "))
print(f"{number} inch = {inch_to_cm(number)} cm")