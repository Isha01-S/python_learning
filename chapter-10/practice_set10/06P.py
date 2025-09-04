'''6. Can you change the self-parameter inside a class to something else (say
“isha”). Try changing self to “slf” or “isha” and see the effects.'''

#No change self can be replace with any word


# import random
from random import randint
class Train:
    def __init__(isha, trainNo):
        isha.trainNo=trainNo
    def book(isha, fro, to):

        print(f"Ticket is booked in train no {isha.trainNo} from {fro} to {to}")

    def getstatus(isha):
        print(f"Train no {isha.trainNo} is running on time")

    def getfare(isha, fro, to):
        print(f"Ticket fare in train no :{isha.trainNo} from {fro} to {to} is {randint(200, 500)}")

train=Train(12033)
train.fro="ETW"
train.to="NDLS"
train.book(train.fro,train.to)
train.getstatus()
train.getfare(train.fro,train.to)