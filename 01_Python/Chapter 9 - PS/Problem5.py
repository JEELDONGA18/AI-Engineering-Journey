words=['Donkey','Kharab','bad']
with open('Donkey.txt') as f:
    content=f.read()
for word in words:
    content = content.replace(word,'#'*len(word))

with open('Donkey.txt','w') as f:
    f.write(content)