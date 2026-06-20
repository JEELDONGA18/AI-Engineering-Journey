with open('Donkey.txt') as f:
    content=f.read()

newContent = content.replace('Donkey','######')

with open('Donkey.txt','w') as f:
    f.write(newContent)