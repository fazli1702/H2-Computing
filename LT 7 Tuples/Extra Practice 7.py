#question 1
##def deep_contains(obj, tup):
##    for i in range(len(tup)):
##        if type(tup[i]) == tuple:
##            deep_contains(obj, tup[i])
##        elif tup[i] == obj:
##            return True
##        elif i == len(tup)-1 and tup[i] != obj:
##            return False
##        else:
##            continue
            



def deep_contains2(obj, tup):
    if obj is tup:
        return True
    elif type(tup) != tuple:
        return False
    elif len(tup) == 1:
        return deep_contains2(obj, tup[0])
    else:
        return deep_contains2(obj, tup[0]) or deep_contains2(obj, tup[1:])

        
    

x = (2,1)
a = (1, x, 3, 4)
b = (1, (2,1), 3, 4)
c = (1, (x,3), 4)
d = (1, (2,1), 3, x)

y = (6, 3)
e = (1, ((y, 3)), 4)
f = (1, (2, (3, (4, y))))

##print(deep_contains(x, a))
##print(deep_contains(x, b))
##print(deep_contains(x, c))
##print(deep_contains(x, d))
##print(deep_contains(y, d))
##print(deep_contains(y, e))









#question 2
def deep_copy(tup):
    new_tup = ()
    
    for ele in tup:

        if type(ele) == tuple:
            new_tup += (deep_copy(ele),)

        else:
            new_tup += (ele,)
        
    return new_tup
        
    

##print(deep_copy((1,2,(3,4),5)))
##print(deep_copy(((1,2),(3,(4,5)))))
##print(deep_copy(((1,(2,(1,4))),(3,(4,5)))))















#question 3
def deviation(data):
    if len(data) == 1:
        return 0.0 

    n = len(data)
    mean = sum(data)/n
    numerator = 0
    frac = 0
    sd = 0
    #print('n:', n)
    #print('mean:', mean)

    for i in range(n):
        numerator += (data[i] - mean) ** 2
    #print('numerator:', numerator)
    
    frac = numerator/n
    #print('frac:', frac)
    sd = frac ** (1/2)

    return round(sd, 2)


##print(deviation((1, 4)))



















#question 4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def pascal_row_n(n):
        n -= 1
        row_n = ()
        for i in range(n):
            row_n += (factorial(n)/(factorial(n-i)*(factorial(i))),)
        return row_n + (1,)

def pascal(n):
    result = ()
    i = 1
    while i <= n:
        result += (pascal_row_n(i),)
        i += 1
    return result

    

        











#question 5
#abs is modulus function
def no_floor(tup):
    return (tup[1]-1) + abs(tup[1]-tup[2])

def time(tup):
    return 2 * no_floor(tup)

def elevator(tup):
    return (tup[0], time(tup), tup[2])

def operate_elevator(tup1, tup2):
    if tup1[0] == tup2[0] and tup1[0] == 1:
        total_floor = no_floor(tup1) + abs(tup1[2] - tup2[1]) + abs(tup2[1] - tup2[2])
        return ((1, total_floor*2, tup2[2]),) + ((2, 0, 1),)

    elif tup1[0] == tup2[0] and tup1[0] == 2:
        total_floor = no_floor(tup1) + abs(tup1[2] - tup2[1]) + abs(tup2[1] - tup2[2])
        return ((1, 0, 1),) + ((2, total_floor*2, tup2[2]),)

    elif tup1[0] == 1:
        return (elevator(tup1),) + (elevator(tup2),)
    else:
        return (elevator(tup2),) + (elevator(tup1),)
    


