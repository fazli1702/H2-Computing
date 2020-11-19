# Task 3.1

'''
Design:
 - use a 2d array to represent 3x3 grid
 - use '.' for blank  and 'O' & 'X' to represent O & X  (string)
 - user input coordinate (x, y)
'''

def displayInstructions():
    string = '''
    Instructions: \n
    To input your move, you are prompted to input the \n
    x and y coordinate of your move \n
    '''
    return string



def getBoard():
    return [['.' for i in range(3)] for i in range(3)]

def getPlayerMove():
    x = int(input('Enter x coordinate: '))
    y = int(input('Enter y coordinate: '))
    x -= 1
    y -= 1
    
    return (x, y)

def setMove(board, player, coord):
    if player == 1:
        move = 'O'
    else:
        move = 'X'

    x, y = coord
    board[y][x] = move



def checkHorizontal(board, player):
    if player == 1:
        move = 'O'
    else:
        move = 'X'
        
    for row in board:
        same = False
        for ele in row:
            if ele == move:
                same = True
            else:
                same = False
                break
        if same:
            return True

    return False


def checkVertical(board, player):
    if player == 1:
        move = 'O'
    else:
        move = 'X'

    for x in range(3):
        same = False
        for y in range(3):
            if board[y][x] == move:
                same = True
            else:
                same = False
                break
        if same:
            return True
        
    return False


def checkDiagonal(board, player):
    if player == 1:
        move = 'O'
    else:
        move = 'X'

    same = False
    for i in range(3):
        if board[i][i] == move:
            same = True
        else:
            same = False
            break

    if same:
        return True

    x = 0
    y = 2
    same = False
    for j in range(3):
        if board[y][x] == move:
            same = True
            x += 1
            y -= 1
        else:
            same = False
            break
        
    if not same:
        return False
    return True


def checkWin(board, player):
    if checkHorizontal(board, player):
        return True
    elif checkVertical(board, player):
        return True
    elif checkDiagonal(board, player):
        return True
    else:
        return False
    

def boardString(board):
    string = ''
    for row in board:
        string += row[0], '|' + row[1] + '|' + row[2]
        string += '\n'
    return string

def displayBoard(board):
    print(boardString(board))


def main():
    board = getBoard()
    displayBoard(board)
    for i in range(3):
        getPlayerMove(board, 1)
        displayBoard(board)
        if chekcWin(board, 1):
            return 'Player 1 have won!!!!'
        
        getPlayerMove(board, 2)
        displayBoard(board)
        if checkWin(board, 2):
            return 'Player 2 have won!!!!'
        

# test case
board1 = [['O', 'O', 'O'],
          ['.', '.', '.'],
          ['.', '.', '.']]

board2 = [['O', '.', '.'],
          ['O', '.', '.'],
          ['O', '.', '.']]

board3 = [['O', '.', '.'],
          ['.', 'O', '.'],
          ['.', '.', 'O']]

board4 = getBoard()


print(checkWin(board1, 1))
print(checkWin(board2, 1))
print(checkWin(board3, 1))
print(checkWin(board4, 1))



def main():
    from socket import *

    my_socket = socket()
    my_socket.bind(('127.0.0.1', 12345))
    my_socket.listen()

    new_socket, addr = my_socket.accept()
    print('Connected to', addr)


    board = getBoard()
    ins = displayInstructions()
    print(ins)
    new_socket.sendall(ins.encode())

    print('You are player 2')

    # main game loop
    for i in range(3):
        # player 1 move / display board
        displayBoard(board)
        player1_move = getPlayerMove()
        setMove(board, 1, player1_move)
        displayBoard(board)

        if checkWin(board, 1):  
            win = '1WIN'
            new_socket.sendall(win.encode())
            new_socket.sendall(boardString(board).encode())
            print('Player 1 has won the game')
            break

        new_socket.sendall(boardString(board).encode())

        
        # receive player 2 move
        x = new_socket.recv(1024).decode()
        y = new_socket.recv(1024).decode()
        player2_move = (x, y)
        setMove(board, 2, player2_move)

        if checkWin(board, 2):
            win = '2WIN'
            new_socket.sendall(win.encode())
            new_socket.sendall(boardString(board).encode())
            displayBoard(board)
            print('Player 2 has won the game')
            break
                
        
        
        
            
        
    my_socket.close()
    new_socket.close()
