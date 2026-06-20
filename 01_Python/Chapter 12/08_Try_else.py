# In the C,C++,JavaScript for exception handeling there is a try and catch block is there.
# But in the python there is an try catch block for the exceptional handeling.

try:
    a=int(input('Enter the number : '))
    print(a)

except Exception as e: 
    print('You must enter number not string or floting point number or boolean.')
    print(e) 

else:
    print('I am inside else.')
    print('I am excicute because of the try')
    # so when try is run successfully then else will run otherwise except will run.
    
print('Thank you..')