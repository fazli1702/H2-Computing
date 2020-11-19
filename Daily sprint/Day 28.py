def is_ap(seq):
    a = seq[0]
    print('a:',a)
    d = seq[1] - a
    print('d:',d)
    lst = [a]
    for i in range(len(seq)-1):
        lst.append((lst[-1] + d))
    print(lst)
    return lst == seq


print(is_ap([1,2,4,8,16,32]))
print(is_ap([-1,-5,-9,-13,-17]))
