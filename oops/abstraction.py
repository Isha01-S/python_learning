
class Student:#class
    name='madhav'
    grade=10
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def student_details(self):
        print(f"{self.name} is in {self.grade}")
    
    

#object
student1=Student("isha",12)
student1.student_details() #user doesn't know what is inside student_details this is abstraction
