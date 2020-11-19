def denary_to_binary(n):
    result = ''
    while True:
        result += str(n % 2)
        n //= 2
        if n == 0:
            break
    return result[::-1]

def denary_to_octal(n):
    result = ''
    while True:
        result += str(n % 8)
        n //= 8
        if n == 0:
            break
    return result[::-1]

def denary_to_hexadecimal(n):
    alpha = 'ABCDEF'
    result = ''
    while True:
        mod = n % 16
        if mod > 9:
            result += alpha[mod-10]
        else:
            result += str(mod)
        n = n // 16
        if n == 0:
            break
    return result[::-1]



def binary_to_denary(n):
    # n : string
    n = n[::-1]
    total = 0
    for i in range(len(n)):
        if n[i] == '1':
            total += (2 ** i)
    return total
    
def octal_to_denary(n):
    # n : string
    n = n[::-1]
    total = 0
    for i in range(len(n)):
        if n[i] != '0':
            total += int(n[i]) * (8**i)
    return total

def hexadecimal_to_denary(n):
    # n : string
    key = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    n = n[::-1]
    total = 0
    for i in range(len(n)):
        if n[i] != '0':
            if n[i].isdigit():
                total += int(n[i]) * (16**i)
            else:
                total += int(key[n[i]]) * (16**i)
    return total



def main():
    while True:
        print('1. Denary to Binary')
        print('2. Denary to Octal')
        print('3. Denary to Hexadecimal')
        print('4. Binary to Denary')
        print('5. Octal to Denary')
        print('6. Hexadecimal to Denary\n')

        choice = input('Please enter your choice<1-6>:')

        if choice == '1':
            n = int(input('Enter denary number:'))
            return denary_to_binary(n)
            
        elif choice == '2':
            n = int(input('Enter denary number:'))
            return denary_to_octal(n)
            
        elif choice == '3':
            n = int(input('Enter denary number:'))
            return denary_to_hexadecimal(n)
            
        elif choice == '4':
            n = input('Enter binary number:')
            return binary_to_denary(n)
            
        elif choice == '5':
            n = input('Enter octal number:')
            return octal_to_denary(n)
            
        elif choice == '6':
            n = input('Enter hexadecimal number:')
            return hexadecimal_to_denary(n)
            
        else:
            print('Please enter a valid choice')


##print(denary_to_binary(174))
##print(denary_to_octal(174))
##print(denary_to_hexadecimal(174))
            
##print(binary_to_denary('10101110'))
##print(octal_to_denary('256'))
##print(hexadecimal_to_denary('AE'))
