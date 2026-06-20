# def pattern(n):
#     for i in range(n,0,-1):
#         for j in range(1,i+1):
#             print('* ',end='')
#         print()
# n=int(input('Enter the number : '))
# pattern(n)

def pattern(n):
    if n==0:
        return  # Here return statement is work as after this statement the pattern exicution will stop.
    print('*'*n)
    pattern(n-1)
    
n=int(input('Enter the number : '))
pattern(n)