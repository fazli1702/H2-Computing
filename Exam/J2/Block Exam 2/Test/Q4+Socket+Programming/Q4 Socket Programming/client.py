from socket import socket

my_socket = socket()

my_socket.connect(('127.0.0.1', 12345))

while True:
    #Receive data from the Server
    board = my_socket.recv(1024).decode()
    #Print the data
    print(board)
    
    #Write the code to prompt the user to input the move direction
    move = input('Enter U(p), D(own), L(eft), R(ight) or Q(uit) : ').upper()

    # my move
    if move == 'Q':
        my_socket.sendall(move.encode())
        print('You have ended the game!')
        break
    else:
        print(my_socket.recv(1024).decode())

    # print board/grid after my move
    board = my_socket.recv(1024).decode()
    print(board)

        
    # opponenet move
    op_move = my_socket.recv(1024).decode()
    if op_move == 'Q':
        print('Your opponent ended the game!')
        break

    else:
        pass






        

my_socket.close()
