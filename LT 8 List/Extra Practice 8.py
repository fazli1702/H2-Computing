#question 1
def at_least_n_1(lst,n):
    for i in range(len(lst)):
        if lst[i]<n:
            lst.remove(lst[i])
    return lst

##print(at_least_n_1([1,2,3,4,5,6,7,8,9],4))








#question 2
def at_least_n_2(lst,n):
    for i in lst:
        if i < n:
            lst.remove(i)
    return lst

##print(at_least_n_2([1,2,3,4,5,6,7,8,9],4))











#question 3
def at_least_n_mutated(lst, n):
    i = 0
    while i < len(lst):
        if lst[i] >= n:
            i += 1
        else:
            lst.pop(i)
            i = 0
    return lst

lst1 = list(range(10))  
lst2 = list(range(8))
lst3 = list(range(6,10))

##print(at_least_n_mutated(lst1, 5))
##print(at_least_n_mutated(lst2, 8))











#question 4
def at_least_n(lst, n):
    new_lst = []
    for ele in lst:
        if ele >= n:
            new_lst += [ele]
        else:
            continue
    return new_lst

##print(at_least_n(lst1, 5))
##print(at_least_n(lst2, 8))











#question 5
def col_sum(mat):
    new_lst = []
    col = 0
    for i in range(len(mat[0])):
        for ele in mat:
            col += ele[i]
        new_lst += [col]
        col = 0
    return new_lst


##print(col_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
##print(col_sum([[ 1, 2, 3], [4, 5, 6], [7, 8, 9]]))












#question 6
def row_sum(mat):
    new_lst = []
    for ele in mat:
        new_lst += [sum(ele)]
    return new_lst


##print(row_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
##print(row_sum([[ 1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        
        



        
