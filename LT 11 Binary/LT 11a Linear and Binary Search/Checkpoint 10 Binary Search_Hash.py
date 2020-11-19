#question 1
def find_letter(char, string):
    l = 0
    h = len(string) -1
    lst = []
    while l <= h:
        m = (h + l) // 2
        lst += string[m]
        if string[m] == char:
            return lst
        elif char < string[m]:
            h = m - 1
        else:
            l = m + 1
    return lst



##print(find_letter("e", sorted("atmospheric")))
##print(find_letter("i", sorted("productively")))
##print(find_letter("t", sorted("troublemaking")))
##print(find_letter("d", sorted("personality")))








#question 2
def checksum(s):
    total = 0
    for i in range(len(s)):
        total += ord(s[i]) * (i + 1)
    return total % 10

##print(checksum('linda'))
##print(checksum('aaron'))
        





#question 3
def hash_function(string):
    return checksum(string)

def init_table(n):
    table = []
    table = [''] * n
    return table

def hash_table(seq):
    table = init_table(20)
    for ele in seq:
        i = hash_function(ele)
        print('i:', i)
        if table[i] == '':
            table[i] = ele
    return table


name_lst1 = ['linda', 'aaron', 'rick', 'caleb', 'jane', 'nancy', 'john','annie']

##print(hash_table(name_lst1))







#question 4
def search(seq, item):
    i = hash_function(item)
    if seq[i] == item:
        return i
    return None

##print(search(name_table1, 'jess'))
##print(search(name_table1, 'aaron'))






#question 5
def openhash(table, i, ele):
    while True:
        if table[i] == '':
            table[i] = ele
            return table
        else:
            i = (i + 1) % len(table)

def hash_table(seq):
    table = init_table(20)
    for ele in seq:
        i = hash_function(ele)
        if table[i] == '':
            table[i] = ele
        else:
            openhash(table, i, ele)
    return table

name_lst2 = ['linda', 'aaron', 'rick', 'caleb', 'noel', 'paul', 'jane', 'nancy', 'john', 'annie', 'april', 'cindy']

##print(hash_table(name_lst2))







#question 6
def linear_search(table, item, i):
    for ele in table:
        if table[i] == item:
            return i
        else:
            i = (i + 1) % len(table)

def search(seq, item):
    i = hash_function(item)
    if seq[i] == item:
        return i
    elif seq[i] == '':
        return None
    else:
        return linear_search(seq, item, i)


name_lst2 = ['linda', 'aaron', 'rick', 'caleb', 'noel', 'paul', 'jane', 'nancy', 'john', 'annie', 'april', 'cindy']
name_table2 = hash_table(name_lst2)


##print(search(name_table2, 'jess'))
##print(search(name_table2, 'annie'))
##print(search(name_table2, 'paul'))
