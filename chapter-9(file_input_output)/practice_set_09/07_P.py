'''Write a program to find out the line number where python is present from ques 6'''
flag=0
with open("log.txt","r") as f:
    lines=f.readlines()
line_no=1
for line in lines:
    if "python" in line:
        flag=1
        break
        
    
    line_no+=1
if flag==1:
    print(f"Yes python is present in line {line_no}")
else:
    print("No python is not present in file")