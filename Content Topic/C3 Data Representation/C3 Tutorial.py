##question 1
def binary_to_denary(string):
    total = 0
    length = len(string)
    #print('length:', length)
    for i in range(length):
        power = length-i-1
        #print('power:', length-i-1)
        #print('bin:', string[i])
        total += (int(string[i]) * (2**(power)))
        #print('total:', total)
    return str(total)



##print(binary_to_denary('1000'))
##print(binary_to_denary('1010'))
##print(binary_to_denary('00001111'))
##print(binary_to_denary('11111111'))
##print(binary_to_denary('1011'))
    






##question 2
def denary_to_binary(string):
    binary = ''
    q = int(string)
    while True:
        binary += str(q % 2)
        q = q // 2
        if q == 0:
            return binary[::-1]


##print(denary_to_binary('246'))
##print(denary_to_binary('9'))
        











##question 3
def base_n_to_denary(string, n):
    total = 0
    length = len(string)
    for i in range(length):
        power = length - i - 1
        total += int(string[i]) * n**power
    return str(total)
    

##print(base_n_to_denary('1000', 2))
##print(base_n_to_denary('1000', 3))










##question 4
def denary_to_base_n(string, n):
    base_n = ''
    q = int(string)
    while True:
        r = q % n
        if q == 0:
            return base_n[::-1]
        else:
            base_n += str(r)
        q = q // n
        


##print(denary_to_base_n('11',2))
##print(denary_to_base_n('31',3))
##print(denary_to_base_n('521',8))
##print(denary_to_base_n('4113',16))







##question 5
##method 1
def hex_to_denary1(string):
    total = 0
    length = len(string)
    lst = []
    lst.extend(string)
    for i in range(len(string)):
        if lst[i] == 'A':
            lst[i] = 10
        elif lst[i] == 'B':
            lst[i] = 11
        elif lst[i] == 'C':
            lst[i] = 12
        elif lst[i] == 'D':
            lst[i] = 13
        elif lst[i] == 'E':
            lst[i] = 14
        elif lst[i] == 'F':
            lst[i] = 15
    
    for i in range(length):
        power = length - i - 1
        total += int(lst[i]) * 16**power
    return str(total)




##method 2
def hex_to_denary(string):
    total = 0
    i = 0
    dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    for ele in string:
        #print('ele:', ele)
        power = len(string) - 1 - i
        #print('power:', power)
        if ele in dic:
            total += dic[ele] * 16**power
        else:
            total += int(ele) * 16**power
        i += 1
    return str(total)






##print(hex_to_denary('64'))
##print(hex_to_denary('A8'))
##print(hex_to_denary('BABE'))
##print(hex_to_denary('CAFE'))








##question 6
##method 1
def denary_to_hex1(string):
    q = int(string)
    hexa = ''
    while True:
        r = q % 16
        #print('r:',r)
        if q == 0:
            return hexa[::-1]
        elif r == 10:
            hexa += 'A'
        elif r == 11:
            hexa += 'B'
        elif r == 12:
            hexa += 'C'
        elif r == 13:
            hexa += 'D'
        elif r == 14:
            hexa += 'E'
        elif r == 15:
            hexa += 'F'
        else:
            hexa += str(r)
        #print('hexa:', hexa)

        q = q // 16


##method 2
def denary_to_hex(string):
    hexa = ''
    dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    q = int(string)
    while q != 0:
        r = q % 16
        if r in dic:
            hexa += dic[r]
        else:
            hexa += str(r)
        q = q // 16
        

        
##print(denary_to_hex('51966'))
##print(denary_to_hex('2459'))









##question 7
from stack_module import*

def denary_to_binary(n):
    binary = make_empty_stack()
    string = ''
    while n != 0:
        r = n % 2
        n = n // 2
        push(binary, r)

    for i in range(size(binary)):
        string += str(pop(binary))
    return int(string)


    
print(denary_to_binary(123))
        
    
    
    
