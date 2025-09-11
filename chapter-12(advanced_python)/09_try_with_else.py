'''try with else in Python'''

try:
    a = int(input("Hey, Enter a number : "))
    print(a)
except ValueError as v:
    print("Heyy")
    print(v)

else:
    print("I am inside else.") #else code will run only when try is successful

