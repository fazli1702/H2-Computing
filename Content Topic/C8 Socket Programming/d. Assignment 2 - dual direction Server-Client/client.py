##print('client')
from socket import *

my_socket = socket()

# receive from server
my_socket.connect(('127.0.0.1', 12345))
data = b''
while b'\n' not in data:
    data += my_socket.recv(1024)
    
print(data.decode())

# connect to server
my_socket.sendall(b'Hello from client\n')



my_socket.close()
