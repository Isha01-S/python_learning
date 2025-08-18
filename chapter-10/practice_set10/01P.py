'''Create a class programmer for storing information of few programmers working at microsoft'''
class programmer:
    company="microsoft"
    
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

    def working(self):
        print(f"programmer {self.name} is working at {self.company} ")

isha=programmer("Isha",100000,206001)
isha.working()

print(isha.name)
print(isha.company)
print(isha.pin, isha.salary)