    #question 4
seq1= [23, 12]
##swap the first two adjacent elements
###your swapping code here:
a = seq1[0]
b = seq1[1]
seq1[0] = b
seq1[1] = a

##print(seq1)


###Do not remove/modify
seq2= [23, 12, 8]
###swap the second two adjacent elements
###your swapping code here:
c = seq2[1]
d = seq2[2]
seq2[1] = d
seq2[2] = c

##print(seq2)




###Do not remove/modify
lst = [0,1,2,3,4,5,6,7,8]
###swap the third two adjacent elements
###your swapping code here:
e = lst[2]
f = lst[3]
lst[2] = f
lst[3] = e

##print(lst)



###Do not remove/modify
a=['a','b','c','d','e','f','g']
###swap the fourth two adjacent elements
###your swapping code here:
g = a[3]
h = a[4]
a[3] = h
a[4] = g

##print(a)







#question 5
def single_pass(seq):
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            seq[i] , seq[i+1] = seq[i+1] , seq[i]
    return seq
        
        
seq1 = [23, 12]        
seq2 = [23, 12, 8]
seq3 = [23, 12, 8, 14, 17, 11, 19]

##print(single_pass(seq1))
##print(single_pass(seq2))
##print(single_pass(seq3))







#question 6
def bubble_sort(seq):
    i = 0
    end = len(seq) - 1
    counter = 0
    while end != 0:
        if seq[i] > seq[i+1]:
            seq[i] , seq[i+1] = seq[i+1] , seq[i]
        i = (i+1) % end
        if i == 0:
            end -= 1
        counter += 1
    print('counter:', counter)
    return seq    
          


##print('seq1:', seq1)
##print('bubble_sort seq1:', bubble_sort(seq1))
##print('seq2:', seq2)
##print('bubble_sort seq2', bubble_sort(seq2))
##print('seq3:', seq3)
##print('bubble_sort seq3', bubble_sort(seq3))








#question 10
def optimized_bubble_sort1(seq):
    i = 0
    end = len(seq) - 1
    counter = 0
    swapped = False  
    while end != 0:
        if seq[i] > seq[i+1]:
            seq[i] , seq[i+1] = seq[i+1] , seq[i]
            swapped = True
        i = (i+1) % end
        counter += 1
        if i == 0:
            end -= 1
            if swapped == False:
                break
    print('optimized counter:', counter)
    return seq  




def optimized_bubble_sort(seq):
    end = len(seq) - 1
    counter = 0
    while end != 0:
        swapped = False
        check = [False, 0]
        for i in range(len(seq[:end])):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                swapped, check[0] = True, True
            else:
                if check[0] == True:
                    check = [False, i]
            counter += 1
        if not swapped:
            break
        elif not check[0]:
            end = check[1]
        else:
            end -= 1
    print('counter:', counter)
    return seq
    




##print('seq1:', seq1)
##print('bubble_sort seq1:', bubble_sort(seq1))
##print('optimized bubble sort seq1:', optimized_bubble_sort(seq1))
##print('seq2:', seq2)
##print('bubble_sort seq2', bubble_sort(seq2))
##print('optimized bubble sort seq2:', optimized_bubble_sort(seq2))
##print('seq3:', seq3)
##print('bubble_sort seq3', bubble_sort(seq3))
##print('optimized bubble sort seq3:', optimized_bubble_sort(seq3))

seq4 = [3, 2, 1, 5, 4, 8, 6, 9, 10, 11]
print('seq4:', seq4)
print('sort:', bubble_sort(seq4))
print('old optimized sort:', optimized_bubble_sort1(seq4))
print('optimized sort:', optimized_bubble_sort(seq4))




