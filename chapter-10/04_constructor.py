class Employee:
    
    language="Python" #class attributes
    salary=100000

    def __init__(self,name,language,salary): #dunder method which is automatically called.
        self.name=name
        self.language=language
        self.salary=salary
        print("I am creating an object.")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Morning")
        

isha=Employee("Isha","C",200000)
#isha.name="Isha"  #object or instance attribute
print(isha.name,isha.language,isha.salary)