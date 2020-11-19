from socket import *

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))

maxim, minim = my_socket.recv(1024).decode().split(',')
user_len = input(f'Choose the length of word to guess:[{minim} to {maxim}]:')
guessCount = int(user_len) * 2

my_socket.sendall(user_len.encode())
guessCount = int(my_socket.recv(1024).decode())

print(f'You have {guessCount} attempts. Good Luck!')

while True:
    i = my_socket.recv(1024).decode()
    userWord = my_socket.recv(1024).decode()
    print('i:', i)
    print('userWord:', userWord)
    userLetter = input(f'[{i}]Guess letter:')
    my_socket.sendall(userLetter.encode())

    solve = my_socket.recv(1024).decode()
    if solve == 'WIN':
        print('WIN')
        break

    elif solve == 'L':
        lose = my_socket.recv(1024).decode()
        print(lose)
        break

    
my_socket.close()
