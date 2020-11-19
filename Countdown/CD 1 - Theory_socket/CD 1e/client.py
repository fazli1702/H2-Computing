from socket import *

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))

while True:
    for _ in range(3):
        rect = my_socket.recv(1024).decode()
        print(rect)

        while True:
            player_input = input('Enter number of letters:')
            if player_input.isdigit():
                my_socket.sendall(player_input.encode())
                break

    correct = my_socket.recv(1024).decode()
    print('Number of correct answer is:', correct)
    break
    

my_socket.close()
