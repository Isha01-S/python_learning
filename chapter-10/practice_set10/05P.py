'''5. Write a Class 'Train' which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.'''
# import random
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo=trainNo
    def book(self, fro, to):

        print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no :{self.trainNo} from {fro} to {to} is {randint(200, 500)}")

train=Train(12033)
train.fro="ETW"
train.to="NDLS"
train.book(train.fro,train.to)
train.getstatus()
train.getfare(train.fro,train.to)