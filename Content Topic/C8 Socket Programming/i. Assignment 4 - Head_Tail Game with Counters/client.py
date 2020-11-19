from socket import *

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))

n = 0
c = 0
while True:
    data = my_socket.recv(1024)

    # sending
    guess = input(data.decode()).upper()
    my_socket.sendall(guess.encode() + b'\n')
    n += 1
    
    # receiving
    data = b''
    while b'\n' not in data:
        data += my_socket.recv(1024)
    print(data.decode())
    if 'right' in data.decode():
        c += 1

    if guess == 'Q':
        n -= 1
        print(f'You have guessed correctly {c} out of {n} times.')
        break

my_socket.close()
