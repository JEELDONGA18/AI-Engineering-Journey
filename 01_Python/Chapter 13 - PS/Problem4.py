ls=[1,3,5,432,64,542,54,32,554,25,4,25,4,255]

def divide_by_5(n):
    if (n%5==0):
        return True
    return False

divdBy5=list(filter(divide_by_5,ls))
print(divdBy5)