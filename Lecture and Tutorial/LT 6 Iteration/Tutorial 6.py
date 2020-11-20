#question 1
def factorial_while(n):
    product, counter = 1, 1
    while counter <= n:
        product = product * counter
        counter = counter + 1
    return product

##print(factorial_while(0) == 1)
##print(factorial_while(1) == 1)
##print(factorial_while(5) == 120)
##print(factorial_while(8) == 40320)










#question 2
def factorial_for(n):
    product = 1
    for counter in range(1, n+1):
        product = product * counter
    return product

##print(factorial_for(0) == 1)
##print(factorial_for(1) == 1)
##print(factorial_for(5) == 120)
##print(factorial_for(8) == 40320)













#question 3
def exp_iterate_while(x,e):
    product, exponent = 1, 1
    while exponent <= e:
        product = product * x
        exponent = exponent + 1
    return product

##print(exp_iterate_while(2,3) == 8)
##print(exp_iterate_while(1,0) == 1)
##print(exp_iterate_while(5,2) == 25)
##print(exp_iterate_while(2,5) == 32)
##print(exp_iterate_while(-5,3) == -125)










#question 4
def exp_iterate_for(x,e):
    product =  1
    for exponent in range(e):
        product = product * x
    return product
    
##print(exp_iterate_for(2,3) == 8)
##print(exp_iterate_for(1,0) == 1)
##print(exp_iterate_for(5,2) == 25)
##print(exp_iterate_for(2,5) == 32)
##print(exp_iterate_for(-5,3) == -125)











#question 5
def count_sum(n):
    total_sum = 1
    for i in range(2,n+1):
        total_sum = total_sum + i
    return total_sum

##print(count_sum(1) == 1)
##print(count_sum(2) == 3)
##print(count_sum(5) == 15)
##print(count_sum(10) == 55)
##print(count_sum(13) == 91)








#question 6
def count_odd(n):
    total_sum = 1
    for i in range(3,n+1,2):
        total_sum = total_sum + i
    return total_sum

##print(count_odd(5) == 9)
##print(count_odd(7) == 16)
##print(count_odd(9) == 25)
##print(count_odd(1) == 1)
##print(count_odd(6) == 9)
##print(count_odd(8) == 16)
##print(count_odd(10) == 25)
##print(count_odd(2) == 1)












#question 7
def count_char(string,character):
    counter = 0
    for i in range (len(string)):
        if string[i] == character:
            counter = counter + 1
        else:
            pass
    return counter
     

##print(count_char('banana','a') == 3)
##print(count_char('banana','n') == 2)
##print(count_char('she sells seashells on the seashore',' ') == 5)
##print(count_char('oohlala','o') == 2)
        














#question 8
def star_wars_iterate(num_enemy_ships):
    beam = ''
    for i in range( num_enemy_ships):
        beam = beam + '*-'
    return beam
        

##print(star_wars_iterate(3))
##print(star_wars_iterate(0))
##print(star_wars_iterate(5))
##print(star_wars_iterate(6))
##print(star_wars_iterate(7))













#question 9
def alt_fire_iterate(num_enemy_ships):
    beam = ''
    for i in range(1, num_enemy_ships + 1):
        if i % 2 == 0:
            beam = beam + '*--'
        else:
            beam = beam + '*-'
    return beam


##print(alt_fire_iterate(3))
##print(alt_fire_iterate(0))
##print(alt_fire_iterate(5))
##print(alt_fire_iterate(6))
##print(alt_fire_iterate(7))
##print(alt_fire_iterate(8))
















#question 10
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_odd_factorials(n):
    x = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            x = x + factorial(i)
    return x
        
        
            
##print(sum_odd_factorials(0) == 0)
##print(sum_odd_factorials(1) == 1) 
##print(sum_odd_factorials(3) == 7)
##print(sum_odd_factorials(6) == 127)
##print(sum_odd_factorials(7) == 5167)
##print(sum_odd_factorials(8) == 5167)
 


















#question 11
def powers_of_two(n):
    for i in range (n):
        if 2 ** i == n:
            return i


##print(powers_of_two(1) == 0)        
##print(powers_of_two(2) == 1)
##print(powers_of_two(4) == 2)
##print(powers_of_two(8) == 3)    
##print(powers_of_two(16) == 4)
##print(powers_of_two(32) == 5)
##print(powers_of_two(64) == 6)
##print(powers_of_two(128) == 7)














#question 13
def f_iter(n):
    a, b, c = 2, 1, 0
    counter = 0
    if n < 3:
        return n
    else:
        for i in range(n-3):
            a, b, c = a + 2*b + 3*c, a, b
            counter += 1
        print(counter)
        return a + 2*b + 3*c 
    
    
##print(f_iter(4))
        
