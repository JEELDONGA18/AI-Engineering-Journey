a=int(input('Enter the number : '))
b=0
for i in range(2,a):
    if a%i==0:
        b=1
if b==1:
    print('Given number is not prime')
else:
    print('Given number is prime.')
    