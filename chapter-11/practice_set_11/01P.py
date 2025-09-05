'''1. Create a class (2-D vector) and use it to create another class representing a 3-D
vector.'''

class twoD_vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")

class threeD_vector(twoD_vector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k ")

object1 = twoD_vector(1, 2)
object1.show()
object2 = threeD_vector(1, 2, 3)
object2.show()


