class Employee:
    # def __init__(self,name,salary,increment) :
    #     self.name=name
    #     self.salary=salary
    #     self.increment=increment
    
    salary=1234567
    increment=40
        
    @property
    def SalaryAfterIncrement(self):
        return (self.salary + ((self.salary*self.increment)/100))
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100
        
e=Employee()
# print(e.SalaryAfterIncrement)
e.SalaryAfterIncrement 
print(e.increment)