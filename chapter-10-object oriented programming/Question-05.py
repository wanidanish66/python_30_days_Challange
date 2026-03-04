# this is a simple program to Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

import random
class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def bookTicket(self,fro,to):
        print(f"the ticket is booked for train no. {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"the number of seats avalible is 45")
    def fare(self,fro,to):
        print(f"the fair of the train no {self.trainNo} is {random.randint(200,500)}")

t = Train(678)
t.bookTicket("jammu","kashmir")
t.getStatus()
t.fare("jammu","kashmir")
