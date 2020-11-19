from random import randint

def new_pond():            # initialise empty grid
    # 15-by-8 2D array
    return [['.' for i in range(15)] for i in range(8)]


def string_pond(pond):            # print empty grid
    string = ''
    for row in pond:
        for ele in row:
            string += ele
        string += '\n'
    return string

def print_pond(pond):
    print(string_pond(pond))


def get_user_input(pond):
    x = int(input('X coordinate <1 to 15>? '))
    y = int(input('Y coordinate <1 to 8>? '))
    x -= 1
    y -= 1
    pond[y][x] = 'S'


def put_3_fish(pond):
    randPos = []
    
    # make sure not same position
    while len(randPos) != 3:
        x = randint(0, 14)
        y = randint(0, 7)
        coord = [x, y]
        if coord not in randPos:
            randPos.append(coord)
            
    for x, y in randPos:
        pond[y][x] = 'F'


def place_pellet(pond, x, y):
    x -= 1
    y -= 1
    if pond[y][x] == 'F':
        pond[y][x] = 'H'
        return True
    else:
        pond[y][x] = 'P'
        return False
    



from socket import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print(f'Connected to {addr}')


counter = 0
pond = new_pond()
put_3_fish(pond)
new_socket.sendall(string_pond(pond).encode())
while True:
    x = int(new_socket.recv(1024).decode())
    y = int(new_socket.recv(1024).decode())
    
    if place_pellet(pond, x, y):
        counter += 1

    if counter == 3:
        win = 'WIN'
        new_socket.sendall(win.encode())
        new_socket.sendall(string_pond(pond).encode())
        break
    else:
        new_socket.sendall(string_pond(pond).encode())




my_socket.close()
new_socket.close()









