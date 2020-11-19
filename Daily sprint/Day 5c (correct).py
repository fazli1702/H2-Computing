import math as m

def smallest(n):
    ans = 1
    for i in range(1, n+1):
        ans = (ans * i) / m.gcd(ans, i)
    return ans


print(smallest(10))
print(smallest(20))
print(smallest(25))
