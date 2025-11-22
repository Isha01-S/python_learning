#parent class

class Student:#class
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def student_details(self):
        print(f"{self.name} is in {self.grade}")


#child class
class Graduate_Student(Student):
    def __init__(self, name, grade,stream):
        super().__init__(name,grade)#call parent class initializer
        self.stream=stream
    def student_details(self):
        print(f"{self.name} is in {self.grade} and is from {self.stream} stream")
student1=Student("madhav",12)
grad_student1=Graduate_Student("keshav",10,"science")
student1.student_details()
grad_student1.student_details()