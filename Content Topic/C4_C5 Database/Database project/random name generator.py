from random import *

def random_name():
    for i in range(51):
        lst = ['JC', 'SEC']
        no = randint(0,1)
        print(lst[no])


print(random_name())
