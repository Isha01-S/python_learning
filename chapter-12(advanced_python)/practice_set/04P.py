'''4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
handling the ‘ZeroDivisionError’'''
a = int(input("enter a : "))
b = int(input("enter b : "))

try:
    print(a/b)

except ZeroDivisionError as e:
    print("Infinite")

print("Executed")