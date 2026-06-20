class Calculator:
    def __init__(self,number) :
        self.number=number
    def Square(self):
        print(f'The square of the number is {self.number*self.number}')
    def Cube(self):
        print(f'The cube of the number is {self.number*self.number*self.number}')
    def Squareroot(self):
        print(f'The squareroot of the number is {self.number**(1/2)}')
    @staticmethod
    def greet():
        print('Hello!!')
        
n=int(input('Enter the number : '))
Calc=Calculator(n)
Calc.Square()
Calc.Cube()
Calc.Squareroot()
Calc.greet()