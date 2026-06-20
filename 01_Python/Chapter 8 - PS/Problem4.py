def sum_of_first_n(n):
    if n==1:
        return n
    return n+sum_of_first_n(n-1)
n=int(input('Enter the number :  '))
print(f'the sum of the first n natural number is : {sum_of_first_n(n)}')

