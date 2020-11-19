def is_gp(seq):
    a = seq[0]
    #print('a:',a)
    r = seq[1] / a
    #print('r:',r)
    lst = [a]
    for i in range(len(seq)-1):
        lst.append((lst[-1] * r))
    #print(lst)
    return lst == seq


print(is_gp([1,2,4,8,16,32]))
print(is_gp([-1,-2,-4,-12,-16,-32]))
        
    
    
