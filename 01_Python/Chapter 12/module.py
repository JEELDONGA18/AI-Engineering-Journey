# def greet():
#     print('Hello all , Good Morning..')
# greet()
# print(__name__)  # This gives __main__ because,the main file from where someone import the greet function to other file.

def greet():
    print('Hello world!!')

greet()
if (__name__=='__main__'):
    # If this code is directly executed by running the file its present in.
    print('we are directly running this code')
    print(__name__)
    
    