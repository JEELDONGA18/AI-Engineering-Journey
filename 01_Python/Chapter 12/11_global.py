a=89  # Global variable : That variable which can access at anywhere in the file.

def fun():
    global a
    a=3 # Local variable : That variable which can access at only between perticular function.  
    print(a)

fun()   
print(a)

# fun()     # Output : 3
# print(a)  # Output : 3


# print(a)  # Output : 89
# fun()     # Output : 3

# so the logic is if in the function if we made golabal variable(here, global a) so the function always returns its golabal value but if the any gloabal variable which is outside the function, so if it is upper side of the fun() so it will print its older value(here,89) and if that is under the fun() then it will return gloabal variables new value(here, 3) means \
    
# after  ,then new value and before , then old value.
