##print('server')
from socket import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

while True:
    print('Type Ctrl-F6 or close the shell to terminate the server.')
    
    new_socket, addr = my_socket.accept()
    print('Connected to: ' + str(addr))
    new_socket.sendall(b'Hello from server\n')
    
    new_socket.close()

my_socket.close()
