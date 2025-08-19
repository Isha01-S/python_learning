'''7. Write a program to print the following star pattern.
  *
 ***
***** for n = 3'''
n=int(input("Enter the number: "))
# x=1
# for i in range(n):
#     print(" "*(n-i),end="")
#     print("*"*(i+x), end="")
#     x+=1
#     print("\n")

for i in range(n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print("\n")