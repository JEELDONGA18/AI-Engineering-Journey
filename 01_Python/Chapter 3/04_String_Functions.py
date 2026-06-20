name='jeel'

print(len(name))
print(name.endswith('l'))
print(name.startswith('j'))
print(name.capitalize()) # --> If our string's first letter is small character so it will converts string's first letter as capital letter.

#--> one most imoportant thing is if my string is 'hello jeel' so it will not capitalize both first letter of string's words like 'Hello Jeel' it will only convert 'Hello jeel'.

# If you want to capatilize all first letter of the string's word so you can use title function.(title())
name2='Hanumanji kem chho??'
print(name2.title())
print(name2.upper())
print(name2.lower())

name3='   Hanumanji   '
print(name3.strip())  #--> It will remove space form the both side of the string.
print(name3.lstrip()) #--> It will remove space form the left side of the string.
print(name3.rstrip()) #--> It will remove space form the right side of the string.

name4='Happy Janmashtami'
print(name4.count('a'))    # -->It counts how many times a is occur in given string.
print(name4.find('Happy')) # -->It will return at which index number Happy word first time occur. 
print(name4.replace('Happy')) # -->It will return at which index number Happy word first time occur.

#--> Most important thing about replace function is it replace all the words which we want to replace like, string='Bad Bad Boy' If I replace Bad to Good so after replace string is ='Good Good Boy'



  