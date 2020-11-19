a = [['.' for i in range(5)] for i in range(5)]

def place_pellet(pond, x, y):
    x -= 1
    y -= 1
    if pond[y][x] == '.':
        pond[y][x] = 'H'
        return True
    else:
        pond[y][x] = 'P'
        return False


print(place_pellet(a, 1, 1))
