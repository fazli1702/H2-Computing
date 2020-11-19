from socket import *

s = socket()
s.connect(('127.0.0.1', 12345))

while True:
    data = b''
    while b'\n' not in data:
        data += s.recv(1024)
    received = data.decode().strip()

    if received == 'LOW':
        print('Your guess is too low.')
    elif received == 'HIGH':
        print('Your guess is to high.')
    elif received == 'GUESS':
        guess = int(input('Enter guess (1-100): '))
        s.sendall(str(guess).encode() + b'\n')
    elif received == 'WIN':
        print('You Win!')
        break
    elif received == 'GAMEOVER':
        print('You ran out of tries! Game over.')
        break

s.close()
