class Employee: #base class
    company="ITC"
    def show(self):
        print(f"The name is {self.company}")

class Coder:
    language= "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is you language: {self.language}")


class Programmer(Employee, Coder): #derived or child class
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he/she is good at {self.language} language.")
a=Employee()
b=Programmer()

print(a.company, b.company,b.language)
b.show()
b.printLanguages()
b.showLanguage()