from socket import *

s = socket()
s.connect(('127.0.0.1', 12345))

counter = 3
d = {'1':'Scissor', '2':'Paper', '3':'Stone'}
print('You are player 1')
while True:
    d = {'1':'Scissor', '2':'Paper', '3':'Stone'}
    data = s.recv(1024)
    choice = input(data.decode()).upper()
    choice = d[choice]
    s.sendall(choice.encode() + b'\n')
    data = b''
    while b'\n' not in data:
        data += s.recv(1024)
    d = data.decode()
    d = d.split(',')
    print('Player 1:', d[1])
    print('Player 2:', d[2])
    print(d[0])

    s.sendall(data)

    counter -= 1
    if counter == 0:
        break
    
s.close()
