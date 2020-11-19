##print('client')
from socket import *

chat_socket = socket()
chat_socket.connect(('127.0.0.1', 12345))

while True:
    print('WAITING FOR SERVER ...')
    data = b''
    while b'\n' not in data:
        data += chat_socket.recv(1024)
    print('Server wrote: ' + data.decode())

    data = input('Input message: ').encode()
    chat_socket.sendall(data + b'\n')

chat_socket.close()
