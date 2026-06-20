class Employee:
    language='Java'
    salary=120000000
    def getInfo(self):
        print(f'The language is {self.language} and the salary is {self.salary}.')
    @staticmethod
    def greet():
        print('Good Morning')
        
    # Here we pass whole object in the greet method and this method is not take any other varibale so ideally whole object passing is not suitable so we can make it STATIC METHOD and declare that it have not any requirement of the object 
Jeel=Employee()
# Jeel.language='C++'
# Jeel.salary=20000000
print(Jeel.language,Jeel.salary)

Jeel.getInfo()
Jeel.greet()
# Employee.getInfo(Jeel)
# This is taken as : Emplyoee.getInfo(Jeel)  means Class.method(Object) and this is alternate of Jeel.getInfo()

# So the story is that if we give not any argument during the calling the function by object so it will automatically take one argument and this argument is generally self(You can take any name)and by this in the function all the variables access by self.variable and this variable's value  is given by us in to function. AND self argument is by default given means we always give self parameter give to function which is in the class.
