'''3. Create a class with a class attribute a; create an object from it and set 'a'
directly using 'object.a = 0'. Does this change the class attribute?'''

class Demo:
    a=4

classobject= Demo()
print(classobject.a)
classobject.a=0
print(classobject.a)

print(Demo.a)

#class attribute is not changed but instance attribute is set