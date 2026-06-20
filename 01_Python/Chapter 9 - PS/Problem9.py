with open('This.txt') as f:
    content=f.read()
with open('This-copy.txt') as f:
    Copycontent=f.read()
    
if content==Copycontent:
    print('Yes Both file has same content and matches another.')
else:
    print('No Both file has not same content and not matches another.')

    