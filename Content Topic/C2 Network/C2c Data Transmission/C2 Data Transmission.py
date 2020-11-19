#question 1
def last_letter(nric):
    num = nric[1:]
    check = [2, 7, 6, 5, 4, 3, 2]
    letter = {0:'J', 1:'Z', 2:'I', 3:'H', 4:'G', 5:'F', 6:'E', 7:'D', 8:'C', 9:'B', 10:'A'}
    total = 0
    for i in range(len(num)):
        total += int(num[i]) * check[i]
    if nric[0] == 'T':
        total += 4
    r = total % 11
    return letter[r]
    




##print(last_letter('S1234567'))
##print(last_letter('T1234567'))
##print(last_letter('T0239655'))
##print(last_letter('T0239653'))












#question 2
def isbn(string):
    check = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    total = 0
    isbn = ''
    for i in range(len(string)):
        total += int(string[i]) * check[i]
    #print('total:', total)

    r = total % 11
    #print('r:', r)
    check_digit = 11 - r
    #print('check digit:', check_digit)
    
    if check_digit == 10:
        isbn += string + 'X'
    elif check_digit == 11:
        isbn += string + '0'
    else:
        isbn +=  string + str(check_digit)
    
    return isbn


##print(isbn('075154926') == '0751549266')
##print(isbn('184146208') == '184146208X')
##print(isbn('034085045') == '0340850450')
