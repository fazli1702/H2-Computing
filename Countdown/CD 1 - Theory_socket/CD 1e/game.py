import random
import string

letters = string.ascii_uppercase

def main():
    correct = 0
    for i in range(3):
        n = random.randint(1, 10)  # number of letters
        letter_i = random.randint(0, len(letters)-1) 
        rect = [['.' for j in range(10)] for j in range(5)] # init empty rect
        coordinates = []
        for k in range(n):  # add letters
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 4)
                coord = (x, y)
                if coord not in coordinates:  # ensure not repeated coordinate
                    rect[y][x] = letters[letter_i]
                    break
        # display rect
        for row in rect:
            string = ''
            for ele in row:
                string += ele
            print(string)

        # player input
        player_input = int(input('Enter number of letters:'))
        if player_input == n:
            correct += 1

    print('Number of correct answer is', correct)





        
