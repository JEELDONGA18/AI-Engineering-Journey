class vector:
    def __init__(self,a,b,c) :
        self.a=a
        self.b=b
        self.c=c
        
    def __add__(self1,self2):
        return vector(self1.a+self2.a , self1.b+self2.b, self1.c+self2.c)
    def __mul__(self1,self2):
        return self1.a*self2.a+self1.b*self2.b+self1.c*self2.c
    
    def __str__(self) :
        return f'Vector is ({self.a},{self.b},{self.c})'
    
v1=vector(1,2,3)
v2=vector(4,5,6)
# v3=vector(7,8,9)
print('The addition of the two vectors : ',v1+v2)
print('The multiplication of the two vectors : ',v1*v2)
    