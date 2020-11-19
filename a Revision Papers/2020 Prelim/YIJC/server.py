def read():
    with open('GAME.TXT') as f:
        data = f.readlines()
        grid = []
        for row in data:
            temp = []
            for ele in row.strip():
                temp.append(ele)
            grid.append(temp)
    return grid


def hide_grid(grid):
    new_grid = []
    for row in grid:
        temp = []
        for col in row:
            if col == 'X':
                temp.append('.')
            else:
                temp.append(col)
        new_grid.append(temp)
    return new_grid


def fire(pos, grid):
    x, y = pos
    if grid[y][x] == 'X':
        grid[y][x] = 'S'
    else:
        grid[y][x] = 'O'
        
    
def display_grid(grid):
    s = ''
    for row in grid:
        for col in row:
            s += col
        s += '\n'
    return s



from socket import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print('Connected to:', addr)

grid = read()
for i in range(5):
    pos = new_socket.recv(1024).decode().split(',')
    pos[0] = int(pos[0])
    pos[1] = int(pos[1])

    fire(pos, grid)
    new_grid = display_grid(hide_grid(grid))
    new_socket.sendall(new_grid.encode())


new_socket.sendall(display_grid(grid).encode())

new_socket.close()
my_socket.close()











    
    
