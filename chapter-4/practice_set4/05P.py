'''write a program to count the number of zeros in the following tuple
(7,0,8,0,0,9)'''

my_tuple=(7,0,8,0,0,9)
zeros=0
if my_tuple[0]==0:
    zeros+=1
if my_tuple[1]==0:
    zeros+=1
if my_tuple[2]==0:
    zeros+=1
if my_tuple[3]==0:
    zeros+=1
if my_tuple[4]==0:
    zeros+=1
if my_tuple[5]==0:
    zeros+=1

print(zeros)
#or
n=my_tuple.count(0)
print(n)



