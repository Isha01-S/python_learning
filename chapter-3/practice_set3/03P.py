'''Write a program to detect double space in a string'''

s="Isha is a good  girl"
print(s.find("  "))

'''replace the double space in this problem with single space'''
b= s.replace("  "," ")
print(b)
print(b.find("  "))