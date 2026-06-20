myList = [6,3,9,8,2]

# How to print this list's items to make square and make new list as squaredList ??

# Way : 1 --> By normal for loop

print('Way 1 : By normal for loop')
squaredList=[]
for i in myList:
    squaredList.append(i*i)
print(squaredList)


# Way : 2 --> By for loop with some iteration

print('Way 2 : By for loop with some iteration')
squaredList=[i*i for i in myList]  # (iteration) (for loop)
print(squaredList)