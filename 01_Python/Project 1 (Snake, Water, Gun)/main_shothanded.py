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
while True:
    computer = random.choice([1,2,3])
    you = int(input('Enter your choice : '))
    if you>=1 and you<=3:
        youDict={ 's':1 , 'p':2, 'sc':3}

        displayDict={1:'Stone',2:'Paper',3:'Scissors'}

        print(f'You choose {displayDict[you]}\nComputer choose {displayDict[computer]}')

        if computer==you:
            print('The game is draw!!')
        else:
            # if computer==1 and you==2:   #(computer - you) = -1
            #     print('You win!!')
            # elif computer==1 and you==3: #(computer - you) = -2
            #     print('You lose!!')
            # elif computer==2 and you==1: #(computer - you) = 1
            #     print('You lose!!')
            # elif computer==2 and you==3: #(computer - you) = -1
            #     print('You win!!')
            # elif computer==3 and you==1: #(computer - you) = 2
            #     print('You win!!')
            # elif computer==3 and you==2: #(computer - you) = 1
            #     print('You lose!!')
            
            # The below logic is set by computer - you 
            # If user win so (computer - you) is -1 or 2
            # If computer win or you lose so (computer - you) is 1 or -2
            if (computer-you)==-1 or (computer-you)==2:
                print('You win!!')
            else:
                print('You lose!!')
    else:
        print('Invalid input')
