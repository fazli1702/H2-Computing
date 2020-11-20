##### BUBBLE SORT #####

### normal ###
def bubble_sort(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            counter += 1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print('counter:', counter)
    return lst


def bubble_sort2(lst):
    i = 0
    end = len(lst) - 1
    counter = 0
    while end != 0:
        if lst[i] > lst[i+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
        i = (i+1) % end
        if i == 0:
            end -= 1
        counter += 1
    print('counter:', counter)
    return lst


def bubble_sort3(lst):
    counter = 0 
    end = len(lst)-1
    for i in range(len(lst)):
        for j in range(len(lst[:end])):
            counter += 1
            if lst[i] > lst[i+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        end -= 1
    print('counter:', counter)
    return lst
            
    
        
            
            


### optimised ###
def op_bubble_sort(lst):
    counter = 0
    end = len(lst)-1
    for i in range(len(lst)):
        flag = False
        for j in range(len(lst[:end])):
            counter += 1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag = True
        if flag == False:
            print('counter:', counter)
            return lst
            
        
seq1= [23, 12]
seq2= [23, 12, 8]
seq3= [23, 12, 8,14,17,11,19]            

##print(seq1)
##print(bubble_sort(seq1))
##print(bubble_sort2(seq1))
##print(bubble_sort3(seq1)) 
##print(op_bubble_sort(seq1))
##print()
##print(seq2)
##print(bubble_sort(seq2))
##print(bubble_sort2(seq2))
##print(bubble_sort3(seq2)) 
##print(op_bubble_sort(seq2))
##print()
print(seq3)
##print(bubble_sort(seq3))
##print(bubble_sort2(seq3))
##print(bubble_sort3(seq3)) 
print(op_bubble_sort(seq3))








#########################################################################
#########################################################################


##### INSERTION SORT #####

def insertion_sort(lst):
    counter = 0
    for i in range(1, len(lst)):
        j = i - 1
        while j >= 0:
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                j -= 1
                counter += 1
            else:
                counter += 1
                break
    print('counter:', counter)
    return lst

##print(insertion_sort(seq3))





#########################################################################
#########################################################################


##### SELECTION SORT #####

def selection_sort(lst):
    minim_i = 0
    for i in range(len(lst)-1):
        minim_i = smallest(lst[i:]) + i
        if minim_i != i:
            lst[minim_i], lst[i] = lst[i], lst[minim_i]
    return lst

def smallest(lst):
    smallest = lst[0]
    si = 0
    for i in range(len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            si = i
    return si


def selection_sort2(lst):
    counter = 0 
    for i in range(len(lst)-1):
        #print('i:', i)
        #print('lst[i]:', lst[i])
        for j in range(i+1, len(lst)):
            #print('j:', j)
            #print('lst[j]:', lst[j])
            #print('comparing lst[i]=', lst[i], 'and lst[j]=', lst[j])
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
            counter += 1
    print('counter:', counter)
    return lst
            
            
            
        
##print(seq3)
##print(selection_sort(seq3))
##print(selection_sort2(seq3))


        

#########################################################################
#########################################################################


##### MERGE SORT #####

def merge_sort(seq):
    if len(seq) == 1:
        return seq
    mid = len(seq) // 2
    l = seq[:mid]
    r = seq[mid:]
    return merge(merge_sort(l), merge_sort(r))

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

##print(merge_sort(seq3))



#########################################################################
#########################################################################


##### QUICKSORT SORT #####

def QuickSort(Scores):
    QuickSortHelper(Scores, 0, len(Scores)-1)
    return Scores

def QuickSortHelper(Scores, First, Last):
    if First < Last:
        SplitPoint = Partition(Scores, First, Last)
        QuickSortHelper(Scores, First, SplitPoint - 1)
        QuickSortHelper(Scores, SplitPoint + 1, Last)
    return Scores

def Partition(Scores, First, Last):
    PivotValue = Scores[First]
    LeftMark = First + 1
    RightMark = Last
    Done = False
    while Done == False:
        while LeftMark <= RightMark and Scores[LeftMark] <= PivotValue:
           LeftMark = LeftMark + 1
        while Scores[RightMark] >= PivotValue and RightMark >= LeftMark:
            RightMark = RightMark - 1
        if RightMark < LeftMark:
            Done = True
        else:
            Scores[LeftMark], Scores[RightMark] = Scores[RightMark], Scores[LeftMark]
            #Temp = Scores[LeftMark]
            #Scores[LeftMark] = Scores[RightMark]
            #Scores[RightMark] = Temp
    Scores[First], Scores[RightMark] = Scores[RightMark], Scores[First]
    return RightMark
