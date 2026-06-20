class vector:
    def __init__(self,a,b,c) :
        self.a=a
        self.b=b
        self.c=c
    
    def __str__(self) :
        return f'The vector is {self.a}i + {self.b}j + {self.c}k'
    
v1=vector(7,8,10)
print(v1)
    