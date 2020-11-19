##print('server')
from socket import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket1, addr1 = my_socket.accept()
new_socket2, addr2 = my_socket.accept()
print('Connected to: ' + str(addr1))
print('Connected to: ' + str(addr2))
Msg = 'Hello from server\n'
new_socket1.sendall(Msg.encode())
new_socket2.sendall(Msg.encode())

new_socket1.close()
new_socket2.close()
my_socket.close()
