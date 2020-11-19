x=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843

def product(lst, n):
    total = 1
    for i in range(n):
        total *= int(lst[i])
    return total
    


def largestprod(string, n):
    maxim = 1
    a  = 1
    lst = []
    for ele in string:
        lst.append(int(ele))
    #print(lst)

    for i in range(n):
        maxim *= lst[i]
    #print(maxim)

    while len(lst) >= n:
        a = product(lst, n)
        if a > maxim:
            maxim = a
        lst.pop(0)
        a = 0
    return maxim
            
        



print(largestprod(str(x),11))
print(largestprod(str(x),5))
print(largestprod(str(x),25))
print(largestprod(str(x),70))
    



        
    
