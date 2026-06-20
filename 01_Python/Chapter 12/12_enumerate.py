l=[1,2,4654,2354,365,425,43,2,4325,432]
 
# How to print this list items with index ??

# Way : 1 --> By normal for loop

print('Way 1 : By normal for loop')
index=0 
for item in l:
    print(f'The item number at index {index} is {item}')
    index+=1

# Way : 2 --> By Enumerate function
print('Way 2 : By Enumerate function')
for ind,i in enumerate(l):
    print(f'The item number at index {ind} is {i}')
    