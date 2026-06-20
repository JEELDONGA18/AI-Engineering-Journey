# persist :  means save the variablic data into perticular file.
# volatile : variablic(RAM) means temperaroly data stored.
# non-volatile : non variablic(HDD) means permenetly data stored.

'''
a='A very long string with mails..'

emails=[]

3 seconds
'''

f=open('file.txt','r') # by defualt mode of open function is read so we can or not write 'r'.
# data=f.read()
# print(data)
print(f.read()) 
f.close # This is must important and most recomended and this is a good practice and this is use for the say that to computer we have done our work in our file and now we close it.