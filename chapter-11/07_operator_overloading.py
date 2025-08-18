class Number:
    a=1
    b=2
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n + num.n

n=Number(1)
m=Number(2)
print(n+m)
        