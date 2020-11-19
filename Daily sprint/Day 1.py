def sumOfMultiples(number):
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
        else:
            continue
    return total

print(sumOfMultiples(10))
