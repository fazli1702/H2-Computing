def factorial(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total
        
def sumDigits(n):
    a = n
    a = str(a)
    total = 0
    for ele in a:
        total += int(ele)
    return total

def totalSum(n):
    return sumDigits(factorial(n))

print(totalSum(10))
print(totalSum(100))
