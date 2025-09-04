'''4. Add a static method in problem 2, to greet the user with hello.'''

class Calculator:
    def __init__(self, number):
        self.number=number

    @staticmethod
    def greet():
        print("Hello! You can use this calculator to find square, cube and squareroot")

    def square(self):
        print(f"The square is {self.number*self.number}")
    
    def cube(self):
        print(f"The cube is {self.number*self.number*self.number}")

    def square_root(self):
        print(f"The square root is : {self.number**1/2}")


a = Calculator(4)
a.greet()
a.square()
a.cube()
a.square_root()