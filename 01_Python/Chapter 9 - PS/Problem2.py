import random

def game():
    print('You are playing the game..')
    score=random.randint(1,100)
    # Displaying your score
    print(f'Your score is {score}')
    
    # Hi score importing
    with open('Hiscore.txt') as f:
        hiscore=f.read()
        if hiscore!='':
            hiscore=int(hiscore)
        else:
            hiscore=0
    
    # compairing hiscore and score
    if score>hiscore:
        with open('Hiscore.txt','w') as f:
            f.write(str(score))

    
# Using game() function:
game()
    