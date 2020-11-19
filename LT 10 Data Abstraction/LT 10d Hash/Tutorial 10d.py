#question 1
def GenerateHash(SearchName):
    HashTotal = 0
    for i in range(len(SearchName)):
        HashTotal += ord(SearchName[i]) * (i+1)
    Hash = HashTotal % 42
    return Hash

##print(GenerateHash('SONAWANE BHAVESH SANJAY'))
##print(GenerateHash('DEAN ALEXANDER SANTOS BUNO'))







#question 2
def read_file(filename):   
    with open(filename, "r") as f:
        content = f.readlines()
        lst = []
        for row in content:
            row = row.rstrip('\n')
            lst.append(row)
        return lst

def init_table(n):
    table = []
    table += [''] * n
    return table


def openhash(table, index, item):
    while True:
        if table[index] == '':
            table[index] = item
            return table
        else:
            index = (index + 1) % len(table)


def HashTable(filename):
    data = read_file(filename)
    table = init_table(len(data))
    for ele in data:
        i = GenerateHash(ele)
        if table[i] == '':
            table[i] = ele
        else:
            openhash(table, i, ele)
    return table
    

data_table = HashTable('NAMES.txt')


##print(data_table[:5])










#question 3
def linear_search(tbl, item, i):
    for cell in range(len(tbl)):
        if tbl[i] == '':
            return 'NOT FOUND'
        elif tbl[i] == item:
            return (i, item)
        else:
            i = (i + 1) % len(tbl)
    return 'NOT FOUND'

def Find1(SearchName):
    data = data_table
    i = GenerateHash(SearchName)
    if data[i] == '':
        return 'NOT FOUND'
    elif data[i] == SearchName:
        return (i, SearchName)
    else:
        return linear_search(data, SearchName, i)

data_table = HashTable('NAMES.txt')

##print(Find('CHIA YEE JEY'))
##print(Find('ASHVIN SAKTHI VALE'))
##print(Find('WONG RUI HAO'))
##print(Find('SINGAPORE'))












#question 4
def GenerateHash(name):
    total = 0
    for i in range(len(name)):
        total += ord(name[i]) * (i + 1)
    return total % 42

def read_file(filename):   
    with open(filename, "r") as f:
        content = f.readlines()
        lst = []
        for row in content:
            row = row.rstrip('\n')
            lst.append(row)
        return lst

def init_table(n):
    table = []
    table += [''] * n
    return table

def HashTable(filename):
    data = read_file(filename)
    table = init_table(len(data))
    for ele in data:
        i = GenerateHash(ele)
        if table[i] == '':
            table[i] = ele
        elif type(table[i]) == list:
            table[i] = table[i] + [ele]
        else:
            table[i] = [table[i], ele]
    return table

def Find(SearchName):
    data = data_table
    i = GenerateHash(SearchName)
    string = ''
    if data[i] == SearchName:
        return (i, SearchName)
    elif SearchName in data[i]:
        for a in range(len(data[i])):
            if data[i][a] == SearchName:
                string = str(i) + '-' + str(a)
                return (string, SearchName)
    return 'NOT FOUND'

data_table = HashTable('NAMES.txt')

##print(data_table)
print(data_table[:5])
print(Find('CHIA YEE JEY'))
print(Find('DINIE ZIKRY B RUDI'))
print(Find('ABRAHAM TEOW LIANG THYE'))
print(Find('ONG YI ZHEN JUSTINA'))
print(Find('JAMES BOND'))
