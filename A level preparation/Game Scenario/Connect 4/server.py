from socket import *
from connect4 import *
from random import randint

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print(f'Connected to {addr}')

# client - player 1
# server - player 2 / computer
board = Board()
new_socket.sendall(board.to_string().encode())
while True:
    # player 1 turn
    player1_move = int(new_socket.recv(1024).decode())
    board.drop_token(player1_move, 1)

    if board.win(1):
        win = '1WIN'
        new_socket.sendall(win.encode())
        new_socket.sendall(board.to_string().encode())
        break

    # player 2 turn
    board.drop_random()
    new_socket.sendall(board.to_string().encode())

    if board.win(2):
        win = '2WIN'
        new_socket.sendall(board.to_string().encode())
        new_socket.sendall(win.encode())
        break
    

    
    


my_socket.close()
new_socket.close()
    
