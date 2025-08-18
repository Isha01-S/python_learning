#Write a Python program to fill in a letter template given below with name and date
#letter='''
#     // Dear<|name|>
#     //you are selected!
#      //<|Date|>

# '''

A=input("Enter name:")
D=input("Enter date")

letter='''Dear <|name|>\n you are selected!\n <|date|>'''
letter=(letter.replace("<|name|>",A).replace("<|date|>",D))
print(letter)



