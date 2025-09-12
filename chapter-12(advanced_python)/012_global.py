'''‘global’ keyword is used to modify the variable outside of the current scope.'''

a = 89
def fun():
    global a #if I don't write global a it will print 3 and 89
    a = 3

    print(a)

fun()
print(a)