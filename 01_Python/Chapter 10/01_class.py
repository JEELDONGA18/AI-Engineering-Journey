class Employee:    
    name=input('Enter your name : ')
    salary=120000000
    language='Java'

employee = Employee()
print(employee.name,employee.salary,employee.language)
# Here name ,employee and salary is the class attributes but if I write in main --> employee.name='Yash dilkhush ' then it will called as object attributes
# so Class attributes are they which are directly belongs to class but object attributes are they which are override after usage of the object.
# like this
class Employee:    
    salary=120000000 # This is a class attribute.
    language='Java'  # This is a class attribute.

employee = Employee()
employee.name =  'Yash Dilkhush' # This is an object attribute or  instance attribute.
# here this name attribute is created by object so it is called as object attributes or instance attributes.
# instance attribute is that attributes which is created at perticular instances means in our example if we creates name attribute and we define perticular name so in every object access that name is show ,if that is other's application so at object making we can define new name attribute and give name to it.
print(employee.name,employee.salary,employee.language)
