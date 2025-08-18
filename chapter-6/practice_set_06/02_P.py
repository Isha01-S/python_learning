"""2. Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user."""

subject1=int(input("Enter the Percentage : "))

subject2=int(input("Enter the Percentage : "))

subject3=int(input("Enter the Percentage : "))

total=(subject1+subject2+subject3)/3

if total>=40 and subject1>=33 and subject2>=33 and subject3>=33:
    print("Pass",total)

else:
    print("Not Pass",total)
    