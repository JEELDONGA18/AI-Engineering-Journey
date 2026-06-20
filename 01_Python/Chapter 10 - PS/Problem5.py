from random import randint
class Train:
    def __init__(self,TrainNo) :
        self.TrainNo=TrainNo
        
    def book(self,fro,to):
        print(f'Ticket is booked in train no : {self.TrainNo} from {fro} to {to}')
        
    def getStatus(self):
        print(f'Train no. : {self.TrainNo} is running on time.')
        
    def getFare(self,fro,to):
        print(f'Ticket fare in train no : {self.TrainNo} and from {fro} to {to} is {randint(1,5000)}')
        
        
t=Train(12345)
t.book('Surat','Jamnagar')
t.getStatus()
t.getFare('Surat','Jamnagar')
