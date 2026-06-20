# class twoDVector:
#     def __init__(self,a,b) :
#         self.a=a
#         self.b=b
    
#     def firstVector(self):
#         print(f'The first component of the is {self.a}')
    
#     def secondVector(self):
#         print(f'The second component of the is {self.b}')
    
# class threeDVector(twoDVector):
#     def __init__(self,c) :
#         super().__init__(10,20)
#         self.c=c
#     def thirdVector(self):
#         print(f'The third component of the is {self.c}')
    
# o=threeDVector(5)
# o.firstVector()
# o.secondVector()
# o.thirdVector()

class twoDvector:
    def __init__(self,i,j) :
        self.i=i
        self.j=j
        
    def show(self):
        print(f'The 2D vector is {self.i}i + {self.j}j + 0k')
class threeDvector(twoDvector):
    def __init__(self,i,j,k) :
        super().__init__(i,j)
        self.k=k
        
    def show(self):
        print(f'The 3D vector is {self.i}i + {self.j}j + {self.k}k')
        
a=twoDvector(1,2)
a.show()
b=threeDvector(3,4,5)
b.show()