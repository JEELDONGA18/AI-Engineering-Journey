# a=int(input('Enter a : '))
# b=int(input('Enter b : '))
# if b==0:
#     raise ZeroDivisionError('Infinte')
# else:
#     c=a/b
#     d=round(c,3)
#     print(f'a/b is {d}')

try:
    a=int(input('Enter a : '))
    b=int(input('Enter b : '))
    c=a/b
    d=round(c,3)
    print(f'a/b is {d}')
except ZeroDivisionError as z:
    print('Infinite')
    