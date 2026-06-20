# EVERYTIME we close the file by close function thus we give masal between open and close function but anyone extra way to we do not want to close the file and not remember everytime for closing a file by close function , Yes we can do this by with statement.

f=open('file.txt')
print(f.read())
f.close()

# This can be written by with statement like this : 
with open('file.txt') as f:
    print(f.read())
    
# Thus in this we do not need close the file because the with statement automatically do this.
