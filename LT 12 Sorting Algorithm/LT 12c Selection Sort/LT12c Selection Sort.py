#question 3
def smallest(seq):
    minim = seq[0]
    for i in range(1, len(seq)):
        if minim > seq[i]:
            minim = seq[i]
    return minim

##print(smallest([3,5,2,6,4]))
##print(smallest(['john', 'annie', 'peter', 'siti']))
        


#question 4
def smallest_index(seq):
    minim = seq[0]
    index = 0
    for i in range(1, len(seq)):
        if minim > seq[i]:
            minim = seq[i]
            index = i
    return index

##print(smallest_index([3,5,2,6,4]))
##print(smallest_index(['john', 'annie', 'peter', 'siti']))





#question 5
def swap_smallest(seq):
    minim = smallest(seq)
    minim_i = smallest_index(seq)
    seq[0], seq[minim_i] = seq[minim_i], seq[0]
    return seq
    
seq1= [3,5,2,6,4]
seq2=['john', 'annie', 'peter', 'siti']
##print(swap_smallest(seq1))
##print(swap_smallest(seq2))




#question 6
def selection_sort(seq):
    minim_i = 0
    for i in range(len(seq)-1):
        minim_i = smallest_index(seq[i:]) + i
        if i != minim_i:
            seq[i], seq[minim_i] = seq[minim_i], seq[i]
    return seq
        
        
        
print(selection_sort(seq1))
print(selection_sort(seq2))
