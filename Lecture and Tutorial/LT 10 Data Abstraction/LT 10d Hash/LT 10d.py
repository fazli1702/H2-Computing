#question 1
# Hash Function - Part 1 slide 19 
def hash(string):
    total = 0
    for i in range(len(string)):
        total += ord(string[i]) * (i+1)
    return total % 5


# Hash Table (without Collision) - Part 1 slide 21
def init_table(n):
    table = []
    table += [''] * n
    return table

def hashtable(seq):
    tbl = init_table(len(seq))
    for ele in seq:
        i = hash(ele)
        if tbl[i] == '':
            tbl[i] = ele
        else:
            print(ele, ' is not added.')
    return tbl


# Search (without Collision) - Part 1 slide 27
def search(table, name):
    i = hash(name)
    if table[i] == name:
        return True
    else:
        return False


lst = ['WONG CHU HENG TIM', 'KATHRYN CHAN HUI', 'PATEL KRISH KADAMB', 'MANSIB MIRAJ', 'SEAN NG JING HAO']
data_table = hashtable(lst)



##print(hash('NADHIRAH BTE AYUB KHAN'))
##print(hash('ABRAHAM TEOW LIANG THYE'))
##print(hashtable(lst))
##print(search(data_table, 'SEAN NG JING HAO'))
##print(search(data_table, 'TANG HAOYANG'))
##print(search(data_table, 'RYU HYUNSUN'))
##print(init_table(5))












#question 2
def hash(string):
    total = 0
    for i in range(len(string)):
        total += ord(string[i]) * (i+1)
    return total % 5


## (a) Collision Resolution : Separate Chaining 

# Hash Table (hashing with Separate Chain) - Part 2 slide 11
def hashtable(seq):
    tbl = init_table(len(seq))
    for ele in seq:
        i = hash(ele)
        if tbl[i] == '':
            tbl[i] = ele
        else:
            if type(tbl[i]) != list:
                tbl[i] = [tbl[i], ele]
            else:
                tbl[i] = tbl[i] + [ele]
    return tbl

# Search (hashing with Separate Chain) - Part 2 slide 13
def search(table, name):
    i = hash(name)
    if table[i] == '':
        return False
    elif table[i] == name:
        return True
    elif type(table[i]) == list:
        return name in table[i]
    else:
        return False


lst = ['WONG CHU HENG TIM', 'KATHRYN CHAN HUI', 'PATEL KRISH KADAMB', 'MANSIB MIRAJ', 'TANG HAOYANG']
data_table = hashtable(lst)


##print(data_table)
##print(search(data_table, 'TANG HAOYANG'))
##print(search(data_table, 'KATHRYN CHAN HUI'))
##print(search(data_table, 'ANG ZHEN YI'))
##print(search(data_table, 'VOO ZI XUAN, FELIX'))
##print(search(data_table, 'SHWE TIN AUNG'))












#question 3
# Hash Function - Part 1 slide 19 
def hash(string):
    total = 0
    for i in range(len(string)):
        total += ord(string[i]) * (i+1)
    return total % 5

def init_table(n):
    table = []
    table += [''] * n
    return table

## (b) Collision Resolution : Open Hashing 

# Hash Table (using Open Hashing) - Part 2 slide 15-18
def openhash(table, index, item):
    while True:
        if table[index] == '':
            table[index] = item
            return table
        else:
            index = (index + 1) % len(table)

def hashtable(seq):
    tbl = init_table(len(seq))
    for ele in seq:
        i = hash(ele)
        if tbl[i] == '':
            tbl[i] = ele
        else:
            return openhash(tbl, i, ele)
    return tbl

# Search (Hash Table using Open Hashing) - Part 2 slide 20-21
def linear_search(tbl, item, i):
    for cell in range(len(tbl)):
        if tbl[i] == '':
            return False
        elif tbl[i] == item:
            return True
        i = (i + 1) % len(tbl)
    return False


def search(table, name):
    i = hash(name)
    if table[i] == '':
        return False
    elif table[i] == name:
        return True
    else:
        return linear_search(table, name, i)


lst = ['WONG CHU HENG TIM', 'KATHRYN CHAN HUI', 'PATEL KRISH KADAMB', 'MANSIB MIRAJ', 'TANG HAOYANG']
data_table = hashtable(lst)


print(data_table)
print(search(data_table, 'TANG HAOYANG'))
print(search(data_table, 'NG JUN JIE, KEITH'))

    
    
