from functools import reduce
ls=[24,5,6,6,4,2,7654,4,6,7,8654,5432,76,4,3,2,143,214,3,513,43,21,4312]

def greater(a,b):
    if a>b:
        return a
    return b

print(reduce(greater,ls))

# print(max(ls))
