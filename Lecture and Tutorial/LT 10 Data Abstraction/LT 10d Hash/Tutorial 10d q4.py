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

##print(read_file('NAMES.txt'))

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
##print(Find('MANSIB MIRAJ'))
print(data_table[:5])
print(Find('CHIA YEE JEY'))
print(Find('DINIE ZIKRY B RUDI'))
print(Find('ABRAHAM TEOW LIANG THYE'))
print(Find('ONG YI ZHEN JUSTINA'))
print(Find('JAMES BOND'))
