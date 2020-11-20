#question 1
def count_sum(n):
    if n == 1:
        return 1
    else:
        return n + count_sum(n-1)

#print(count_sum(1) == 1)
#print(count_sum(2) == 3)
#print(count_sum(5) == 15)
#print(count_sum(10) == 55)


#question 2
def sum_n_squares(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_n_squares(n-1)

#print(sum_n_squares(5) == 55)
#print(sum_n_squares(4) == 30)
#print(sum_n_squares(1) == 1)


#question 3
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(0) == 1)
#print(factorial(1) == 1)
#print(factorial(5) == 120)
#print(factorial(8) == 40320)



#question 4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_odd_factorials(n):
    if n == 0:
        return 0
    elif n % 2 == 1:
        return factorial(n) + sum_odd_factorials(n-1)
    else:
        return sum_odd_factorials(n-1)
         
##print(sum_odd_factorials(0) == 0)    
##print(sum_odd_factorials(3) == 7)
##print(sum_odd_factorials(6) == 127)
##print(sum_odd_factorials(7) == 5167)
##print(sum_odd_factorials(8) == 5167)




#question 5
def powers_of_two(x):
    if x == 1:
        return 0
    else:
        return 1 + powers_of_two(x // 2)
    
##print(powers_of_two(1) == 0)
##print(powers_of_two(2) == 1)      
##print(powers_of_two(4) == 2)
##print(powers_of_two(8) == 3)
##print(powers_of_two(1024) == 10)
##print(powers_of_two(32) == 5)




#question 6
def exp_recursive(x,e):
    if e == 0 or x == 1:
        return 1
    else:
        return x * exp_recursive(x,e-1)
    
##print(exp_recursive(2,3) == 8)	
##print(exp_recursive(1,0) == 1)	
##print(exp_recursive(5,2) == 25)	
##print(exp_recursive(2,5) == 32)	
##print(exp_recursive(-2,4) == 16)   
        



#question 7
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


##print(fib(1) == 1)
##print(fib(5) == 5)
##print(fib(11) == 89)



#question 8
def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 1:
        return collatz(3*n+1)
    else:
        return collatz(n//2)

##print(collatz(6) == 1)
##print(collatz(1) == 1)



#question 9
def count_char(string, character):
    if string == '':
        return 0
    elif string[0] == character:
        return 1 + count_char(string[1:], character)
    else:
        return 0 + count_char(string[1:], character)

##print(count_char('banana','a'))
##print(count_char('banana','n'))
##print(count_char('she sells seashells on the seashore',' '))



#question 10
def replace_char(string, c, r):
    if string == '':
        return ''
    elif string[0] == c:
        return r + replace_char(string[1:], c, r)
    else:
        return string[0] + replace_char(string[1:], c, r)

##print(replace_char("31242154125", "1", "0") == '30242054025')
##print(replace_char("thisisasong", "s", "e") == "thieieaeong")


#question 11
def delete_letter(msg, letter):
    if msg == '':
        return ''
    elif msg[0] == letter:
        return delete_letter(msg[1:], letter) 
    else:
        return msg[0] + delete_letter(msg[1:],letter)


##print(delete_letter('habit', 'h') == 'abit')
##print(delete_letter('a pack of pickled peppers', 'p') == 'a ack of ickled eers')
##print(delete_letter('jack and jill', ' ') == 'jackandjill')
##print(delete_letter('a ack of ickled eers', 'e') == 'a ack of ickld rs')
##print(delete_letter('a ack of ickld rs', ' ') == 'aackofickldrs')
##print(delete_letter('jack and jill', 'j') == 'ack and ill')
##print(delete_letter('abcde', 'f') == 'abcde')
##print(delete_letter('aaaaa', 'a') == '')




#question 12
def shift_left(string, n):
    if n == 0:
        return string
    else:
        return shift_left(string[1:] + string[0], n-1)
    

##print(shift_left("12345", 1) == '23451')
##print(shift_left("def", 1) == 'efd')
##print(shift_left("12345", 2) == '34512')
##print(shift_left("hello", 3) == 'lohel')



#question 13
def shift_right(string, n):
    if n == 0:
        return string
    else:
        return shift_right(string[-1] + string[0:-1], n-1)

##print(shift_right("12345", 3) == "34512")
##print(shift_right("hello", 2) == 'lohel')


