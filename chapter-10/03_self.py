class Employee:
    
    language="Python" #class attributes
    salary=100000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Morning")
        

isha=Employee()
isha.name="Isha"  #object or instance attribute
print(isha.name,isha.language,isha.salary)

isha.getInfo()

Employee.getInfo(isha)
isha.greet()

