def size(n):
    if n == 0:
        return 0
    else:
        total = n
        counter = 0
        while True:
            total /= 10
            counter += 1
            if total < 1:
                return counter
            else:
                continue



def digitlst(n):
    if n == 0:
        return []
    else:
        x = str(n)
        lst = []
        for ele in x:
            lst.append(int(ele))
        lst.sort()
        return lst[::-1]



def pandigital(n):
    lst = digitlst(n)
    lst1 = list(range(1, size(n)))
    for ele in lst1:
        if ele not in lst:
            return False
        elif lst.count(n) > 1:
            return False
    return True
            

print(pandigital(135792468))
print(pandigital(132))
print(pandigital(1))
print(pandigital(2234))
print(pandigital(2345))

    
