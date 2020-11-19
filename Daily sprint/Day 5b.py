import math as m

def smallest(n):
    lst = list(range(1,  n+1))
    i = 1
    x = True
    while True:
        ans = n * i
        for ele in lst:
            if ans % ele != 0:
                x = False

        if x == True:
            return ans
        else:
            i += 1


print(smallest(10))
    
    
                
