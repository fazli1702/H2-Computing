#question 1
def QuickSort1(Scores):
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
    
    while not Done:
        while LeftMark <= RightMark and Scores[LeftMark] <= PivotValue:
           LeftMark = LeftMark + 1
           
        while Scores[RightMark] >= PivotValue and RightMark >= LeftMark:
            RightMark = RightMark - 1
            
        if RightMark < LeftMark:
            Done = True
            
        else:
            Temp = Scores[LeftMark]
            Scores[LeftMark] = Scores[RightMark]
            Scores[RightMark] = Temp
            
    Scores[First], Scores[RightMark] = Scores[RightMark], Scores[First]
    
    return RightMark



print(QuickSort1([7, 5, 9, 3, 6]))
    


#question 2
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
    PivotValue = Scores[Last]
    LeftMark = First 
    RightMark = Last - 1
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
            
    Scores[Last], Scores[LeftMark] = Scores[LeftMark], Scores[Last]
    
    return LeftMark



##print(QuickSort([7, 1, 5, 4, 9, 8, 3, 2, 6]))






#question 3
def quicksort(seq, start, end):
    if start < end:
        partition = Partition(seq, start, end)
        quicksort(seq, start, partition - 1)
        quicksort(seq, partition + 1, end)



    
lst = [7,2,5,1,29,6,4,19,11]

##print(quicksort(lst, 0, len(lst) - 1))                                                                   
    
    
