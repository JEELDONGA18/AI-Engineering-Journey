list=[1,2,3,4,5,5,6,7,7,8,9,9]

for i,item in enumerate(list):
    if i==2 or i==4 or i==6:
        print(f'The value of {i+1}th element is : {item}')