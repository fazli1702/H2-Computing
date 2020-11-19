def size(n):
    if n == 0:
        return 0
    else:
        total = n
        counter = 0
        while True:
            total /= 10
            counter += 1
            if total < 1:
                return counter
            else:
                continue


print(size(54321))
print(size(1))
print(size(0))
print(size(100925759386))
