l=[1,2,3,4,5,6,7,8,9,10]
n=int(input('Enter the table number : '))

Table=[n*i for i in l]
with open('Tables.txt','a') as f:
    f.write(f'Table of {n} is : {str(Table)} \n')