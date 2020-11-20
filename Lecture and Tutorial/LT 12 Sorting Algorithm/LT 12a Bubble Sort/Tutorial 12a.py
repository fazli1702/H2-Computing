#question 1
def get_age(tup):
    return tup[1]

def sort_age(lst):
    i = 0
    end = len(lst) - 1
    counter = 0
    while end!= 0:
        if get_age(lst[i]) < get_age(lst[i+1]):
            lst[i], lst[i+1] = lst[i+1], lst[i]
        i = (i+1) % end
        counter += 1
        if i == 0:
            end -= 1
    #print('counter:', counter)
    return lst

seq1=[("M", 23), ("F", 19), ("M", 30)]
seq2=[("F", 18), ("M", 23), ("F", 19), ("M", 30)]
seq3=[("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq4=[("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq5=[("M", 35), ("F", 30), ("M", 23), ("F", 19), ("M", 23), ("M", 17)]




##print(sort_age(seq1))
##print(sort_age(seq2))
##print(sort_age(seq3))
##print(sort_age(seq4))
##print(sort_age(seq5))



#question 3
def op_sort_age(lst):
    end = len(lst) - 1
    counter = 0
    while end != 0:
        swapped = False
        check = [False, 0]
        for i in range(len(lst[:end])):
            if get_age(lst[i]) < get_age(lst[i+1]):
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped, check[0] = True, True
            else:
                if check[0] == True:
                    check = [False, i]
            counter += 1
        if swapped == False:
            break
        elif not (check[0]):
            end = check[1]
        else:
            end -= 1
    #print('counter:', counter)
    return lst



seq1=[("M", 23), ("F", 19), ("M", 30)]
seq2=[("F", 18), ("M", 23), ("F", 19), ("M", 30)]
seq3=[("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq4=[("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq5=[("M", 35), ("F", 30), ("M", 23), ("F", 19), ("M", 18), ("M", 17)]



##print(op_sort_age(seq1))
##print(op_sort_age(seq2))
##print(op_sort_age(seq5))
