m1=int(input('Enter the marks of the subject-1 : '))
m2=int(input('Enter the marks of the subject-2 : '))
m3=int(input('Enter the marks of the subject-3 : '))
m=(m1+m2+m3)*100/300
if m1>=33 and m2>=33 and m3>=33:
    if m>40:
        print('Congratulations!! Student is PASS.',m)
    else:
        print('Sorry!! You have not sufficient marks.',m)
else:
    print('You have not sufficient marks in the your subject.')

