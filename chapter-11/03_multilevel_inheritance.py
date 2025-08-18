class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3

n=Manager()
print(n.a, n.b, n.c)