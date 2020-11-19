#question 1
def swap_two(lst):
    if lst[0] > lst[1]:
        lst[0], lst[1] = lst[1], lst[0]
    return lst

##print(swap_two([3, 5]))
##print(swap_two([5, 3]))
##print(swap_two(['computing', 'chemistry']))




#question 2
def shift(lst):
    a = -1
    for i in range(2, len(lst)+1):
        if lst[a] >= lst[-i]:
            break
        else:
            lst[a], lst[-i] = lst[-i], lst[a]
            a -= 1
    return lst






##print(shift([1,3,7,8,9]))
print(shift([1,3,5,7,8,4]))
##print(shift([3,5,7,8,1]))
##print(shift(['ab','ad','am','ap','az','ak']))
        







#question 3
def insertion_sort(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            lst = shift(lst[:i+1]) + lst[i+1:]
    return lst

##print(insertion_sort([7,1,3,5,8,4]))
        
