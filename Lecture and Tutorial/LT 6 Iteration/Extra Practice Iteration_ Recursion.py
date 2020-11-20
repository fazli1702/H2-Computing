#question 1
def hangman(string):
    total = ''
    for i in range(len(string)):
        if i % 2 == 0:
            total += string[i]
        else:
            total += ' '
    return total


##print(hangman('valedictorian'))
##print(hangman('computingrox'))
##print(hangman(''))








#question 2
def dancing_rec(string):
    if len(string) == 0 or len(string) == 1:
        return string
    else:
        return string[1] + string[0] + dancing_rec(string[2:])
    



##print(dancing('1234'))
##print(dancing('dance'))






#question 3
def dancing(string):
    total = ''
    while len(string) > 0:
        if len(string) == 1:
            total += string
        else:
            total += string[1] + string[0]
        string = string[2:]
    return total



##print(dancing('1234'))
##print(dancing('dance'))






#question 4
def is_perfect_square(n):
    x = n ** (1/2)
    if x % 1 == 0:
        return True
    return False





#question 5
def num_perfect_square_rec(n):
    if n == 1:
        return 1
    else:
        if is_perfect_square(n) == True:
            return 1 + num_perfect_square(n - 1)
        else:
            return num_perfect_square(n - 1)


##print(num_perfect_square(4))
##print(num_perfect_square(10))





#question 6
def num_perfect_square(n):
    lst = list(range(1, n+1))
    #print(lst)
    total = 0
    for ele in lst:
        if is_perfect_square(ele) == True:
            total += 1
    return total

##print(num_perfect_square(4))
##print(num_perfect_square(10))










#question 7
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

def evenFib(n):
    total = 0
    i = 0
    while fib(i) <= n:
        if fib(i) % 2 == 0:
            total += fib(i)
        i += 1
    return total


##print(evenFib(10))
##print(evenFib(50))
            
    







#question 8
from math import *

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def primeFactors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            if isPrime(i) == True:
                factors.append(i)
            else:
                continue
    return max(factors)



##print(primeFactors(13195))
##print(primeFactors(20000))



##def fact(n):
##    if n == 0:
##        return 1
##    else:
##        return n * fact(n-1)
##
##
##def find_e(n):    
##    if n == 0:
##        return 1
##    else:
##        return 1/fact(n) + find_e(n - 1)



#question 15
def find_e(n):
    if n == 0:
        return 1
    else:
        total = 0
        fact = 1
        for i in range(n+1):
            #print('i:', i)
            if i == 0:
                total += 1
            else:
                #print('fact:', fact)
                fact *= i
                #print('fact * i:', fact)
                total += 1 / fact
            #print('total:', total)
        return total
            
            
            

##print(find_e(0))
##print(find_e(2))
##print(find_e(8))
