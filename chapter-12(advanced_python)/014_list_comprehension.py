'''List Comprehension is an elegant way to create lists based on existing lists.'''

myList = [1,12,13,14,5,6]

# squaredList = []

# for item in myList:
#     squaredList.append(item*item)

squaredList =[i*i for i in myList]
print(squaredList)