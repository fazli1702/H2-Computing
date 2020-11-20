from random import randint

def MysSort(lst):
    while True:
        Swap = Helper(lst)
        if Swap == False:
            break
    return lst

def Helper(lst):
    Swap = False
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            r = randint(i+1, len(lst)-1)
            lst[i], lst[r] = lst[r], lst[i]
            Swap = True
            return Swap
    return Swap



a = [6, 5, 4, 3, 2, 1]
b = [1, 2, 5, 4, 6]
c = [1, 2, 3, 4, 5]

##print(MysSort(a))
##print(MysSort(b))
##print(MysSort(c))
print(MysSort([1,7,3,-4,20,9531,11,111]))
  
