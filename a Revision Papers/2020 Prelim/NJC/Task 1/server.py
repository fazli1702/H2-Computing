import random

def read():
    with open('WORDS.TXT') as f:
        data = f.readlines()
        words = {}
        minim = maxim = 0
        for ele in data:
            ele = ele.strip()
            minim = len(ele)  # give temp value 
            maxim = len(ele)  
            if len(ele) not in words:
                words[len(ele)] = [ele]
            else:
                words[len(ele)] += [ele]


    for k, v in words.items():
        if k < minim:
            minim = k
        if k > maxim:
            maxim = k
            
    return maxim, minim, words

def lst_to_str(lst):
    s = ''
    for ele in lst:
        s += str(ele)
    return s



from socket import *

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print('Connected to:', addr)

maxim, minim, words = read()
new_socket.sendall((str(maxim)+','+str(minim)).encode())

# get secret word
user_len = int(new_socket.recv(1024).decode())
secretWord = random.choice(words[user_len])
userWord = ['.' for i in range(user_len)]

guessCount = user_len * 2
new_socket.sendall(str(guessCount).encode())
guess = False

while guessCount != 0:
    new_socket.sendall(str(guessCount).encode())
    new_socket.sendall(lst_to_str(userWord).encode())

    userLetter = new_socket.recv(1024).decode()
    for i in range(user_len):
        if secretWord[i] == userLetter:
            userWord[i] = userLetter
            break

    if lst_to_str(userWord) == secretWord:
        new_socket.sendall('WIN'.encode())
        guess = True
        break

    guessCount -= 1

if not guess:
    new_socket.sendall('L'.encode())
    new_socket.sendall(('LOSE..The word is ' + secretWord).encode())

new_socket.close()
my_socket.close()
    




