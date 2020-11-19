# stage1
# open MAZE.TXT file and print line by line
def read():
    with open('MAZE.TXT') as f:
        data = f.readlines()
        for row in data:
            row = row.strip()
            print(row)

def display(maze):
    for row in maze:
        print(row)

#stage2
def read_wall(filename):
    '''store "X" coordinates and return it'''
    walls = []
    y = 0
    with open(filename) as f:
        data = f.readlines()
        for row in data:
            row = row.strip()
            for x in range(len(row)):
                if row[x] == 'X':
                    walls.append([x, y])
            y += 1
    return walls


# stage 3
def print_it(lst):
    '''read "X" coordinate and print it'''
    row = ['.'] * 10
    maze = [row for i in range(11)]
    # for ele in maze:
    #     print(ele)
    for ele in lst:
        x, y = ele
        # print(x, y)
        maze[y][x] = 'X'

    for row in maze:
        print(row)




# Do not modify the following:
wall = read_wall('MAZE.TXT')
# print(wall)
##display()
print_it(wall)
