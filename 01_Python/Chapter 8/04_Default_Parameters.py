def greet(name,ending='Thank you'):
    print(f'GOOD DAY {name}!!!')
    print(ending)
# name=input('Enter your name : ')
# greet(name)

greet('Jeel','Thanks')
greet('Yash') # here the second argument of the greet function is missing but we take by default 'Thank you' means ending so it take thank you and this ending is called as default paramerter and argument or parameter.

# So we can say that, when we give perticular argument if we set default argument so it default argument is override and cosider as new argument and when we give not any argument then it will take default argument.