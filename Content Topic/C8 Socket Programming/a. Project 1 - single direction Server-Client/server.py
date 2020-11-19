# server
from socket import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))
Msg = 'Hello from server\n'
new_socket.sendall(Msg.encode())

new_socket.close()
my_socket.close()
