'''Write a program to input name, marks and phone number of a student and format it
using the format function like below:
“The name of the student is Harry, his marks are 72 and phone number is 99999888”'''

name = input("Enter Name:")
marks = int(input("Enter marks:"))
phno = input("Enter Phone no:")

a = "Name : {} \nMarks : {}\nPhone No.:{}\n".format(name, marks, phno)
print(a)