#question 1
def get_age(tup):
    return tup[1]

def biggest_index(lst):
    maxim = get_age(lst[0])
    maxim_i = 0
    counter = 0
    for i in range(len(lst)):
        if get_age(lst[i]) > maxim:
            maxim  = get_age(lst[i])
            maxim_i = i
        counter += 1
    return maxim_i

def sort_age_s(lst):
    counter = 0 
    for i in range(len(lst)-1):
        print('i:', i)
        print('lst[i]:', lst[i])
        for j in range(i+1, len(lst)):
            print('j:', j)
            print('lst[j]:', lst[j])
            print('comparing lst[i]=', lst[i], 'and lst[j]=', lst[j])
            if get_age(lst[i]) < get_age(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
            counter += 1
    print('counter:', counter)
    return lst
            
        


seq1=[("M", 23), ("F", 19), ("M", 30)]
seq2=[("F", 18), ("M", 23), ("F", 19), ("M", 30)]
seq3=[("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq4=[("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]


print(sort_age_s(seq1))
##print(sort_age_s(seq2))
##print(sort_age_s(seq3))
##print(sort_age_s(seq4))
