from socket import *

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))

while True:
    data = my_socket.recv(1024)

    # sending
    guess = input(data.decode()).upper()
    my_socket.sendall(guess.encode() + b'\n')

    # receiving
    data = b''
    while b'\n' not in data:
        data += my_socket.recv(1024)
    print(data.decode())

    if guess == 'Q':
        break

my_socket.close()
