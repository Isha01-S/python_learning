

class Student:#class
    name='madhav'
    grade=10
    def __init__(self,name,grade,percentage,team):
        self.name=name
        self.grade=grade
        self.percentage=percentage
        self.team=team
    def student_details(self):
        print(f"{self.name} is in {self.grade} and has scored {self.percentage}% is in team {self.team}")


team1='A'
team2='B'
student1=Student("keshav",90,90,team1)
student1.student_details()
print(student1.team)