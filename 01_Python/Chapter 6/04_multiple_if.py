a=int(input('Enter the age : '))
# Stating of the first if statement.
if(a%2==0):
    print('a is even.')
# Ending of the first if statement.

# Stating of the second if statement.
if a>=18:
    print('You are adult.')
elif(a<0):
    print('This is Invalid input.')    
elif(a==0):
    print('This is Invalid input because noone has 0 year.')    
else:
    print('You are becoming an adult.')
# Ending of the second if statement.

print('Ending of the program.')