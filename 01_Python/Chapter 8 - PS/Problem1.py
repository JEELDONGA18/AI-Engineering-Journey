def greatest(a,b,c):
    if a>b and a>c:
        print('First number is greatest.')
    elif b>a and b>c:
        print('Second number is greatest.')
    else:
        print('Third number is greatest.')
a=int(input('Enter the first number :  '))
b=int(input('Enter the second number :  '))
c=int(input('Enter the third number :  '))
greatest(a,b,c)

        