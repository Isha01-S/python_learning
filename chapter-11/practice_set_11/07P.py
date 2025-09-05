'''7. Override the __len__() method on vector of problem 5 to display 
the dimension of the
vector.'''

class Vector:
    def __init__(self,list):
        self.list=list


    def __len__(self):
        return len(self.list)

    

v1 = Vector([1,2,3]) #here v1 is the object of class vector

print(len(v1))
