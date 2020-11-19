'''
CONNECT 4 GAME
---------------------------
board: 6 rows * 7 columns
Each player have 21 tokens
---------------------------
The winner is the player who is the first
to connect four of their own tokens in a
horizontal / vertical


Write a program to play this game, letting a player to play against the computer, 
taking their turn in placing tokens, 'O' and 'X'. The computer will randomly choose a 
column to drop its token. Your program should display the grid after each token is added 
and declare the winner once four tokens have been connected.
'''

from random import randint

class Board:
    def __init__(self):
        # initialise emmpty board
        self.board = [['.' for i in range(7)] for i in range(6)]

    def is_empty(self):
        for row in self.board:
            for ele in row:
                if ele != '.':
                    return False
        return True

    # returns columns (list) there are full
    def column_full(self):
        full = []
        for col in range(7):
            if self.board[0][col] != '.':
                full.append(col+1)
        return full

    def drop_random(self):
        while True:
            col = randint(1, 7)
            if col not in self.column_full():
                break
        self.drop_token(col, 2)

    # game mechanics - mutate list
    def drop_token(self, column, player):
        column -= 1
        for row in range(5, -1, -1):
            # first row empty1
            if self.board[row][column] == '.':
                if row == 5:
                    if player == 1:
                        self.board[row][column] = 'O'
                        break
                    else:
                        self.board[row][column] = 'X'
                        break

                # there is token at next row
                else:
                    if self.board[row+1][column] != '.':
                        if player == 1:
                            self.board[row][column] = 'O'
                            break
                        else:
                            self.board[row][column] = 'X'
                            break
                        


    # check if there is win on board -> return bool
    def win(self, player):
        if self.is_empty():
            return False
        
        # check horizontal
        # check from bottom up & left to right
        for row in range(5, 0, -1):
            for col in range(3):
                if self.check_horizontal(row, col, player):
                    return True

        for row in range(5, 2, -1):
            for col in range(7):
                if self.check_vertical(row, col, player):
                    return True

        return False


    # helper functions for win
    def check_horizontal(self, row, col, player):
        # 4 in a row - horizontal
        # row is constant - col change
        for i in range(4):
            if player == 1:
                if self.board[row][col+i] != 'O':
                    return False
            else:
                if self.board[row][col+i] != 'X':
                    return False
        return True


    def check_vertical(self, row, col, player):
        # 4 in a row - vertical
        # col is constant - row change
        for i in range(4):
            if player == 1:
                if self.board[row-i][col] != 'O':
                    return False
            else:
                if self.board[row-i][col] != 'X':
                    return False
        return True
                        

                
    # convert to string
    def to_string(self):
        string_board = ''
        for row in self.board:
            string = '| '
            for i, ele in enumerate(row):
                string += ele + ' | '
            string_board += string + '\n'
        string_board += ('-' * 29) + '\n'

        footer = '| '
        for i in range(7):
            footer += str(i+1) + ' | '
        string_board += footer + '\n'
        
        return string_board

    def display(self):
        print(self.to_string())


def main():
    board = Board()
    board.display()
    while True:
        # player1/user move
        print('Player 1')
        player1_move = int(input('Enter column number:'))
        board.drop_token(player1_move, 1)
        board.display()
        print()
        if board.win(1):
            print('You won the game')
            break

        # player2/computer move
        print('Player 2')
        board.drop_random()
        board.display()
        print()
        if board.win(2):
            print('Computer won the game')
            break


if __name__ == '__main__':
    main()


