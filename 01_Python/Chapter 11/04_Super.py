class Programmer:
    def __init__(self):
        print('The constructor of Programmer')
    a=1

class Employee(Programmer):
    def __init__(self):
        print('The constructor of Employee')
    b=2

class Manager(Employee):
    def __init__(self):
        # If I want to access the constructor of the parent of this class.
        super().__init__()
        print('The constructor of Manager')
    c=3
    
o=Programmer()
print(o.a) 

p=Employee()
print(p.a,p.b)
    
r=Manager()
print(r.a,r.b,r.c)