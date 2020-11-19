def digitlst(n):
    if n == 0:
        return []
    else:
        x = str(n)
        lst = []
        for ele in x:
            lst.append(int(ele))
        lst.sort()
        return lst[::-1]


print(digitlst(343532))
print(digitlst(12345))
print(digitlst(1))
print(digitlst(0))
