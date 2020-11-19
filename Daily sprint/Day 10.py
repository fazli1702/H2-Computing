def isTriplet(n):
    for i in range(1,n):
        for j in range(1,n):
            if (i**2) + (j**2) == (n**2):
                return True
    return False


print(isTriplet(5))
print(isTriplet(13))
print(isTriplet(4))
print(isTriplet(10))
