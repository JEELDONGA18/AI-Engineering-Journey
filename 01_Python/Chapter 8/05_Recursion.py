'''
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1
.
.
.
.
factorial(n) = n x (n-1) x ...  3 x 2 x 1
factorial(n) = n * factorial(n-1)

'''

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

n=int(input('Enter the number : '))
print(f'The factorial of the n is : {factorial(n)}')