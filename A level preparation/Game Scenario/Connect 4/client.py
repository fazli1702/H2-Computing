from socket import *

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))


# client - player 1
# server - player 2 / computer
board = my_socket.recv(1024).decode()
print(board)
while True:
    player1_move = input('Enter column number:')
    my_socket.sendall(player1_move.encode())

    info = my_socket.recv(1024).decode()
    if info == '1WIN':
        board = my_socket.recv(1024).decode()
        print(board)
        print('*' * 30)
        print('You won the game!!!')
        break
    elif info == '2WIN':
        board = my_socket.recv(1024).decode()
        print(board)
        print('*' * 30)
        print('Computer won the game, you loss :(')
        break
    else:
        print(info)
    
    




my_socket.close()
