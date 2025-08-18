'''inheritance is a way of creating a new class from an existing class.'''


class Employee: #base class
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company="ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he/she is good with {self.language} language.")

class Programmer(Employee): #derived or child class
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he/she is good at {self.language} language.")

a=Employee()
b=Programmer()

print(a.company, b.company)