##print('server')
from socket import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

# connect to client
new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))

new_socket.sendall(b'Hello from server\n')

# receive from client
data = b''
while b'\n' not in data:
    data += new_socket.recv(1024)
    
print(data.decode())

new_socket.close()
my_socket.close()
