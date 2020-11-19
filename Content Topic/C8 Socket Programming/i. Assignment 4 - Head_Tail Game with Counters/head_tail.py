import random

def game(guess):
    if guess == 'H' or guess == 'T':
        if guess == random.choice(['H', 'T']):
            return 'You are right!'
        else:
            return 'Sorry, you are wrong.'

    elif guess == 'Q':
        return 'Thanks for playing the game. Bye!'

    else:
        return 'Please enter head (H), tail (T) or (Q) to quit'


def main():
    while True:
        guess = input('\n\nI will toss a coin, guess if it is a head (H) or tail (T) :').upper()

        if guess == 'Q':
            break

        else:
            print(game(guess))


