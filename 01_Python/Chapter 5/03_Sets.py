S=set() #Empty set declaration.

s={13,4,6,7,8,9.0,7,5,3,2,56,8,9,10}
print(s)

# why set is use?  --> Set is used for the making non repeating collection of the values.
# You can not access elements of the set by it's index.


s.add(566)
print(s,type(s))
s.remove(566)
print(s,type(s))
s.pop() #it removes random element. 
print(s,type(s))
s.clear()
print(s,type(s))
