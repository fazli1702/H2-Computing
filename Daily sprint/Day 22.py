def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

def nCr(n, r):
    if r > n or r < 0 or n < 0:
        return 'Invalid input'
    else:
        num = factorial(n)
        den = factorial(r) * factorial(n-r)
        ans = num / den
        return int(ans)

def binomial(n):
    lst = []
    for i in range(n+1):
        lst.append(nCr(n, i))
    return lst

print(binomial(5))
print(binomial(0))
print(binomial(10))
        
        
    
    
