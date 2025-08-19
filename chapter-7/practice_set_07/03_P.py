'''4. Write a program to find whether a given number is prime or not.'''

number=int(input("Enter the number: "))
i=2
flag=1
while i*i<=number:
    if number%i==0:
        flag=0
        break
    i+=1

if flag==0:
    print("not prime")

else:
    print("Prime")