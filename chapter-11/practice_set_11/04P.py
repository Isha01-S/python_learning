'''4. Write a class ‘Complex’ to represent complex numbers,
 along with overloaded
operators ‘+’ and ‘*’ which adds and multiplies them.'''

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary=imaginary
    def __add__(self, c2):
        return Complex(self.real +c2.real, self.imaginary+c2.imaginary)
    
    def __mul__(self, c2):
        real_part = self.real * c2.real - self.imaginary * c2.imaginary
        image_part = self.real * c2.imaginary + self.imaginary * c2.real
        return Complex(real_part, image_part)
    
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
    
c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2)
print(c1*c2)