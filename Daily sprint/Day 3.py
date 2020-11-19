def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

        
def primeFactors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            if isPrime(i) == True:
                factors.append(i)
            else:
                continue
    return max(factors)
            


print(primeFactorsZ(13195))
print(primeFactors(20000))
