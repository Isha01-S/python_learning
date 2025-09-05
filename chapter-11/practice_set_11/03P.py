'''3. Create a class ‘Employee’ and add salary and increment properties to it.
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
which changes the value of increment based on the salary.'''

class Employee:
    salary=5000
    increment=10

    @property
    def salary_after_increment(self):
        return self.salary + self.salary *(self.increment/100) 
    
    @salary_after_increment.setter
    def salary_after_increment(self,salary):
        self.increment =((salary/self.salary) -1)*100


employee_object = Employee()
print(employee_object.salary_after_increment)
employee_object.salary_after_increment=18879
print(employee_object.increment)