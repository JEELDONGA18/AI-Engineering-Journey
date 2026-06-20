try:
    a=int(input('Enter the number : '))
    print(a)

except ValueError as v: # You know which error raise and thus you print that perticular error.
    print('Heyy!! this is a value error.')
    print(v)

except Exception as e: # by default error printing
    print('You must enter number not string or floting point number or boolean.')
    print(e) 
    
print('Thank you..')