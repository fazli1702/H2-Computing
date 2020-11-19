from connect4 import *

def test1():
    print('test1:')
    # test for vertical stacking
    board = Board()
    # board.display()
    print(board.check_vertical(5, 0, 1))
    # print(board.win(1))
    # print()

    board.drop_token(1, 1)
    # board.display()
    # print(board.check_vertical(5, 0, 1))
    print(board.win(1))
    # print()

    board.drop_token(1, 2)
    # board.display()
    # print(board.check_vertical(5, 0, 1))
    print(board.win(1))
    # print()

    board.drop_token(1, 1)
    # board.display()
    # print(board.check_vertical(5, 0, 1))
    print(board.win(1))
    # print()

    board.drop_token(1, 2)
    board.display()
    # print(board.check_vertical(5, 0, 1))
    print(board.win(1))
    print()

test1()

def test2():
    print('test2:')
    # test for horizontal placement
    board = Board()
    # board.display()
    # print(board.check_horizontal(5, 0, 1))
    print(board.win(1))
    # print()

    board.drop_token(1, 1)
    # board.display()
    # print(board.check_horizontal(5, 0, 1))
    print(board.win(1))
    # print()

    board.drop_token(2, 1)
    # board.display()
    # print(board.check_horizontal(5, 0, 1))
    print(board.win(1))
    # print()

    board.drop_token(3, 1)
    # board.display()
    # print(board.check_horizontal(5, 0, 1))
    print(board.win(1))
    # print()

    board.drop_token(4, 1)
    board.display()
    # print(board.check_horizontal(5, 0, 1))
    print(board.win(1))
    print()

test2()