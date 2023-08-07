import random

def play(move):
    print('You:- '+move)
    n=random.randint(1, 3)
    if n==1:
        print('Computer:- rock')
        if move=='paper':
            return "Won"
        elif move=="scessor":
            return "Lost"
        else:
            return "Draw"
    elif n==2:
        print('Computer:- paper')
        if move=='rock':
            return "Lost"
        elif move=="scessor":
            return "Won"
        else:
            return "Draw"
    elif n==3:
        print('Computer:- scessor')
        if move=='paper':
            return "lost"
        elif move=="rock":
            return "Won"
        else:
            return "Draw"
        

print(play('rock'))