from socket import socket

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))

while True:
    # Receive data from the server
    data = my_socket.recv(1024).decode()
    print(data)

    if data == 'You have ended the game' or 'You got the prize in' in data:
        break

    # prompt user for input
    move = input('Enter U(p), D(own), L(eft), R(ight) or Q(uit) : ').upper()
    my_socket.sendall(move.encode())
    
my_socket.close()
