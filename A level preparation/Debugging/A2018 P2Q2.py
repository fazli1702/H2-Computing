def sodoku():
    puzzle = [[0 for i in range(9)] for i in range(9)]
    with open('soduku.txt', 'w') as f:
        for row in puzzle:
            f.write(str(row) + '\n')
