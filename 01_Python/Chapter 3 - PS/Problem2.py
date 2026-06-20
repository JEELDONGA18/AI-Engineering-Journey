# NAME=input('Enter the name : ')
# DATE=input('Enter the Date : ')
# MONTH=input('Enter the Month : ')
# YEAR=input('Enter the Year : ')
          
# letter=print( 'Dear '+NAME+
#           '\nYou aare Selected!!\n'+
#           DATE+'/'+MONTH+'/'+YEAR)
# print(f'Dear {NAME}\nYou are Selected!!\n{DATE}/{MONTH}/{YEAR}')

letter='''Dear <|Name|>,
You are Selected!!
<|Date|>'''
print(letter.replace('<|Name|>','Jeel').replace('<|Date|>','21/04/2006'))




