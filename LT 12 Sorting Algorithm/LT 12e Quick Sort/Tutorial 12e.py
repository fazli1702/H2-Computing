#question 1
def get_age(tup):
    return tup[1]

def Partition(Scores, First, Last):
    PivotValue = get_age(Scores[Last])
    LeftMark = First
    RightMark = Last - 1
    Done = False

    while Done == False:
        while LeftMark <= RightMark and get_age(Scores[LeftMark]) >= PivotValue:
           LeftMark = LeftMark + 1

        while get_age(Scores[RightMark]) <= PivotValue and RightMark >= LeftMark:
            RightMark = RightMark - 1

        if RightMark < LeftMark:
            Done = True

        else:
            Scores[LeftMark], Scores[RightMark] = Scores[RightMark], Scores[LeftMark]

    Scores[Last], Scores[LeftMark] = Scores[LeftMark], Scores[Last]

    return LeftMark

def quicksort(seq, start, end):
    if start < end:
        partition = Partition(seq, start, end)
        quicksort(seq, start, partition - 1)
        quicksort(seq, partition + 1, end)
        return seq

def sort_age_q(lst):
    if len(lst) == 1:
        return lst
    return quicksort(lst, 0, len(lst) - 1)


seq1=[("M", 23), ("F", 19), ("M", 30)]
seq2=[("F", 18), ("M", 23), ("F", 19), ("M", 30)]
seq3=[("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq4=[("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]

##print(sort_age_q(seq1))
##print(sort_age_q(seq2))
##print(sort_age_q([("F", 19)]))










#question 2
def get_age(tup):
    return tup[1]

def get_gender(tup):
    return tup[0]



def Partition_gender(Scores, First, Last):
    PivotValue = get_gender(Scores[Last])
    LeftMark = First 
    RightMark = Last - 1
    Done = False
    
    if PivotValue == 'M':
        while Done == False:
            while LeftMark <= RightMark and get_gender(Scores[LeftMark]) == PivotValue:
                LeftMark = LeftMark + 1
           
            while get_gender(Scores[RightMark]) < PivotValue and RightMark >= LeftMark:
                RightMark = RightMark - 1
            
            if RightMark < LeftMark:
                Done = True
            
            else:
                Scores[LeftMark], Scores[RightMark] = Scores[RightMark], Scores[LeftMark]
            
        Scores[Last], Scores[LeftMark] = Scores[LeftMark], Scores[Last]
    
    else:
         while Done == False:
            while LeftMark <= RightMark and get_gender(Scores[LeftMark]) > PivotValue:
                LeftMark = LeftMark + 1
           
            while get_gender(Scores[RightMark]) == PivotValue and RightMark >= LeftMark:
                RightMark = RightMark - 1
            
            if RightMark < LeftMark:
                Done = True
            
            else:
                Scores[LeftMark], Scores[RightMark] = Scores[RightMark], Scores[LeftMark]
            
         Scores[Last], Scores[LeftMark] = Scores[LeftMark], Scores[Last]
        
    
    return LeftMark

def quicksort_gender(seq, start, end):
    partition = 0
    if start < end:
        partition = Partition_gender(seq, start, end)
        quicksort_gender(seq, start, partition - 1)
        quicksort_gender(seq, partition + 1, end)
    return partition

def quicksort_age(seq, partition):
    quicksort(seq, 0, partition)
    quicksort(seq, partition + 1, len(seq) - 1)
    return seq

        
def sort_by_gender_then_age(lst):
    if len(lst) == 1:
        return lst
    return quicksort_age(lst, quicksort_gender(lst, 0, len(lst) - 1))






seq1 = [("M", 23), ("F", 19), ("M", 30)]
seq2 = [("F", 18), ("M", 23), ("F", 19), ("M", 30)]
seq3 = [("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq4 = [("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]
seq5 = [("F", 9), ("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]


##print(sort_by_gender_then_age(seq1))
##print(sort_by_gender_then_age(seq2))
##print(sort_by_gender_then_age(seq3))
##print(sort_by_gender_then_age(seq4))
print(sort_by_gender_then_age(seq5))
##print(sort_by_gender_then_age([("F", 19)]))
