'''use of map filter and reduce'''
from functools import reduce
#map examples
l=[1,2,3,4,5]

square=lambda x:x*x

sq_list = map(square,l)
print(list(sq_list))

#Filter Example

def even(n):
    if (n%2==0):
        return True
    return False

only_even = filter(even,l)
print(list(only_even))

#reduce examples

def sum(a,b):
    return a+b

print(reduce(sum,l))

