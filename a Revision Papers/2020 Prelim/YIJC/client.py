def get_user_input():
    while True:
        x = input('Enter x coordinate: ')
        if x.isdigit():
            if 0 <= int(x) <= 5:
                break
                
    while True:
        y = input('Enter y coordinate: ')
        if y.isdigit():
            if 0 <= int(y) <= 5:
                break
    
    return x + ',' + y


from socket import *

my_socket = socket()
my_socket.connect(('127.0.0.1', 12345))

for i in range(5):
    pos = get_user_input()  # validate user input
    my_socket.sendall(pos.encode())

    grid = my_socket.recv(1024).decode()
    print(grid)

grid = my_socket.recv(1024).decode()
print(grid)

my_socket.close()
