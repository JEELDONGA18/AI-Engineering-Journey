from functools import reduce

# Map fuction Example :

l=[1,2,3,4,5,6,7]
square= lambda x:x*x
SquaredList=map(square,l)
print(list(SquaredList))

# Filter function Example : 
l=[1,2,3,4,5,6,7]
def even(n):
    if (n%2==0):
        return True
    return False

OnlyEven=filter(even,l)
print(list(OnlyEven))

# Reduce function example :

l=[1,2,3,4,5,6,7,8]
def sum(a,b):
    return a+b

mul=lambda a,b:a*b
 
print(reduce(sum,l))
print(reduce(mul,l))