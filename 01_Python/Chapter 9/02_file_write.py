str='This is a content means string for the new file.'
f=open('myfile.txt','w') # Here, in open function we mension filename and also type of the file which is reading('r') or writing('w').
f.write(str)
f.close()