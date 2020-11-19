import math as m

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
        
def primeFactors(n):
    if isPrime(n) == True:
        return [n]
    else:
        factors = []
        ans = n
        i = 2
        while True:
            if i == n:
                break
            elif ans % i == 0:
                if isPrime(i) == True:
                    factors.append(i)
                    ans = ans / i
                    i = 2
                else:
                    continue
            else:
                i += 1

        return factors


def smallest(n):
    lst = []

    for i in range(2,n+1):
        print('prime factors of', i, ':', primeFactors(i))
        lst.append(primeFactors(i))
        for i in range(n):
            pass
        
        

print(smallest(10))
        

