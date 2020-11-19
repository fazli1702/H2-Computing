from socket import *

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))


ins = my_socket.recv(1024).decode()
print(ins)
print('You are player 2')

# main game loop
for i in range(3):
    # display player 1 move / board
    info = my_socket.recv(1024).decode()
    if info == '1WIN':
        board = my_socket.recv(1024).decode()
        print(board)

        print('Player 1 has won the game')
        break
    
    board = my_socket.recv(1024).decode()


    # player 2 input move
    x = input('Enter x coordinate: ').encode()
    y = input('Enter y coordinate: ').encode()
    x -= 1
    y -= 1

    my_socket.sendall(x)
    my_socket.sendall(y)

    # display player 2 move / board
    info = my_socket.recv(1024).decode()
    if info == '2WIN':
        board = my_socket.recv(1024).decode()
        print(board)
        print('Player 2 has won the game')
        break
    



my_socket.close()
