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

print(nCr(8,1))
print(nCr(15,0))
print(nCr(2,3))
print(nCr(12,-3))
print(nCr(6,4))


