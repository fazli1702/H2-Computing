#question 1
def average(values):
    return sum(values) / len(values)

##print(average((1, 2, 3)))
##print(average((-3, 2, 8, -1)))
    



#question 2
def max_and_min(values):
    maxim = values[0]
    minim = values[0]
    
    for i in range(len(values)):
        if maxim > values[i]:
            maxim = maxim 
        else:
            maxim = values[i]

    for i in range(len(values)):
        if minim < values[i]:
            minim = minim
        else:
            minim = values[i]
    return maxim, minim

##print(max_and_min((1, 2, 3, 4, 5)))



#question 3
def mid_point(coord_1, coord_2):
    return (coord_1[0] + coord_2[0]) / 2 , (coord_1[1] + coord_2[1]) / 2

##print(mid_point((1,1),(3,3)))



#question 4
def change_value_at_index(tup, i, value):
    #method 1
    if i >= len(tup):
        return tup
    else:
        tup = list(tup)
        tup[i] = value
        tup = tuple(tup)
        return tup


    #method 2
    if i >= len(tup):
        return tup
    elif i == 0:
        return (value,) + tup[1:]
    else:
        return tup[:i] + (value,) + tup[i+1:]
    

##print(change_value_at_index((1, 2, 3), 1, -1))



#question 5
def even_rank(tup):
    total = ()
    for i in range(1,len(tup),2):
        total += (tup[i],)
    return total

##print(even_rank(('a', 'v', 'b', 'w', 'c', 'x', 'd', 'y', 'e', 'z')))




#question 6
def odd_even_sums(tup):
    tup_even = ()
    tup_odd = ()

    sum_even = 0
    sum_odd = 0
    
    for i in range(0,len(tup),2):
        tup_even += (tup[i],)
        sum_even = sum(tup_even)
        continue
    
    for i in range(1,len(tup),2): 
        tup_odd += (tup[i],)
        sum_odd = sum(tup_odd)
        continue
        
    return (sum_even, sum_odd)

##print(odd_even_sums ((1, 3, 2, 4, 5)))
##print(odd_even_sums ((1, )))
##print(odd_even_sums (()))



#question 7
def contains(obj, tup):
    for i in range(len(tup)):
        if obj is tup[i]:
            return True
    return False
    

#question 8
#method 1
def copy_tuple1(tup):
    new_tup = ()
    for i in range(len(tup)):
        new_tup += (tup[i],)
    return new_tup

#method 2
def copy_tuple2(tup):
    new_tup = ()
    for ele in tup:
        new_tup += (ele,)
    return new_tup

a = (1,2,3,4,5)
##print(copy_tuple(a))




        
