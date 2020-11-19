def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def sumPrime(n):
    total  = 0
    for i in range(2,n):
        if isPrime(i) == True:
            total += i
    return total


print(sumPrime(10))
print(sumPrime(100))
print(sumPrime(1000))
print(sumPrime(10000))
