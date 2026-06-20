a=int(input('First Person : Enter the number : '))
b=int(input('Second Person : Enter the number : '))
c=int(input('Third Person : Enter the number : '))
d=int(input('Fourth Person : Enter the number : '))

if (a>b and a>c and a>d):
    print('First person\'s number is greater.')
elif (b>a and b>c and b>d):
    print('Second person\'s number is greater.')
elif (c>a and c>b and c>d):
    print('Third person\'s number is greater.')
elif (d>a and d>b and d>c):
    print('Fourth person\'s number is greater.')
else:
    print('any two,three or four person\'s number is equal.')