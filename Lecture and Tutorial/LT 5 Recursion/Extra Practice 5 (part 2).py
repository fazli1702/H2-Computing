def choose(n,r):
    if n == 0 or r == 0 or n == 1:
        return 1
    elif n == r:
        return 1
    else:
        return choose(n-1,r-1) + choose(n-1,r)


##print(choose(4,2))
##print(choose(5,0))
##print(choose(6,6))
##print(choose(7,4))
##print(choose(18,8))
