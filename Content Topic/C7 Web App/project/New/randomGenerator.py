import random
import string

days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

def randomDay(n):
    for i in range(n):
        print(random.choice(days))


def randomPrice(n):
    for i in range(int(n/2)):
        h1 = random.randint(500, 600)
        h2 = random.randint(h1, h1+200)
        print(h1)
        print(h2)



def randomTime(n):
    seq = [0, 30]
    for i in range(n):
        h = random.randint(16, 20)
        m = random.choice(seq)
        if m == 0:
            m = '00'
        print('start:', str(h) + ':' + str(m), end='')
        h += 2
        print('    end:', str(h) + ':' + str(m))


def randomName(n):
    names = []
    with open('names.txt') as f:
        for ele in f:
            names.append(ele.lower())
    for i in range(n):
        print(random.choice(names).strip())

def randomPassword(n):
    for i in range(n):
        letters = string.ascii_lowercase
        print(''.join(random.choice(letters) for j in range(8)))
        


def randomNRIC(n):
    for i in range(n):
        nric = random.choice(['T', 'S'])
        for j in range(7):
            nric += str(random.randint(0, 9))
        nric += random.choice(string.ascii_uppercase)
        print(nric)

def randomTel(n):
    for i in range(n):
        phone = str(random.randint(8, 9))
        for j in range(7):
            phone += str(random.randint(0, 9))
        print(phone)


def randomClassID(n):
    a = ['C', 'M', 'P']
    for i in range(n):
        classID = random.choice(a) + '0' + str(random.randint(1, 9))
        print(classID)
        


if __name__ == '__main__':
##    randomNRIC(8)
##    randomName(8)
##    randomTel(8)
##    randomPassword(8)
    randomClassID(10)


    
