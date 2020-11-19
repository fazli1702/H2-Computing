#question 1
def split_1(seq):
    if len(seq) == 1:
        return seq
    mid = len(seq) // 2
    l = seq[:mid]
    r = seq[mid:]
    return (l, r)

##print(split([5, 2, 1, 8, 9]))
##print(split([1]))
##print(split([1, 8, 9]))





#question 2
def split(seq):
    if len(seq) == 1:
        return seq
    mid = len(seq) // 2
    l = seq[:mid]
    r = seq[mid:]
    return (split(l), split(r))


##print(split([5, 2, 1, 8, 9]))
##print(split([1]))
##print(split([1, 8, 9]))

    



#question 4
def merge_1(left, right):
    if left < right:
        left += right
        return left
    else:
        right += left
        return right

##print(merge([8], [9]))
##print(merge([5], [2]))







#question 5
def merge_2(left, right):
    lst = []
    while len(left) != 0 and len(right) != 0:
        if left[0] > right[0]:
            lst.append(right.pop(0))
        else:
            lst.append(left.pop(0))
    if len(left) != 0:
        lst += left
    else:
        lst += right
    return lst


##print(merge([1], [8,9]))
##print(merge([8,9], [1]))





#question 6
def merge(left, right):
    lst = []
    while len(left) != 0 and len(right) != 0:
        if left[0] > right[0]:
            lst.append(right.pop(0))
        else:
            lst.append(left.pop(0))
    if len(left) != 0:
        lst += left
    else:
        lst += right
    return lst

##print(merge([2, 5],[1,8,9]))
##print(merge([2,6,7], [9,10]))






#question 7
def merge_sort(seq):
    if len(seq) == 1:
        return seq
    mid = len(seq) // 2
    l = seq[:mid]
    r = seq[mid:]
    return merge(merge_sort(l), merge_sort(r))
    


##print(merge_sort([5, 2, 1, 8, 9]))
##print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
