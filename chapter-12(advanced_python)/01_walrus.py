'''using walrus operator'''

if (n := len([1,2,3,4,5])) > 3:
    print(f"The list is too long ({n} elements, expected <=3)")

