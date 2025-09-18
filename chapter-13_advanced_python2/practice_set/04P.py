'''5. Write a program to find the maximum of the numbers in a list using the reduce
function.'''
from functools import reduce
num_list=[1,2,3,3,4,1,223]


def max_list(a,b):
    if a>b:
        return a
    return b

print(reduce(max_list,num_list))
