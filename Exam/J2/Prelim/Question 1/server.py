def read():
    grid = []
    with open('GAME.txt') as f:
        data = f.readlines()
        for ele in data:
            ele = ele.strip()
            row = []
            for i in ele:
                row.append(i)
            grid.append(row)
            
    return grid

def display(grid):
    string = ''
    for row in grid:
        for ele in row:
            string += ele
        string += '\n'
    return string

def hide_grid(grid):
    string = ''
    for row in grid:
        for ele in row:
            if ele == 'X':
                string += '.'
            else:
                string += ele
        string += '\n'
    return string
    

def fire(pos, grid):
    x, y = pos
    if grid[y][x] == '.':
        grid[y][x] = 'O'
    else:
        grid[y][x] = 'S'

# -------------------------------------- #

from socket import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print('Connected to:', addr)

# intialise grid
grid = read()

for i in range(5):
    x = new_socket.recv(1024).decode()
    y = new_socket.recv(1024).decode()

    pos = (int(x), int(y))
    fire(pos, grid)
    new_socket.sendall(hide_grid(grid).encode())


new_socket.sendall(display(grid).encode())



new_socket.close()
my_socket.close()
