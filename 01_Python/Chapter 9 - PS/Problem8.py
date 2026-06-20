with open('This.txt') as f:
    content=f.read()
with open('This-copy.txt','w') as f:
    newContent=f.write(content)