# class method is the way by which we can access the class in the method.
class Employee:
    a=1
    # we can declare show method as class method by decorator.
    @classmethod
    def show(cls):
        # and do self as cls
        print(f'the value of the class attribute is : {cls.a}')

E=Employee()
E.a=123
E.show()  # In the output It shows a's value 123(Instance attribute) but If I want to see 1 (Class attribute) so how can I do??