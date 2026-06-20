with open('file for rename.txt') as f:
    content=f.read()
with open('remoced_by_python.txt','w') as f:
    newContent=f.write(content)
del('file for rename.txt')