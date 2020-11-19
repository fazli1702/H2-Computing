#qustion 3
def foo(n):
    if n == 0:
        return 0
    else:
        return 2 * n + foo(n - 1)
    
##print(foo(5) == 30)


#question 4
def bar(n):
    if n < 3:
        return n + 1
    else:
        return bar(n - 3) + bar(n - 2) + bar(n - 1)

##print(bar(4) == 11)


#question 6
def f(n):
    if n < 3:
        return n
    else:
        return f(n-1) + 2*f(n-2) + 3*f(n-3)

##print(f(4) == 11)
##print(f(-1) == -1)
##print(f(20) == 10771211)



#question 7
def conway(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return conway(conway(n-1)) + conway(n-conway(n-1))

##print(conway(1))    
##print(conway(2))    
##print(conway(6))


#question 8
def recursive_sum(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    elif n % 2 == 0:
        return recursive_sum(n-1) + recursive_sum(n-2) + recursive_sum(n-3)
    else:
        return recursive_sum(n-1) + recursive_sum(n-2)

print(recursive_sum(2) == 1)
print(recursive_sum(3) == 2)
print(recursive_sum(6) == 12)
        



    
