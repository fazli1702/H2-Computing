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
   

from socket import socket

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()



player = [4, 5]
x, y = 4, 5
while [x, y] == [4, 5]:
    x = randint(0, 9)
    y = randint(0, 10)
prize = [x, y]

counter = 0
while True:
    table = grid(prize, player)
    new_socket.sendall(table.encode())

    # user input
    move = new_socket.recv(1024).decode()

    if move == 'Q':
        msg = 'You have ended the game'
        new_socket.sendall(msg.encode())
        print(msg)
        break

    else:
        next_position = user(player, move)
        counter += 1

        if next_position == prize:
            msg = f'You got the prize in {counter} steps!'
            new_socket.sendall(msg.encode())
            break
        else:
            player = next_position
    


new_socket.close()
my_socket.close()



