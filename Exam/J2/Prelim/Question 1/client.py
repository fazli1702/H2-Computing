from socket import *

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))



for i in range(5):
    x = input('Enter x coordinate:').encode()
    y = input('Enter y coordinate:').encode()
    my_socket.sendall(x)
    my_socket.sendall(y)

    grid = my_socket.recv(1024).decode()
    print(grid)


grid = my_socket.recv(1024).decode()
print(grid)

my_socket.close()
