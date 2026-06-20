# Using walrus operator
if (n:= len([1,2,3,4,5])) > 3:
    print(f'List is too long ({n} elements, expected <= 3)')

# Here this operator works like n=length of the list and this will also check the condition is true or not.
#  ------- OR --------  

list=[1,2,3,4,5]
n=len(list)
if n>3:
    print(f'List is too long ({n} elements, expected <= 3)')