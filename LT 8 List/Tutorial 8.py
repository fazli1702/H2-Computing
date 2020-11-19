#question 1
def double_up(lst):
    new_list = []
    for ele in lst:
        new_list += [ele*2]
    return new_list
        

##print(double_up([1,2,3]))




#question 2
def double_up(lst):
    for i in range(len(lst)):
        lst[i] = lst[i]*2
    return lst

##print(double_up([1, 2, 3]))












#question 3
def count_strings(lst):
    counter = 0
    for i in range(len(lst)):
        if type(lst[i]) == str:
            counter += 1
    return counter


##print(count_strings([0, '1', 'two', 3, (4, 5)]))
##print(count_strings(['hello', True]))











#question 4
def remove_extras(lst):
    new_lst = []
    for ele in lst:
        if ele not in new_lst:
            new_lst += [ele]
    return new_lst
    
    


##print(remove_extras([1, 5, 1, 1, 3, 2]))
##print(remove_extras([1, 1, 1, 2, 3]))
##print(remove_extras([1, 2, 3]))
##print(remove_extras([1,1,2,2,3,3,4,4]))













#question 5
def remove_extra(lst):
    counter = 0
    while counter < len(lst):
        for ele in lst:
            if lst.count(ele) > 1:
                lst.pop(lst.index(ele))
        counter += 1
    return lst




##def remove_extra(lst):
##    i = 0
##    while i < len(lst) :
##        if lst[i] in lst[i+1:]:
##            del lst[i]
##        else:
##            continue
##            i += 1
##        
        
lst1 = [1, 5, 1, 1, 3]
lst2 = [2, 2, 2, 1, 5, 4, 4]
result1 = remove_extra(lst1)
result2 = remove_extra(lst2)
##print(result1)
##print(result2)

















#question 6
def top_k(lst, k):
    if k > len(lst):
        k = len(lst)
        return top_k(lst, k)
    elif k == 1:
        return [max(lst)]
    else:
        new_lst = []
        for i in range(k):
            new_lst += [max(lst)]
            lst.remove(max(lst))
        return new_lst
    
##print(top_k([4, 5, 2, 3, 1, 6], 3))
##print(top_k([4, 5, 2, 3, 1, 6], 6))
##print(top_k([9, 8, 4, 5, 7, 2, 3, 1, 6], 5))
##print(top_k([9, 9, 4, 9, 7, 9, 3, 1, 6], 5))
##print(top_k([9, 9, 4, 9, 7, 9, 3, 1, 6], 10))
    
    





    









#question 7
def count_occurrences(lst, num):
    if num == lst:
        return 1
    elif type(lst) != list or len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return count_occurrences(lst[0], num)
    else:
        return count_occurrences(lst[0], num) + count_occurrences(lst[1:], num)


##def count_occurences_2(lst, num):
##    counter = 0
##    for ele in lst:
##        if type(ele) == lst:
##            count_occurences_2(ele, num)
##        elif ele == num:
##            counter += 1:
##        else:
##            counter += 0
            
    



##print(count_occurrences([1, [2, 1], 1, [3, [1, 3]], [4, [1], 5], [1], 1, [[1]]], 3))


            
