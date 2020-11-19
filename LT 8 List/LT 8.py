#question 11
p = ["hello", "kitty"]
q = [123, 456]
r = p.copy()
s = q
q[0] = ( ) 





#question 12
alist = [4, 2, 8, 6, 5]
alist[2] = True
alist[2:2] = [False]
##print(alist)




#question 13
a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
a.remove(3)
b.remove(4)
##print(a)
##print(b)


#question 14
c = ["a", 2]
d = [4, "e"]
d.reverse()
c.extend(d)
e = c.copy()
e.append(d)
##print(c)
##print(d)
##print(e)



#question 15
list1 = [1] * 4
list2 = [5, 5, 5]
while not 0:
    list1[0] += 1
    if list1[0] == 5: 
         break
         list1[1] += 2
    list1[2] += 3

##print(list1 < list2)
##print(list2 == (5, 5, 5))









#question 16
balls = ['red', 'green', 'blue', 'red', 'yellow', 'blue']
balls.pop()
balls.pop()
balls.insert(2, 'yellow')
balls.append('red')
balls.pop(4)
del balls[0]
balls.insert(0, 'blue')
balls.remove('blue')
##print(balls)
