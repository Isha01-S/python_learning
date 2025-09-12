'''The ‘enumerate’ function adds counter to an iterable and returns it'''

l = [5, 53, 545, 55]

# index =0
# for item in l:
    
#     print(f"The item number {index} is {item}")
#     index+=1

# this can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number {index} is {item}")