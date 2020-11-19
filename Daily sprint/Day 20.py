def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        total = 1
        for i in range(1, n+1):
            total *= i
        return total
