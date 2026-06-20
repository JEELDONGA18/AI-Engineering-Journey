# Advanced type hints : 
from typing import List, Tuple, Dict, Union

n=5
# If n is an integer then I want to get all the methods of the integer.
# so I can mark the variable as an integer like this,
n : int = 5
# now I simply right 'n.' and all the suggestions give me the methods of the integer.

name : str = 'Hanuman dada'

def sum(a:int , b: int) -> int:
    return a+b

print(sum(3,5))

# So , this Type is not required but generally some other user or many times us may help for checking the type of the variables for giving that type of the value by the computer .



# List of the integers : 
numbers : List[int] = [1,2,3,4,5]

# Tuple of strings and integers : 
person : Tuple[str, int] = ('Krishna bhagwan','8')

# Dictonary with string keys and integer values : 
scores : Dict[str:int] = {'Hanuman dada':'4','Krishna bhagwan':'4','Swaminarayan bhagwan':'3'}

# Union type for variables that can hold multiple types : 
idetifier : Union[int,str] =  'Jeel123'
identifier = 12345 # Also valid
