a=int(input('Enter the first number : '))
b=int(input('Enter the second number : '))

if (b==0):
    raise ZeroDivisionError('Hey you divide some numbers with 0 and this is not fair.')
else:
    print(f'The division of the first and second number is : {a/b}')

# This error raising crash the program(means after this error showing program will not excicute)
# It is like this, we not hit small kid but small kid not behave well then we hit it and give lesson to him or her or it.