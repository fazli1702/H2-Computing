from socket import *

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))

pond = my_socket.recv(1024).decode()
print(pond)
while True:
    x = input('X coordinate <1 to 15>? ').encode()
    y = input('Y coordinate <1 to 8>? ').encode()
    my_socket.sendall(x)
    my_socket.sendall(y)

    data = my_socket.recv(1024).decode()
    
    if data == 'WIN':
        pond = my_socket.recv(1024).decode()
        print(pond)
        print('*'*30)
        print('You have won the game!!')
        break
    
    else:
        # data - pond
        print(data)



my_socket.close()
