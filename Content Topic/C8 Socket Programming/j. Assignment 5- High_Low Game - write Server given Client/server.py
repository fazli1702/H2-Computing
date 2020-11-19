from socket import *
from high_low import game

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

print('Type Ctrl-F6 or close the shell to terminate the server.')

new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))

n = 0
while True:
    if n == 5:
        new_socket.sendall(b'GAMEOVER\n')
        break
    
    new_socket.sendall(b'GUESS\n')
    
    client_guess = b''
    while b'\n' not in client_guess:
        client_guess += new_socket.recv(1024)
    client_guess = client_guess.decode().strip()
    n += 1

    new_socket.sendall(game(client_guess).encode() + b'\n')

    if game(client_guess) == 'WIN':
        break

    
new_socket.close()
my_socket.close()

    
