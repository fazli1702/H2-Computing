def sumDigits(n):
    a = n
    a = str(a)
    total = 0
    for ele in a:
        total += int(ele)
    return total


print(sumDigits(0))
print(sumDigits(12))
print(sumDigits(2**250))
