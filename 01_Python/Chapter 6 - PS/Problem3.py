p1='Make a lot of money.'
p2='Buy now.'
p3='Subscribe this.'
p4='Click this.'

a=input('Enter you text : ')

if (p1 in a) or (p2 in a) or (p3 in a) or (p4 in a) :
    print('This comment is spam.')
else:
    print('This comment is not a spam.')