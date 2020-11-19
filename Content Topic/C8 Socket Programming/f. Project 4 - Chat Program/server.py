##print('server')
from socket import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

print('Type Ctrl-F6 or close the shell to terminate the server.')
chat_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))
    
while True:
    # server send data to client
    data = input('Input message: ').encode()
    chat_socket.sendall(data + b'\n')

    data = b''
    # server receive data from client
    while b'\n' not in data:
        data += chat_socket.recv(1024)
    print('Client wrote: ' + data.decode())

chat_socket.close()
my_socket.close()
