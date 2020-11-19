from random import *


def last_letter(nric):
    num = nric[1:]
    check = [2, 7, 6, 5, 4, 3, 2]
    letter = {0:'J', 1:'Z', 2:'I', 3:'H', 4:'G', 5:'F', 6:'E', 7:'D', 8:'C', 9:'B', 10:'A'}
    total = 0
    for i in range(len(num)):
        total += int(num[i]) * check[i]
    if nric[0] == 'T':
        total += 4
    r = total % 11
    return letter[r]


def random_nric():
    for i in range(2):
        nric = 'T'
        level = ''
        for j in range(7):
            no = randint(0,9)
            if j == 0:
                nric += '0'
            elif j == 1:
                ran = randint(3,4)
                nric += str(ran)
            else:
                nric += str(no)
        nric += last_letter(nric)
        if nric[2] == '3' or nric[2] == '4':
            level = 'SEC'
        else:
            level = 'JC'
            
        print(nric)


print(random_nric())
            


            
            
            
