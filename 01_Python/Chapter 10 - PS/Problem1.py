# class programmer:
#     def __init__(self,progammer1,progammer2,progammer3,progammer4) :
#         self.Programmer1=progammer1
#         self.Programmer2=progammer2
#         self.Programmer3=progammer3
#         self.Programmer4=progammer4
#         print(f'Programmer 1 is {self.Programmer1}')
#         print(f'Programmer 2 is {self.Programmer2}')
#         print(f'Programmer 3 is {self.Programmer3}')
#         print(f'Programmer 4 is {self.Programmer4}')
    
# Prog=programmer('Jeel','Vansh','Yash','Dhyey')

class programmer:
    company='Microsoft'
    def __init__(self,name,salary,pin) :
        self.name=name
        self.salary=salary
        self.pin=pin
    
j=programmer('Jeel',120000000,394107)
print(j.name,j.salary,j.pin,j.company)
v=programmer('Vansh',120000000,394107)
print(v.name,v.salary,v.pin,v.company)

