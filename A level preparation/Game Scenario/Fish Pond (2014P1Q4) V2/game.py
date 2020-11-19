from random import randint

def new_pond():            # initialise empty grid
    # 15-by-8 2D array
    return [['.' for i in range(15)] for i in range(8)]


def print_pond(pond):            # print empty grid
    for row in pond:
        string = ''
        for ele in row:
            string += ele
        print(string)


def get_user_input(pond):
    x = int(input('X coordinate <1 to 15>? '))
    y = int(input('Y coordinate <1 to 8>? '))
    x -= 1
    y -= 1
    pond[y][x] = 'S'


def put_3_fish(pond):
    randPos = []
    
    # make sure not same position
    while len(randPos) != 3:
        x = randint(0, 14)
        y = randint(0, 7)
        coord = [x, y]
        if coord not in randPos:
            randPos.append(coord)
            
    for x, y in randPos:
        pond[y][x] = 'F'


def place_pellet(pond):
    x = int(input('X coordinate <1 to 15>? '))
    y = int(input('Y coordinate <1 to 8>? '))
    x -= 1
    y -= 1
    if pond[y][x] == 'F':
        pond[y][x] = 'H'
    else:
        pond[y][x] = 'P'


    
