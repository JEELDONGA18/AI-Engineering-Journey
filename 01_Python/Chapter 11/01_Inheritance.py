class Employee:
    company = 'Google'
    def show(self):
        print(f'The name of the employee is {self.name} and the salary of the employee is {self.salary}')

# class Programmer:
#     def show(self):
#         print(f'The name of the employee is {self.name} and the salary of the employee is {self.salary}')
#     def showlanguage(self):
#         print(f'The name of the employee is {self.name} and he is comfortable with {self.language} language.')

class Programmer(Employee):
    company=('You Tube')
    def showlanguage(self):
        print(f'The name of the employee is {self.name} and he is comfortable with {self.language} language.')

a=Employee()
b=Programmer()
a.name='Jeel'
a.salary=2000000000
print(a.show())
print(a.company, b.company)
    
        