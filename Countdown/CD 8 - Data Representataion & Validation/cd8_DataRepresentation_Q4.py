def binary_to_denary(s):
    s = s[::-1]
    total = 0
    for i in range(len(s)):
        if s[i] != '0':
            total += 2**i
    return total

def binary_to_octal(s):
    # split string
    s = s[::-1]
    temp = ''
    splitBin = []
    for ele in s:
        if len(temp) < 3:
            temp += ele
        else:
            splitBin.append(temp)
            temp = ''
            temp += ele
            
    if len(temp) != 0:
        splitBin.append(temp)
    splitBin.reverse()

    # convert bin to octal
    octal = ''
    for ele in splitBin:
        ele = ele[::-1]
        octal += str(binary_to_denary(ele))
    return octal


def binary_to_hexadecimal(s):
    # split string
    s = s[::-1]
    temp = ''
    splitBin = []
    for ele in s:
        if len(temp) < 4:
            temp += ele
        else:
            splitBin.append(temp)
            temp = ''
            temp += ele
            
    if len(temp) != 0:
        splitBin.append(temp)
    splitBin.reverse()

    # convert bin to octal
    alpha = 'ABCDEF'
    hexa = ''
    for ele in splitBin:
        ele = ele[::-1]
        n = binary_to_denary(ele)
        if n > 9:
            hexa += alpha[n-10]
        else:
            hexa += str(n)
    return hexa




##print(binary_to_octal('110101111011'))
##print(binary_to_hexadecimal('110101111011'))
##print(binary_to_octal('1101011011'))
##print(binary_to_hexadecimal('1101011011'))
