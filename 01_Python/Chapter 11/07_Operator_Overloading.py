class Number:
    def __init__(self1,n):
        self1.n=n
    
    def __add__(self1,self2):
        return self1.n + self2.n
    def __sub__(self1,self2):
        return self1.n - self2.n
    def __mul__(self1,self2):
        return self1.n * self2.n
    def __truediv__(self1,self2):
        return self1.n / self2.n
    def __floordiv__(self1,self2):
        return self1.n // self2.n
    
n=Number(1)
m=Number(2)

print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n//m)

class Str:
    def __init__(self1,str) :
        self1.str=str
        
    def __str__(self1) :
        return self1.str
    
    # def __len__(self1):
    #     return self1.__len__
    
s=Str('Jeel')   
print(str(s))
# print(len(s))