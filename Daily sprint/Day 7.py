import math as m

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def nthPrime(n):
    prime = []
    i = 2
    while True:
        if len(prime) == n:
            return prime[-1]
        elif isPrime(i) == True:
            prime.append(i)
        i += 1



print(nthPrime(5))
print(nthPrime(11))
print(nthPrime(1000))            
        
