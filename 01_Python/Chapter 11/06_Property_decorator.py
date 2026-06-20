class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f'the value of the class attribute is : {cls.a}')
    
    @property
    def name(self):
        # return self.Name
        return f'{self.FName} {self.LName}'
    # This property means that fill the user that it use the E.name='Value value' and prints that value with this show line no. 17

    @name.setter
    def name(self,value):
        self.FName=value.split(' ')[0]
        self.LName=value.split(' ')[1]
    # also do this which set first entered string as first name and last endtered string as last name and this part is user can not see.
    
    # ABSTRACTION : We hide the implementation details like we hide @name.setter property from the user, by this we split the name into first name and last name but user can not see this.
    
    # ENCAPSULATION : The lots of working units, we packed them into one perticular unit and in our case it is the class.
        
    # def nameSpliter(self,value):
    #     self.FName=value.split(' ')[0]
    #     self.LName=value.split(' ')[1]
    #     print(f'{self.FName} {self.LName}')
        
         
    #  Here what happens??
    # In this we do not set name named instance attribute at out of the class but we creates one type of the instance attribute which is made from existing instance attribute(E.name='Jeel Donga').
E=Employee()
E.a=123

E.name='Jeel Donga'
print(E.name)  # It prints the E.name as Jeel
# print(E.FName,E.LName)  # Same output as E.name 

# If my name is Jeel Donga and If I want to make my name's two instance attribute like firstname and lastname so how can I do?
# E.nameSpliter(E.name)
E.show()