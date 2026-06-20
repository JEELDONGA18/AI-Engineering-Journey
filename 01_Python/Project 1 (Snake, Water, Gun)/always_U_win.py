import random
'''
 1 for Stone 
 2 for Paper 
 3 for Scissors
'''
print('Welcome!! This is a Stone , Paper ,Scissors Game')
print('By entering your choice you can play.')
print('1 for Stone')
print('2 for Paper')
print('3 for Scissors')

n=1
m=int(input('Enter how many times you want to win : '))

while n<=m:
    computer = random.choice([1,2,3])
    # you = int(input('Enter your choice : '))
    you = computer%3+1
    if you>=1 and you<=3:
        youDict={ 's':1 , 'p':2, 'sc':3}

        displayDict={1:'Stone',2:'Paper',3:'Scissors'}

        print(f'You choose {displayDict[you]}\nComputer choose {displayDict[computer]}')

        if computer==you:
            print('The game is draw!!')
        else:
            if computer==1 and you==2:
                print('You win!!')
            elif computer==1 and you==3:
                print('You lose!!')
            elif computer==2 and you==1:
                print('You lose!!')
            elif computer==2 and you==3:
                print('You win!!')
            elif computer==3 and you==1:
                print('You win!!')
            elif computer==3 and you==2:
                print('You lose!!')
    else:
        print('Invalid input')
    n+=1
