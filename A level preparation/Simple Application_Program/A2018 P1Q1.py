'task 1.1'

def getName(person):
    return person[0]

def getStep(person):
    return person[1]


# reading file
def read():
    with open('STAR.txt') as f:
        data = f.readlines()
        last_star = []
        i = 0
        for row in data:
            row = row.strip()
            if i == 0:
                last_star.append(row)
                i += 1
            else:
                last_star.append(row[1:])
    return last_star[::-1]

##    print(last_star)


def main():
    # input names - max 10
    data = []
    for i in range(10):
        name, step = input('Enter name and step:').split(',')
        data.append([step, name])
    data.sort(reverse=True)
    
    curr_star = data[0]
    last_star = read()

    print(f"Last week, {getName(last_star)} was 'Star of the Week' \
            with {getStep(last_star)} steps taken")
    print(f"This week, {getName(curr_star)} is 'Star of the Week' \
            with {getStep(curr_star)} steps taken")

    with open('STAR.txt', 'a') as f:
        f.write(f'{getName(curr_star)}\n')
        f.write(f'{getStep(curr_star)}\n')
    


    
test1 = 'Yi Ling Aw, 10232'
test2 = 'Ryan Batisah, 42231'
test3 = 'Ryan Batisah, 42231'
test4 = 'Lee Casmir, 35020'
test5 = 'Daniel Bennett, 60192'
test6 = 'Sarah Heng Chee, 29389'
test7 = 'Vanessa Lim, 67152'
tset8 = 'Wong Yip, 53231'
test9 = 'Rin Xie, 49480'
test10 = 'Tin Wee, 49480'
test11 = 'David Bala, 32010'
 
