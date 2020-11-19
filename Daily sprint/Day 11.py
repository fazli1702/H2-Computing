def lstTriplet(n):
    for i in range(1,n):
        for j in range(1,n):
            if (i**2) + (j**2) == (n**2):
                return [i, j, n]
    return 'No such triplet exist given this value of n.'

print(lstTriplet(10))
print(lstTriplet(100))
print(lstTriplet(8))
