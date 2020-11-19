from socket import *
import random

letters = [chr(i) for i in range(65, 91)]
letter = random.choice(letters)
print('letter:', letter)

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print('Connected to', addr)


while True:
    user_guess = new_socket.recv(1024).decode()
    if user_guess == letter:
        win = 'WIN'
        new_socket.sendall(win.encode())
        break
    
    elif user_guess > letter:
        info = '>'
        new_socket.sendall(info.encode())
        
    else:
        info = '<'
        new_socket.sendall(info.encode())
    


new_socket.close()
my_socket.close()
