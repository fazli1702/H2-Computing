# Checkpoint 6 - Tuples and Lists

#Q1 Reverse the elements in a Tuple
def reverse(tup):
    newtup = ()
    for i in range(len(tup)):
        if tup == '':
            return newtup
        else:
            newtup += (tup[-1],)
            tup = (tup[:-1])
    return newtup


# Test Cases :
##print(reverse(("a","b","c","d","e"))==("e","d","c","b","a"))
##print(reverse((1,2,3,4,5))==(5,4,3,2,1))


#Q2 Oddify (Part 1)
def oddify_not_mutated(lst):
    newlst = []
    for ele in lst:
        if ele % 2 == 1:
            newlst += [ele]
        else:
            continue
    return newlst


# Test Cases :
##print(oddify([1, 2, 3, 4, 5])==[1, 3, 5])
##print(oddify([-1, 0, 2, 3])==[-1,3])
##print(oddify([2,4,6])==[])




#Q3 Oddify (Part 2)
def oddify(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 1:
            i += 1
        else:
            lst.pop(i)
    return lst


# Test Cases :
##print(oddify([1, 2, 3, 4, 5])==[1, 3, 5])
##print(oddify([-1, 0, 2, 3])==[-1,3])
##print(oddify([2,4,6])==[])






#bonus
def split(string):
    lst = []
    new_str = ''
    i = 0

    if len(string) == 0:
        return []

    for ele in string:
        if ele == ' ':
            continue
        else:
            new_str += ele

    while i < len(new_str):
        if new_str[i] == ',':
            lst += [new_str[:i]]
            new_str = new_str[i+1:]
            i = 0
        else:
            i += 1

    lst += [new_str]
    return lst
    
   
string = '1,2,3,4'
print(split(string))
