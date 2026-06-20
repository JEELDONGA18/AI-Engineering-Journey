a=(1,3,4,5,5,6,3,4321.43,2,3251,23232,3,2,3,23,3,546.32,323)
print(a)
print(type(a))

no=a.count(3)  #--> It counts how many times value repeat in the tuple
print(no)
# or print(a.count(3))

ind=a.index(4321.43) #--> It returns given value's index where it occure first time.
print(ind)  

print(len(a))

#Slicing concept is same as String and list.

# ----UNIQUE METHODS OF THE TUPPLE----
# Repeatation
b=(1,4,5,6)
print(b*3)

print(1 in b)

print(min(b))
print(max(b))

# d, e, f=b

# print(d)
# print(e)
# print(f)
