'''2. Write a program to print third, fifth and seventh element from a list using enumerate
function.'''

l = [1,2,3,4,5,6,6,7,7,54,44,4242,6454,332,4]

for index , item in enumerate(l):
    if index==2 or index==4 or index==6:
        print(f"The element {index + 1} is {item}")