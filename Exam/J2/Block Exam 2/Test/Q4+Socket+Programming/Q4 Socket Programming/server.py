# copy the necessary program code
# from maze.py and paste it here:
from random import randint

def user(position, direction):
    if direction == 'U':
        return [position[0], position[1]-1]
    elif direction == 'D':
        return [position[0], position[1]+1]
    elif direction == 'L':
        return [position[0]-1, position[1]]
    elif direction == 'R':
        return [position[0]+1, position[1]]
    else:
        return position
   
def grid(p,o):
    string = ''
    for row in range(11):
        for i in range(10):
            if [i,row] == p:
                string += 'P'     #prize
            elif [i,row] == o:
                string += 'O'     #player
            else:
                string += '.'
        string += '\n'
    return string    
   


def main():

    player = [4, 5]

    x, y = 4,5
    while [x,y] == [4,5]:   
        x = randint(0,9)    #prize must not be [4,5]
        y = randint(0,10)
    prize = [x,y]

    print(grid(prize,player))

    counter = 0

    while True:
        move = input('Enter U(p), D(own), L(eft), R(ight) or Q(uit) : ').upper()

        if move == 'Q':
            print('You have ended the game.')
            break
        else:
            next_position = user(player, move)
            counter += 1
            if next_position==prize:
                print('You got the Prize in '+str(counter)+' steps!')
                break
            else:
                player = next_position
                print(grid(prize,player))












from socket import socket

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

print('Type Ctrl-C or close the shell to terminate game.')
new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))


player = [4, 5]

x, y = 4,5
while [x,y] == [4,5]:   
    x = randint(0,9)    #prize must not be [4,5]
    y = randint(0,10)
prize = [x,y]

counter = 0
while True:
    # Write your code here:
    # print board/grid at start/after my move
    board = grid(prize, player)
    print(board)
    board.encode()
    new_socket.sendall(board)

    # oppponent move
    op_move = new_socket.recv(1024).decode()

    if op_move == 'Q':
        print('Your opponent ended the game!')
        break
    else:
        next_position = user(player, move)
        counter += 1

        if next_position == prize:
            win = 'You got the Prize in '+str(counter)+' steps!'
            new_socket.sendall(win)
            break
        else:
            player = next_position

    # print board/grid after opponenet move
    board = grid(prize, player)
    print(board)
    board.encode()
    new_socket.sendall(board)

        
    # my move    
    move = input('Enter U(p), D(own), L(eft), R(ight) or Q(uit) : ').upper()

    if move == 'Q':
        print('You have ended the game!')
        new_socket.sendall(move.encode())
        break
    
    else:
        next_position = user(player, move)
        counter += 1

        if next_position == prize:
            win = 'You got the Prize in '+str(counter)+' steps!'
            new_socket.sendall(win)
            break
        else:
            player = next_position
    


    

    
new_socket.close()
my_socket.close()
