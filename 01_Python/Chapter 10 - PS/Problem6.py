from random import randint
class Train:
    def __init__(jeel,TrainNo) :
        jeel.TrainNo=TrainNo
        
    def book(jeel,fro,to):
        print(f'Ticket is booked in train no : {jeel.TrainNo} from {fro} to {to}')
        
    def getStatus(jeel):
        print(f'Train no. : {jeel.TrainNo} is running on time.')
        
    def getFare(jeel,fro,to):
        print(f'Ticket fare in train no : {jeel.TrainNo} fand from {fro} to {to} is {randint(1,5000)}')
        
        
t=Train(12345)
t.book('Surat','Jamnagar')
t.getStatus()
t.getFare('Surat','Jamnagar')
