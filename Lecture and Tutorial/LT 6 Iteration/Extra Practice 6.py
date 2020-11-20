#question 1
def sum_n_squares(n):
    power = 0
    total = 0
    for i in range(1, n+1):
        power = i ** 2
        total += power
    return total

##print(sum_n_squares(5))














#question 2
def perfect_number(number):
    total = 0
    counter = 1
    while True:
        if counter == number:
            break
        elif number % counter == 0:
            total += counter
        counter += 1
    return total == number


##print(perfect_number(6))
##print(perfect_number(30))
##print(perfect_number(1))
##print(perfect_number(498))





















#question 3
def pattern(number):
    pattern = ''
    for i in range(1, number + 1):
        pattern += '#' + '-' * i
    return pattern

##print(pattern(5))




















#question 4
from math import*
def counter(num):
    power = floor(log(num, 10))
    return power

#print(counter(54321))

def invert_number(num):
    power = counter(num)
    result = 0
    quotient = num
    
    while quotient > 0:
        rem = quotient % 10
        quotient = quotient // 10
        result += rem * 10 ** power
        power -= 1

    return result

##print(invert_number(12345))

















#question 5
def replace_char(string, c, r):
    total = ''
    for i in range(len(string)):
        if string[i] == c:
            total += r
        else:
            total += string[i]
    return total
            

##print(replace_char("31242154125", "1", "0"))
##print(replace_char("thisisasong", "s", "e"))
    
    



    









#question 6
def delete_letter(msg, letter):
    total = ''
    for i in range(len(msg)):
        if msg[i] == letter:
            total += ''
        else:
            total += msg[i]
    return total
    

##print(delete_letter('habit', 'h'))
##print(delete_letter('a pack of pickled peppers', 'p'))
##print(delete_letter('jack and jill', ' '))



















#question 7
def count_longest_streak(num):
    s = str(num)
    counter = 0
    current_char = s[0]
    max_count = 0
    
    for i in range(len(s)):
        if s[i] == current_char:
            counter += 1
            max_count = max(max_count, counter)
        else:
            current_char = s[i]
            counter = 1
    return max_count

##print(count_longest_streak(111111112) == 8)
##print(count_longest_streak(1222) == 3)
##print(count_longest_streak(222233333445) == 5)
##print(count_longest_streak(112233) == 2)
##print(count_longest_streak(573850395782675827578378347844343434) == 2)
##print(count_longest_streak(33333555559999988888811111) == 6)
        



















#question 8
def sumOfMultiples(n):
    result = 0
    for i in range(1, n):
        if i % 3 == 0:
            result += i
        elif i % 5 == 0:
            result += i
        else:
            result += 0
    return result

##print(sumOfMultiples(1000))

















#question 9
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

##print(fib(1) == 1)
##print(fib(5) == 5)        
##print(fib(11) == 89)
