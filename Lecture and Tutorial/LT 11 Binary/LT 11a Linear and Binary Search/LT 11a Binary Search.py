#iteration
def binary_search_iter(seq, key):
    h = len(seq) - 1
    l = 0
    while l <= h:
        m = (l+h) // 2
        if key == seq[m]:
            return True
        elif key < seq[m]:       #LHS
            h = m - 1
        else:                    #RHS
            l = m + 1
    return False


lst = [5,9,12,18,25,34,85,100,123,345]

##print(binary_search(lst, 11))
##print(binary_search(lst, 123))
##print(binary_search(sorted('singapore'),'p'))








#recursion
def find(seq, l, h, key):
    if l > h:
        return False
    else:
        m = (l + h) // 2
        if seq[m] == key:
            return True
        elif key < seq[m]:        #LHS
            return find(seq, l, m-1, key)
        else:                     #RHS
            return find(seq, m+1, h, key)


def binary_search(seq, value):
    l = 0
    h = len(seq) - 1
    return find(seq, l, h, value)



print(binary_search(lst, 11))
print(binary_search(lst, 123))
print(binary_search(sorted('singapore'),'p'))  
    
