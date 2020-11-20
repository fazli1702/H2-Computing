#question 1
def get_age(tup):
    return tup[1]

def merge(left, right):
    lst = []
    while len(left) != 0 and len(right) != 0:
        if get_age(left[0]) < get_age(right[0]):
            lst.append(right.pop(0))
        else:
            lst.append(left.pop(0))
    if len(left) != 0:
        lst += left
    else:
        lst += right
    return lst

def sort_age_m(seq):
    if len(seq) == 1:
        return seq
    mid = len(seq) // 2
    l = seq[:mid]
    r = seq[mid:]
    return merge(sort_age_m(l), sort_age_m(r))


seq1=[("M", 23), ("F", 19), ("M", 30)]
seq2=[("F", 18), ("M", 23), ("F", 19), ("M", 30)]
seq3=[("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq4=[("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]

##print(sort_age_m(seq1))
##print(sort_age_m(seq2))
##print(sort_age_m([("F", 19)]))






#question 2
def merge_lists(list1, list2):
    #print('list1:', list1, 'list2:', list2)
    merged_list = []
    i = 0

    while True:
        if len(list1) == 0 or len(list2) == 0:
            break
        elif list1[i] > list2[i]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
        #print('list1:', list1, 'list2:', list2)
        #print('merged_list:', merged_list)

    if len(list2) != 0:
        for i in range(len(list2)):
            merged_list.append(list2.pop(0))

    else:
        for i in range(len(list1)):
            merged_list.append(list1.pop(0))
        
    return merged_list



##print(merge_lists([4, 2, 1], [6, 5, 3]))
##print(merge_lists([6, 4, 2, 1], [5, 3]))
##print(merge_lists([6, 5, 4, 2, 1], []))
##print(merge_lists([6, 5, 4, -1], [-2, -3]))
