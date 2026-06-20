def rem(l,word):
    n=[]
    for item in l:
        if item!=word:
            n.append(item.strip(word))
    return n
        
l=['Jeel','Nil','Dhyey','Yash','Vansh']
print(rem(l,'el'))
