from socket import *
from scissor_paper_stone import game

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

print('Press Ctrl-F6 or close shell to terminate shell')

new_socket, addr = my_socket.accept()
print('Connected to', addr)

counter = 3
d = {'1':'Scissor', '2':'Paper', '3':'Stone'}
print('You are player 2')
while True:
    new_socket.sendall(b'Enter (1) Scissor (2) Paper or (3) Stone: ')

    # receiving
    client_choice = b''
    while b'\n' not in client_choice:
        client_choice += new_socket.recv(1024)
    client_choice = client_choice.decode().strip()

    # sending
    new_socket.sendall(game(client_choice).encode() + b'\n')

    data = b''
    while b'\n' not in data:
        data += new_socket.recv(1024)
    d = data.decode()
    d = d.split(',')
    print('Player 1:', d[1])
    print('Player 2:', d[2])
    print(d[0])

    counter -= 1
    if counter == 0:
        break

new_socket.close()
my_socket.close()

    

