def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev = 1
    prevprev = 0
    for i in range(2, n+1):
        curr = prev + prevprev
        prevprev = prev
        prev = curr
    return curr

def evenFib(n):
    total = 0
    for i in range(n):
        if fib(i) > n:
            return total
        elif fib(i) % 2 == 0:
            total  += fib(i)
    return total


print(evenFib(10))
print(evenFib(50))
print(evenFib(48000))
