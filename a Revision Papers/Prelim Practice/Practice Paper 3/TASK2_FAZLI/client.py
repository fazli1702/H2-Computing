from socket import *

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))

while True:
    choice = input('Enter guess (A-Z):').upper()
    my_socket.sendall(choice.encode())

    data = my_socket.recv(1024).decode()
    if data == 'WIN':
        print('You win!')
        break

    elif data == '>':
        print('The answer is before your guess.')

    else:
        print('The answer is after your guess.')



my_socket.close()
