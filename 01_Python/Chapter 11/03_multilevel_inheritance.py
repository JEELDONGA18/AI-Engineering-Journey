class Programmer:
    a=1

class Employee(Programmer):
    b=2

class Manager(Employee):
    c=3
    
o=Programmer()
print(o.a) # It prints a
# print(o.b) # It shows an error because b is not in the Employee class.

p=Employee()
print(p.a,p.b)
    
r=Manager()
print(r.a,r.b,r.c)