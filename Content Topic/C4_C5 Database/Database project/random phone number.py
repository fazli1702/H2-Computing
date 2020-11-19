from random import *

def PhoneNo():
    for j in range(20):
        num = ''
        for i in range(8):
            if i == 0:
                num += str(randint(8,9))
            else:
                num += str(randint(0,9))
        print(num)
            

PhoneNo()
