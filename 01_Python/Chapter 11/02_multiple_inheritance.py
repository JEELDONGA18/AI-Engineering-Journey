class Employee:
    company = 'Google'
    name='Default name'
    def show(self):
        print(f'The name of the employee is {self.name} and the company of the employee is {self.company}')

# class Programmer:
#     def show(self):
#         print(f'The name of the employee is {self.name} and the salary of the employee is {self.salary}')
#     def showlanguage(self):
#         print(f'The name of the employee is {self.name} and he is comfortable with {self.language} language.')
class Coder:
    language='C++'
    def showLanguage(self):
        print(f'The company\'s all the employees are comfortable with the {self.language}')
        
class Programmer(Employee,Coder):
    company=('You Tube')
    language='Python'
    def showlanguage(self):
        print(f'The name of the employee is {self.name} and he is comfortable with {self.language} language.')

a=Employee()
b=Coder()
c=Programmer()
# b.language='Java'
a.show()
b.showLanguage()
c.showlanguage()
# print(a.company, b.company)
    
        