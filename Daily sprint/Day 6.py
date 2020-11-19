def sumSquare(n):
    lst = list(range(1, n+1))
    a = sum(lst) ** 2
    b = 0
    for ele in lst:
        b += (ele ** 2)
    total = a - b
    return total

print(sumSquare(10))
print(sumSquare(100))
print(sumSquare(250))
