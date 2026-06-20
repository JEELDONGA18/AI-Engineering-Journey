class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print('Bhav...Bhav...')
        
d=Dog()
d.bark()