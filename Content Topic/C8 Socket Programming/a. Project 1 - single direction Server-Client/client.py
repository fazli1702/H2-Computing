# client
from socket import *

my_socket = socket()

addr = input('Enter IPv4 address of server: ')
port = int(input('Enter port number of server: '))
my_socket.connect((addr, port))

Msg = my_socket.recv(1024)
print(Msg.decode())

my_socket.close()
