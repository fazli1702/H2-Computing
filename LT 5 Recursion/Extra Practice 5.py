#question 1
def star_wars_recursive(num_enemy_ships):
    if num_enemy_ships == 0:
        return ''
    else:
        return '*-' + star_wars_recursive(num_enemy_ships - 1)

##print(star_wars_recursive(3))
##print(star_wars_recursive(0))
##print(star_wars_recursive(5))
##print(star_wars_recursive(6))



#question 2
def alt_fire_recursive(num_enemy_ships):
    if num_enemy_ships == 0:
        return ''
    else:
        return '*-' + alt_fire_recursive2(num_enemy_ships-1)
    
def alt_fire_recursive2(num_enemy_ships):
    if num_enemy_ships == 0:
        return ''
    else:
        return '*--' + alt_fire_recursive(num_enemy_ships-1)

##print(alt_fire_recursive(3))
##print(alt_fire_recursive(0))
##print(alt_fire_recursive(5))
##print(alt_fire_recursive(6))




#question 3
def count_odd(n):
    if n == 1:
        return 1
    elif n % 2 == 1:
        return n + count_odd(n-1)
    else:
        return count_odd(n-1)

##print(count_odd(5) == 9)
##print(count_odd(7) == 16)
##print(count_odd(9) == 25)
##print(count_odd(10) == 25)
##print(count_odd(2) == 1)



#question 4
def count_even(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n + count_even(n-1)
    else:
        return count_even(n-1)

##print(count_even(5) == 6)
##print(count_even(6) == 12)
##print(count_even(7) == 12)
##print(count_even(8) == 20)
##print(count_even(9) == 20)
##print(count_even(1) == 0)




#question 5
def count_sum(n):
    if n == 1:
        return 1
    else:
        return n + count_sum(n-1)

def count_even(n):
    if n == 0:
        return 0
    else:
        return count_sum(n) - count_odd(n)

##print(count_even(5) == 6)
##print(count_even(6) == 12)
##print(count_even(7) == 12)
##print(count_even(8) == 20)
##print(count_even(9) == 20)
##print(count_even(1) == 0)
##print(count_even(2) == 2)


#question 6   
def count_sum(n):
    if n == 1:
        return 1
    else:
        return n + count_sum(n-1)

def count_even(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n + count_even(n-1)
    else:
        return count_even(n-1)

def count_odd(n):
    if n == 0:
        return 0
    else:
        return count_sum(n) - count_even(n)

##print(count_odd(1) == 1)
##print(count_odd(2) == 1)
##print(count_odd(5) == 9)
##print(count_odd(7) == 16)
##print(count_odd(8) == 16)
##print(count_odd(9) == 25)



#question 7
def shift(char):
    if char == 'z':
        return 'a'
    elif char.isalpha():
        return chr(ord(char) + 1)
    else:
        return char

def shift_all(char, n):
    if n == 0:
        return char
    else:
        return shift_all(shift(char), n-1)


def caesar_encrypt(message, positions):
    if positions == 0:
        return message
    elif message == '':
        return ''
    else:
        return shift_all(message[0], positions) + caesar_encrypt(message[1:],positions)
    
   

##print(caesar_encrypt('abcdef',3) == 'defghi')
##print(caesar_encrypt('hello world!', 3) == 'khoor zruog!')
##print(caesar_encrypt('hello world!', 29) == 'khoor zruog!')
##print(caesar_encrypt('hello world!', 0) == 'hello world!')
##print(caesar_encrypt('abcdefghijklmnopqrstuvwxyz', 13) == 'nopqrstuvwxyzabcdefghijklm')
##print(caesar_encrypt('nopqrstuvwxyzabcdefghijklm', 13) == 'abcdefghijklmnopqrstuvwxyz')
##print(caesar_encrypt('!@\#$%^&*()', 6) == '!@\#$%^&*()')
##print(caesar_encrypt('', 10) == '')

    


#question 8
def shift(char):
    if char == 'z':
        return 'a'
    elif char.isalpha():
        return chr(ord(char) + 1)
    else:
        return char

def shift_all(char, n):
    if n == 0:
        return char
    else:
        return shift_all(shift(char), n-1)
    
def caesar_encrypt(message, positions):
    if positions == 0:
        return message
    elif message == '':
        return ''
    else:
        return shift_all(message[0], positions) + caesar_encrypt(message[1:],positions)

def caesar_decrypt(ciphertext, position2):
    return caesar_encrypt(ciphertext, 26 - (position2 % 26))

##print(caesar_decrypt('khoor zruog!', 3) == 'hello world!')
##print(caesar_decrypt('!@\#$%^&*()', 6) == '!@\#$%^&*()')
##print(caesar_decrypt('abcdefghijklmnopqrstuvwxyz', 13) == 'nopqrstuvwxyzabcdefghijklm')
##print(caesar_decrypt('nopqrstuvwxyzabcdefghijklm', 13) == 'abcdefghijklmnopqrstuvwxyz')
##print(caesar_decrypt('etq eqxxe eqmetqxxe az ftq eqm etadq', 12) == 'she sells seashells on the sea shore')
##print(caesar_decrypt('', 18) == '')

    
