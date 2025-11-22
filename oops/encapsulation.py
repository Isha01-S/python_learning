

class Student:#class
    def __init__(self,name,grade):
        self.name=name
        self.__grade=grade

    def get_grade(self):
        return self.__grade
    def student_details(self):
        print(f"{self.name} is in {self.grade}")
    
    

#object
student1=Student("isha",12)
# print(student1.grade)  gives error

print(student1.get_grade())