##print('server')
from socket import *
from time import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))

new_socket.sendall(b'Hello fr')
sleep(0.1)
new_socket.sendall(b'om server\n')

new_socket.close()
my_socket.close()
