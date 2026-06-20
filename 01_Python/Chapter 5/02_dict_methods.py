a={
    'Keys':'Values',
    'Jeel':100,
    'Vansh':99,
    'Yash':[1,2,4,5,6,7,8,9],
    0.124:'Vishal',
    True: 'NIL'
}

print(a.items()) #--> It will return values in tuple-list format.   
print(a.keys())
print(a.values())

a.update({'Vansh':100,'Dhyey':95}) #--> So this will update value of perticular key which is present in the dictionary and If key is not present in the dictionary so It will add in the dictionary.

print(a)

print(a.get('Jeel')) #If the key is not present in the dictionary so It prints None.
print(a['Jeel'])     #If the key is not present in the dictionary so It will return value error.


print(a.pop(0.124)) #--> It will remove the value of the key from the dictionary.
print(a.popitem())  #--> It will remove the key value from the last of the dictionary.
print(a)