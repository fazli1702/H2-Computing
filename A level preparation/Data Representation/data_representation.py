'2015 P1Q2'
def Converter(DenaryNumber, binary=''):
    if DenaryNumber == 0 or DenaryNumber == 1:
        binary += str(DenaryNumber)
        return binary[::-1]
    else:
        binary += str(DenaryNumber % 2)
        return Converter(DenaryNumber // 2, binary)


'''
test cases:
1) 1, test for 'if' case, 1
2) 10, test for proper/correct output, 1010
3) 57, test for proper/correct output, 111001
'''

##print(Converter(1))
##print(Converter(10))
##print(Converter(57))
        











'20162016 P1Q4'
'Task 4.1 & 4.2'
import string

def hexDec(hexa):
    if hexa in string.digits:
        return int(hexa)
    
    else:
        for i, ele in enumerate(string.ascii_uppercase):
            if hexa == ele:
                return 10 + i


def hex_to_dec(hexadecimal):
    
    # validate input
    if type(hexadecimal) != str:  # check for string type
        return 'Invalid input'
    
    valid = [str(ele) for ele in range(10)]
    valid += string.ascii_uppercase[:6]
    for ele in hexadecimal:
        if ele not in valid:  # invalid letter
            return 'Invalid input'
        
    # convert individual hex to dec
    hexa = [hexDec(ele) for ele in hexadecimal]
    dec = 0

    # convert hex to dec
    for i, ele in enumerate(hexa[::-1]):
        dec += ele * (16 ** i)
    return dec

'''
test cases:
1) "123FGN", check if letter validation is working, "Invalid input"
2) "CA5E", check if conversion is correct, 64206
3) 12346, check if string input validation working, "Invalid input"
'''
##print(hex_to_dec('FACE'))

##print(hex_to_dec('123FGN'))
##print(hex_to_dec('CA5E'))
##print(hex_to_dec(123456))



'task 4.3 & 4.4'
def denary_to_hex(n, hexa=''):

    # validate for integer type
    if type(n) != int:
        return 'Invalid input'
    
    valid = [str(ele) for ele in range(10)]
    valid += string.ascii_uppercase[:6]
    
    if n < 16:
        hexa += valid[n]
        return hexa[::-1]
    else:
        hexa += valid[n % 16]
        return denary_to_hex(n // 16, hexa)

'''
test cases:
1) "1234", check for type validation, "Invalid input"
2) 79, check for correct conversion, "4F"
3) 1728, check for correct coversion, "6C0"
'''

##print(denary_to_hex("1234"))
##print(denary_to_hex(79))
##print(denary_to_hex(1728))










'2015 P2Q4'
def INTMOD(Number, Divisor):
    return Number % Divisor

def INTDIV(Number, Divisor):
    return Number // Divisor

def SUBSTR(ThisString, Start, Length):
    return ThisString[Start:Start+Length]


def DenaryToOctal(n: int) -> str:
    OctalDigits = '01234567'
    if n < 8:
        TempString = SUBSTR(OctalDigits, n, 1)
    else:
        TempString = DenaryToOctal(INTDIV(n, 8)) + \
                     SUBSTR(OctalDigits, INTMOD(n, 8), 1)
        
    return TempString



def DenaryToHexadecimal(n):
    HexDigits = '0123456789ABCDEF'
    if n < 16:
        TempString = SUBSTR(HexDigits, n, 1)
    else:
        div = INTDIV(n, 16)
        substr = SUBSTR(HexDigits, INTMOD(n, 16), 1)
        TempString = DenaryToHexadecimal(div) + substr
        
    return TempString

'''
Describe the changes:
- that are essential to make the revised function work (den-hex)
- that are non-essential but would help with the clarity of the pseudocode

1) One of the main changes is the hexadecimal digits.
   Hex digits run from 1 - 9 and A - F while octal is only 1-7.
   The other main change is that divide and mod the denary number by 16 for
   conversion to hex while we div and mod the denary number by 8 for octal number

2) We can assign variables when we call the different helper functions so that
   we know what the values of each variables are and what other operation we
   are going to do.
'''



##print(INTMOD(7, 3))
##print(INTDIV(7, 3))
##print(SUBSTR('abcd', 1, 2))
##print(DenaryToOctal(6354))
##print(DenaryToHexadecimal(6354))





from string import *

def convert(string):
    lowerCase = ascii_lowercase
    upperCase = ascii_uppercase
    n = len(lowerCase)  # number of letters ->  26
    output = ''
    for ele in string:
        
        # if element is a lowercase letter
        if ele in lowerCase:
            for i, letter in enumerate(lowerCase):
                if ele == letter:
                    index = (i+13) % n
                    output += lowerCase[index]
                    break

        # if element is a uppercase letter
        elif ele in upperCase:
            for i, letter in enumerate(upperCase):
                if ele == letter:
                    index = (i+13) % n
                    output += upperCase[index]
                    break

        # element is not a letter / is a symbol
        else:
            output += ele

    return output
                    
                    
a = 'This is a word'
b = 'ALL &&&& CAPITALS'
c = 'UpperCamelCase12()'

print(convert(a))
print(convert(b))
print(convert(c))

