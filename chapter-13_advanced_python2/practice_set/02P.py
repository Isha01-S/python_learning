'''A list contains the multiplication table of 7. write a program to convert it to vertical
string of same numbers.'''
table = [str(7*i) for i in range(1,11)]

final="\n".join(table)#join needs a list of strings
print(final)