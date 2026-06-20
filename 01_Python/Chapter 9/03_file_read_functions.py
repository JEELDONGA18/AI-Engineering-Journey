f=open('file.txt')
# list=f.readlines()      # This readlines() function works like it read all the lines and put elemnt as list element and make a list for all content.
# print(list,type(list))  

# line=f.readline()
# print(line,type(line))

# line1=f.readline()
# print(line1,type(line1))
# line2=f.readline()
# print(line2,type(line2))
# line3=f.readline()
# print(line3,type(line3))
# line4=f.readline()
# print(line4,type(line4))
# line5=f.readline()
# print(line5,type(line5))
# line6=f.readline()
# # print(line6,type(line6))
# print(line6=='')

line=f.readline()
while line != '':
    print(line)
    line=f.readline() # This line is important for the terminate the while loop otherwise it will become an infinte while loop.
f.close()