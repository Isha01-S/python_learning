'''Write a program to display the marks of 6 students and display them in sorted manner'''


stu_marks=[]

m1=int(input("Enter marks : "))
stu_marks.append(m1)
m2=int(input("Enter marks : "))
stu_marks.append(m2)
m3=int(input("Enter marks : "))
stu_marks.append(m3)
m4=int(input("Enter marks : "))
stu_marks.append(m4)
m5=int(input("Enter marks : "))
stu_marks.append(m5)
m6=int(input("Enter marks : "))
stu_marks.append(m6)

print(stu_marks)
stu_marks.sort()
print(stu_marks)


#print(sorted(stu_marks))



