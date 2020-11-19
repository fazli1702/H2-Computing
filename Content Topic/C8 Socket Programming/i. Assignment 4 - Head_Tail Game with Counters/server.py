from head_tail import game
from socket import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

print('Type Ctrl-F6 or close the shell to terminate the server.')

new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))

# game logic
n = 0
c = 0
while True:
    new_socket.sendall(b'I wil toss a coin, guess if it is head (H) or tail (T) :')

    # receving
    client_guess = b''
    while b'\n' not in client_guess:
        client_guess += new_socket.recv(1024)
    client_guess = client_guess.decode().strip() # remove '\n'

    # sending
    new_socket.sendall(game(client_guess).encode() + b'\n')

    if client_guess == 'Q':
        break

new_socket.close()
my_socket.close()
