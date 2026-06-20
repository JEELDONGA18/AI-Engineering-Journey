class complexin:
    def __init__(self,a,b) :
        self.a=a
        self.b=b
        
    def __add__(self1,self2):
        return complexin(self1.a+self2.a , self1.b+self2.b)
    def __mul__(self1,self2):
        real_part=self1.a*self2.a-self1.b*self2.b
        imag_part=self1.a*self2.b-self1.b*self2.a
        return complexin(real_part,imag_part)
    
    def __str__(self) :
        return f'{self.a} + {self.b}i'
    
    def show(self1,self2):
        print(f'The first complex number is : {self1.a}+{self1.b}i .')
        print(f'The second complex number is : {self2.a}+{self2.b}i .')
    
c1=complexin(1,2)
c2=complexin(3,4)
# c=complexin(5,6)
# c.show()
print('The addition of the two complex number : ',c1+c2)
print('The multiplication of the two complex number : ',c1*c2)
    