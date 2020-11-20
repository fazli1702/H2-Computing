#task 3.1
def hash(string):
    total = 0
    for ele in string:
        total += ord(ele)
    return total % 13

#task 3.2
def init_table(n):
    table = []
    table += [''] * n
    return table

def hash_table(seq):
    table = init_table(13)
    for ele in seq:
        i = hash(ele)
        table[i] = ele
    return table


keys1 = ('onion','tomato','cabbage', 'okra','banana', 'salt','cucumber','mushroom', 'orange')
table1= hash_table(keys1)   

##print(hash('onion'))
##print(hash('tomato'))
##print(hash('cabbage'))
##print(hash_table(keys1))







#task 3.3
def hash_table(seq):
    table = init_table(len(seq))
    for ele in seq:
        i = hash(ele)
        if table[i] == '':
            table[i] = ele
        elif type(table[i]) == list:
            table[i] += [ele]
        else:
            table[i] = [table[i], ele]
    return table

#task 3.4
def search(seq, item):
    i = hash(item)
    if seq[i] == item:
        return True
    elif seq[i] == '':
        return False
    elif type(seq[i]) == list:
        for ele in seq[i]:
            if ele == item:
                return True
    return False


keys2 = ('onion','tomato','cabbage','carrot', 'okra','mellon','potato','banana', 'olive','salt',
         'cucumber','mushroom', 'orange')
table2 = hash_table(keys2)


##print(hash_table(keys2))
##print(search(table2, 'salt'))
##print(search(table2, 'stone'))
##print(search(table2, 'cake'))
