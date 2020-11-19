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

def split(string):
    if len(string) == 0:
        return (0, '')
    elif len(string) == 1:
        return (1.0, string)
    else:
        return (float(string[:-1]), string[-1])


def expansion(a, b, n):
    x = split(a)[0]
    y = split(b)[0]
    lst = []
    
    for i in range(n+1):
        coef = nCr(n, i) * (x ** (n-i)) * (y ** i)
        lst.append(coef)
    return lst
        

        
print(expansion('x','y',2))
print(expansion('3x','-2y',3))
print(expansion('0.5x','4y',4))


    
