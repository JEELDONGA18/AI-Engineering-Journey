class attribute:
    a=123
attr=attribute()
print(attr.a) #Prints the class attribute because instance attribute is not present.
attr.a=0  #Instance attribute is set
print(attr.a)  #Prints the Instance attribute because instance attribute is not present.
print(attribute.a) # Prints the class attribute.    

# ANSWER : NO , the class attribute is not change and the instance attribute is set and we can say that it is the copy of the class attribute and object also prepare this.