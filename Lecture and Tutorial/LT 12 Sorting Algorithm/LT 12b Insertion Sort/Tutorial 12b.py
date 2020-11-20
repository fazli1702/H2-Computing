#question 1
def get_age(tup):
    return tup[1]

def shift(lst):
    a = -1
    counter = 0
    for i in range(2, len(lst)+1):
        if get_age(lst[a]) <= get_age(lst[-i]):
            break
        else:
            lst[a], lst[-i] = lst[-i], lst[a]
            a -= 1
        counter += 1
    #print('shift counter:', counter)
    return lst


def sort_age_i(lst):               #correct
    counter = 0
    for i in range(1, len(lst)):
        insert = lst[i]
        j = i - 1
        while j >= 0:
            if get_age(lst[j]) < get_age(insert):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                j -= 1
                counter += 1
            else:
                counter += 1
                break
    return lst, counter



#counter sucks

def sort_age_i1(lst):
    counter = 0
    for i in range(1, len(lst)):
        if get_age(lst[i]) > get_age(lst[i-1]):
            lst = shift(lst[:i+1]) + lst[i+1:]
        counter += 1
    #print('counter:', counter)
    return lst

def get_age(tup):
    return tup[1]

def sort_age_i2(lst):
    counter = 0
    for i in range(1, len(lst)):
        insert = lst[i]
        j = i - 1
        counter += 1
        while lst[j] < insert and j >= 0:
            lst[j+1], lst[j] = lst[j], lst[j+1]
            j -= 1
            counter += 1
    return lst, counter


def sort_age_i3(lst):
    counter = 0
    for i in range(1, len(lst)):
        insert = lst[i]
        for j in range(i-1, 0, -1):
            if lst[j] > insert:
                lst[j+1] = lst[j]
                counter += 1
            else:
                lst[j+1] = insert
                counter += 1
                break
    return lst, counter



                       
        
seq_1 = [23, 19, 30]
seq_2 = [18, 23, 19, 30]
seq_3 = [18, 23, 19, 30, 17]
seq_4 = [35, 18, 23, 19, 30, 17]
##print(insertion_sort(seq_1))
##print(insertion_sort(seq_2))
##print(insertion_sort(seq_3))
##print(insertion_sort(seq_4))


        
seq1=[("M", 23), ("F", 19), ("M", 30)]
seq2=[("F", 18), ("M", 23), ("F", 19), ("M", 30)]
seq3=[("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq4=[("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]

print(sort_age_i(seq1))
print(sort_age_i(seq2))
print(sort_age_i([("F", 19)]))
