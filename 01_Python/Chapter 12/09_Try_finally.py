# try:
#     a=int(input('Enter the number : '))
#     print(a)

# except Exception as e: 
#     print('You must enter number not string or floting point number or boolean.')
#     print(e) 

# finally:
#     print('Hey! I am inside the finally.')

# print('Thank you..')
    
# In this case finally is run in any how means even try or except is running
# so we can write finally block insted of like this 
# finally:
#     print('Hey! I am inside the finally.')
    # to
    
#     print('Hey! I am inside the finally.')  # means without finally

# and yes, you can you write like this and answer will be same but twist is there in the function you must write it so finally is runing even try or except is running.


def hello():
    try:
        a=int(input('Enter the number : '))
        print(a)
        return

    except Exception as e: 
        print('You must enter number not string or floting point number or boolean.')
        print(e) 
        return

    finally:
        print('Hey! I am inside the finally.')
    
    
hello()