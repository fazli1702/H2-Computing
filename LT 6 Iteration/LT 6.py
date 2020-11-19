#question 2
ans=3
for i in range(1,7):
    if i == 4:
        continue
    ans= ans+ i
##print(ans)


#question 3
def foo():
    i = 0
    result = 0
    while i < 10:
        if i == 3:
            break
        result = result + i
        i = i + 1
    return result
##print(foo())



#question 4
j = 0
for i in range(10):
    if i >= 9: 
        break
    if j == 8:
        j = j + 2
        continue
    j = j + 1
##print(i, j)



#question 5
x, y = 1, 9
def foo(x, y):
    while y > x:
        y = y // 2
        x = x + 1

foo(x, y)

##print(x)
##print(y)



#question 6
ans = 0
for i in range(4):
     for j in range(4):
         ans= ans + 1
print(ans)
