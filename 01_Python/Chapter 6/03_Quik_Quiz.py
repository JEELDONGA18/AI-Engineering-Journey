# Write aprogram to print Yes when the age entered by the iser is greater than or equal to 18.
age=int(input('Enter the age : '))
if(age>=18):
    print('Yes')
elif(age<=0):
    print('Input is invalid.')
else:
    print('No')