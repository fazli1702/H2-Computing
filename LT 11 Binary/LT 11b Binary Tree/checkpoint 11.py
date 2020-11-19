from bst_module import *

def sort_it(lst):
    tree = make_empty_tree()
    for ele in lst:
        tree = insert_tree(ele, tree)
    return flatten(tree)

lst1= [5,3,2,1,4,6,7,9]
lst2=[5,3,2,1,4,-1,6,0,7,9]
##print(sort_it(lst1))
##print(sort_it(lst2))

def get_age(customer):
    return customer[3]

def sort_age(lst):
    end = len(lst) - 1
    for i in range(len(lst)):
        for j in range(len(lst[:end])):
            if get_age(lst[j]) > get_age(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
        end -= 1
    return lst
            
            



#####Do not remove/modify ###########
cust1=[ ("650001", "Henry Lim",  "M", 23) , ("650002", "Jane Chen", "F", 19),  ("650003", "Ahmad", "M", 30) ]
cust2=[("650004", "Dina", "F", 28), ("650001", "Henry Lim", "M", 23), ("650002", "Jane Chen", "F", 19), 
("650003", "Ahmad", "M", 30)]
sort_age(cust1)
sort_age(cust2)

##print(cust1)
##print(cust2)






def get_name(customer):
    return customer[1]

def sort_name(lst):
    for i in range(1, len(lst)):
        insert = get_name(lst[i])
        j = i - 1
        while get_name(lst[j]) > insert and j >= 0:
            lst[j+1], lst[j] = lst[j], lst[j+1]
            j -= 1
    return lst


cust1=[ ("650001", "Henry Lim",  "M", 23) , ("650002", "Jane Chen", "F", 19),  ("650003", "Ahmad", "M", 30) ]

cust2=[("650004", "Dina", "F", 28), ("650001", "Henry Lim", "M", 23), ("650002", "Jane Chen", "F", 19), 
("650003", "Ahmad", "M", 30)]

##print(sort_name(cust1))
##print(sort_name(cust2))

                


