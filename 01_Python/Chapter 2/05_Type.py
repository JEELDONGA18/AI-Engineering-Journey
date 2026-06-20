a=31
t1=type(a)
print(t1)

b=12.3
t2=type(b)
print(t2)

c='Jeel'
t3=type(c)
print(t3)


# Type conversion ---> For this we can use int(), float() and str() functions

# String to Integer
d='31'
print(type(d))
e=int(d)
print(type(e))

# String to Integer
# d='Jeel'  #This is not valid because string contains name and it is not convert into Integer and it will generate error.
# print(type(d))
# e=int(d)
# print(type(e))

# String to Float
d='31.2'
print(type(d))
e=float(d)
print(type(e))

# String to Float
# d='Jeel'  #This is not valid because string contains name and it is not convert into float and it will generate error.
# print(type(d))
# e=float(d)
# print(type(e))


# Integer to String
d=31
print(type(d))
e=str(d)
print(type(e))

# Integer to float
d=31
print(type(d))
e=float(d)
print(type(e))


# float to String
d=31.234
print(type(d))
e=str(d)
print(type(e))

# float to int
d=31.234
print(type(d))
e=int(d)
print(type(e))
