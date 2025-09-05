class Employee:
    a=1
    @classmethod #this shows class attributes 
    def show(cls):
        print(f"The class value of a is {cls.a}. ")

e= Employee()
e.a=45

e.show()
