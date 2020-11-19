from random import *

def game(opponent):
    d = {'1':'Scissor', '2':'Paper', '3':'Stone'}
    player2 = input('Enter (1) Scissor (2) Paper or (3) Stone: ')
    player2 = d[player2]
##    print('Player1:', opponent)
##    print('Player2:', player2)

    if player2 == opponent:
        return 'Draw,' + str(opponent) + ',' + str(player2)

    elif (player2 == 'Scissor' and opponent == 'Paper') \
         or (player2 == 'Paper' and opponent == 'Stone') \
         or (player2 == 'Stone' and opponent == 'Scissor'):
        return 'Player2 wins!,' + str(opponent) + ',' + str(player2)

    else:
        return 'Player1 win!,' +  str(opponent) + ',' + str(player2)


def main():
    print('You are Player1 playing against Player2')
    
    counter = 3
    d = {'1':'Scissor', '2':'Paper', '3':'Stone'}
    while counter > 0:
        player1 = input('Enter (1) Scissor (2) Paper or (3) Stone: ')

        if player1 in d:
            print('Player1:', d[player1])
            print(game(d[player1]))
            counter -= 1

        else:
            print('Please enter only 1, 2 or 3.')


