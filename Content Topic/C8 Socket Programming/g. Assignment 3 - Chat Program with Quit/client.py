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

    if data.decode().upper() == 'BYE\n':
        chat_socket.close()
        break

    data = input('Input message: ').encode()
    chat_socket.sendall(data + b'\n')
    if data.decode().upper() == 'BYE':
        chat_socket.close()
        break

chat_socket.close()
