''' Write a program to find the sum of first n natural numbers using while loop.'''
natural_number=int(input("enter the number: "))

i=1
sum=0
while i<=natural_number:
    sum+=i
    i+=1
print("the sum is : ", sum)