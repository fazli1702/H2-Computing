seq1=[1,0.1,0.01,0.001,0.0001]
seq2=[1,2,4,8,16,32]
seq3=[2,4,6,8,10,12]

def is_gp(seq):
    a = seq[0]
    #print('a:',a)
    r = seq[1] / a
    #print('r:',r)
    lst = [a]
    for i in range(len(seq)-1):
        lst.append((round(lst[-1] * r, 5)))
    #print(lst)
    return lst == seq

##print(is_gp(seq1))

def inf(seq):
    a = seq[0]
    print('a:', a)
    r = seq[1] / a
    print('r:', r)
    
    if is_gp(seq) == False:
        return 'Sequence is not geometric'
    elif abs(r) > 1:
        return 'Sum to infinity does not exist'
    else:
        return round(a / (1-r), 10)

print(inf(seq1))
print(inf(seq2))
print(inf(seq3))
