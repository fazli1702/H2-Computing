#question 6
# Run  the following codes to import the data from psi.csv 
# into the list data

data = []

import csv
file=open('psi.csv')
lines=csv.reader(file)
for i in lines:
    data.append(tuple(i))
    
##print(data)    # run this code to see the data


#Task 5.1

def get_PSI(reading):     
    return int(reading[2])
    
#Task 5.2

def smallest_index(seq):
    minim = seq[0]
    index = 0
    for i in range(1, len(seq)):
        if get_PSI(minim) > get_PSI(seq[i]):
            minim = seq[i]
            index = i
    return index

def selection_sort(seq):
    minim_i = 0
    for i in range(len(seq)-1):
        minim_i = smallest_index(seq[i:]) + i
        if i != minim_i:
            seq[i], seq[minim_i] = seq[minim_i], seq[i]
    return seq

    


#Task 5.3
import math

def median(lst):
    med = (len(lst) + 1) / 2
    if len(lst) % 2 == 0:
        a = len(lst) // 2
        b = (len(lst) // 2) + 1
        return math.ceil((get_PSI(lst[a]) + get_PSI(lst[b])) / 2)
    else:
        return get_PSI(lst[med])
        

    
print(selection_sort(data))
print(median(data))
