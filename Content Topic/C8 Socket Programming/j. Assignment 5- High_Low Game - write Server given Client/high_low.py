from random import *

num = randint(1, 100)

def game(guess):
    if guess.isdigit():
        if int(guess) == num:
            return 'WIN'
        elif int(guess) > num:
            return 'HIGH'
        else:
            return 'LOW'
    else:
        return 'Please enter number 1 to 100'


def main():
    counter = 5
    while counter > 0:
        guess = input('Guess a number 1 to 100: ')
        if game(guess) == 'WIN':
            print(game(guess))
            break
        else:
            print(game(guess))
        counter -= 1

    if counter == 0:
        print('You ran out of tries! Game over.')



