class vector:
    def __init__(self,list) :
        self.list=list
    def __str__(self) :
        return f'Vector is ({self.list})'
    
    def __len__(self):
        return len(self.list)
    
v1=vector([1,2,3,4,5,6,7,8,9,0])
print(v1)
print(len(v1))
    