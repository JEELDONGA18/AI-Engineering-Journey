class Employee:
    language='Java'
    salary=120000000
    def __init__(self,Name,Salary,Language) : # This is dunder method and this is automatically called during object making.
        self.name= Name
        self.salary= Salary
        self.language= Language
        print('I am creating an object')
    def getInfo(self):
        print(f'The name of the employee is {self.name} ,the language is {self.language} and the salary is {self.salary}.')
    @staticmethod
    def greet():
        print('Good Morning')


Jeel=Employee('Jeel Donga',180000000,'JavaScript')

# print(Jeel.language,Jeel.salary,Jeel.name)
Jeel.getInfo()
Jeel.greet()

# In the output we can see that without calling init method it is called and print the sentance which is in the __init__ method but how and why???
# __init__ method is called as dunder method and this called when we create any object of that class.