#question 1
h1 = {'A':10, 'B':8.75, 'C':7.5, 'D':6.25, 'E':5, 'S':2.5, 'U':0}
h2 = {'A':20, 'B':17.5, 'C':15, 'D':12.5, 'E':10, 'S':5, 'U':0}

John = {'H1 GP' : 'C',  'H1 PW' : 'B',  'H1 Geo' :  'D',  'H2 Math' : 'A', 'H2 CP' : 'B', 'H2 Chem' : 'C'}
Mary =  {'H1 GP' : 'E',  'H1 PW' : 'B',  'H1 Geo' :  'C',  'H2 Math' : 'B', 'H2 Phy' : 'D', 'H2 CP' : 'C'}


def rankpoint(result):
    total = 0
    for key in result.keys():
        if key[:2] == 'H1':
            total += h1[result[key]]
        else:
            total += h2[result[key]]
    return total
            

##print(rankpoint(John))
##print(rankpoint(Mary))








#question 2
def replace(src, dest):
    new_dict = {}
    for i in range(len(src)):
        new_dict[src[i]] = dest[i]
    return new_dict

##print(replace('dikn', 'lvei'))





#question 3
def translate(src, dest, string):
    new_str = ''
    new_dict = replace(src, dest)
    lst = []
    lst.extend(string)
    for ele in lst:
        for key in new_dict.keys():
            if ele == key:
                lst[lst.index(ele)] = new_dict[key]
            else:
                continue
    
    for ele in lst:
        new_str += ele
    return new_str
        
                
                
##print(translate("dikn", "lvei", "My tutor IS kind"))
##print(translate("(hrd", ")esy", "CODING is hard :("))
##print(translate(" ", " ", "Python is awesome!!!"))





#question 4
def encrypt_cap(shift):
    if shift >= 26:
        shift = shift % 26
    src = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dest = src[shift:] + src[:shift]
    return replace(src, dest)

##print(encrypt_cap(3))


def encrypt_small(shift):
    if shift >= 26:
        shift = shift % 26
    src  = 'abcdefghijklmnopqrstuvwxyz'
    dest = src[shift:] + src[:shift]
    return replace(src, dest)

##print(encrypt_small(3))







#question 5
def caesar_cipher(shift, string):
    
    cap_dict = encrypt_cap(shift)
    small_dict = encrypt_small(shift)
    lst = []
    lst.extend(string)
    new_str = ''

    for ele in lst:
        for key in cap_dict.keys():
            if ele == key:
                lst[lst.index(ele)] = cap_dict[key]
            else:
                continue

    for ele in lst:
        for key in small_dict.keys():
            if ele == key:
                lst[lst.index(ele)] = small_dict[key]
            else:
                continue

    for ele in lst:
        new_str += ele
    return new_str

##print(caesar_cipher(10,"abcd"))
##print(caesar_cipher(25,"aAbB"))
##print(caesar_cipher(25,""))
        

    
                
                

    
