from socket import *
import string
import random



def to_string(rect):
    string = ''
    for row in rect:
        for ele in row:
            string += ele
        string += '\n'
    return string



my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print('Connected to:', str(addr))


letters = string.ascii_uppercase
correct = 0

while True:
    for _ in range(3):
        n = random.randint(1, 10)  # number of letters
        letter_i = random.randint(0, len(letters)-1) 
        rect = [['.' for j in range(10)] for j in range(5)] # init empty rect
        coordinates = []
        for k in range(n):  # add letters
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 4)
                coord = (x, y)
                if coord not in coordinates:  # ensure not repeated coordinate
                    rect[y][x] = letters[letter_i]
                    break

        # send to client
        rect_string = to_string(rect)
        new_socket.sendall(rect_string.encode())

        # receive client input
        player_input = new_socket.recv(1024).decode()
        if int(player_input) == n:
            correct += 1
            
    new_socket.sendall(str(correct).encode())
    break


new_socket.close()
my_socket.close()







