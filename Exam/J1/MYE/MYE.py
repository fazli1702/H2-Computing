##Q1
def rate(currency_1, currency_2):
    return currency_2 / currency_1

USD=0.72669
JPY=79.97
SGD=1

##print(rate(SGD, USD))
##print(rate(SGD, JPY))
##print(rate(USD, JPY))






##Q2
##2.1
def triangle(n):
    if n == 1:
        return 1
    return n + triangle(n-1)

##print(triangle(4))
##print(triangle(7))


##2.2
def sum_even_triangle(n):
    if n == 1:
        return 0
    elif triangle(n) % 2 == 0:
        return triangle(n) + sum_even_triangle(n-1)
    else:
        return sum_even_triangle(n-1)


##print(sum_even_triangle(1))
##print(sum_even_triangle(3))
##print(sum_even_triangle(7))













##Q3
##3.1
def cipher_alphabet(key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = key
    for ele in alphabet:
        if ele not in string:
            string += ele
    return string

##print(cipher_alphabet('zebra'))



##3.2
def cipher_dictionary(key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = cipher_alphabet(key)
    dic = {}
    for i in range(len(string)):
        dic[alphabet[i]] = string[i]
    return dic

##print(cipher_dictionary('zebra'))




##3.3
def encrypt(message, key):
    dic = cipher_dictionary(key)
    string = ''
    for ele in message:
        if ele == ' ':
            string += ' '
        else: 
            string += dic[ele]
    return string

##print(encrypt('hello world', 'zebra'))














##Q4
##4.1
def to_string(lst):
    string = ''
    for ele in lst:
        if ele < 100:
            string += '0' * (3 - len(str(ele))) + str(ele)
        else:
            string += str(ele)
    return string

##print(to_string([29,100,67,31,45,84]))


##4.2
def average(string):
    lst = []
    while len(string) != 0:
        lst.append(int(string[:3]))
        string = string[3:]
    total = sum(lst)
    n = len(lst)
    average = total / n
    return average

##print(average('029100067031045084'))










##Q5
from random import randint

def guessing_game():
    SecretNumber = randint(0, 100)
    Guess  = int(input('Guess:'))
    counter = 1
    while Guess != SecretNumber:
        if Guess > SecretNumber:
            counter += 1
            Guess = int(input('Input a smaller number:'))
        elif Guess < SecretNumber:
            counter +=1
            Guess = int(input('Input a larger number:'))
    return counter

##print(guessing_game())











##Q6
from module import*

def deviation(lst):
    scores = []
    for ele in lst:
        scores.append(get_score(ele))

    total = sum(scores)
    n = size(lst)
    mean = total / n

    numerator = 0
    for ele in scores:
        numerator += ((ele - mean) ** 2)

    sd = (numerator / n) ** (1/2)
    return round(sd, 2)




students = [('tiffany', 'A', 15),
            ('jane', 'B', 10),
            ('ben', 'C', 8),
            ('simon', 'A', 21),
            ('eugene', 'A', 21),
            ('john', 'A', 15),
            ('jimmy', 'F', 1),
            ('charles', 'C', 9),
            ('freddy', 'D', 4),
            ('dave', 'B', 12)]


##print(deviation(students))

    












##Q7
def make_queue():
    return []

def enqueue(q, item):
    return q.append(item)

def front(q):
    return q[0]

##7.1
def delete(q, item):
    if item not in q:
        return None
    else:
        for ele in q:
            if ele == item:
                q.remove(item)

def shift(q, item):
    if item not in q:
        return None
    else:
        for ele in q:
            if ele == item:
                delete(q, item)
                q.insert(0, item)




##7.2
orders = make_queue()
enqueue(orders, 'Fish Burger')
enqueue(orders, 'Chicken Burger')
enqueue(orders, 'Chicken Nuggets')
enqueue(orders, 'Fried Chicken')
enqueue(orders, 'Nasi Lemak Burger')
delete(orders, 'Chicken Nuggets')
##print(front(orders))
delete(orders, 'Fried Chicken')
shift(orders, 'Nasi Lemak Burger')
##print(front(orders))
##print(orders)

















##Q8
##8.1       
def balanced(name):
    total = 0
    for ele in name:
        total += ord(ele)
    if total % 2 == 0:
        return True
    return False

##print(balanced('Hulk'))



##8.2
def thanos(names):
    i = 0
    while i < len(names):
        if balanced(names[i]) == False:
            names.remove(names[i])
            i = 0
        else:
            i += 1
    return names

singers=['JustinBieber','MichaelJackson','Rihanna', 'LadyGaga',\
         'TaylorSwift','KatyPerry','EdSheeran','BrunoMars']
avengers=['IronMan','BlackPanther','CaptainAmerica','Hulk',
          'SpiderMan','NickFury','Hawkeye','DoctorStrange']

##print(thanos(singers))
##print(thanos(avengers))





##8.3
def power(stone):
    return stone[1]

def top(lst):
    maxim = lst[0]
    for ele in lst:
        if power(ele) < power(maxim):
            maxim = ele
    lst.remove(maxim)
    return maxim

infinity_stones = [('soul stone',13),
                   ('mind stone',6),
                   ('reality stone',9),
                   ('space stone',7),
                   ('time stone',1),
                   ('power stone',5)]

##print(top(infinity_stones))
##print(top(infinity_stones))



##8.4
def sort_stones(lst):
    sort = []
    for i in range(len(lst)):
        sort.append(top(lst))
    return sort

##print(sort_stones(infinity_stones))
        
    
