def check(n):
    i = 6
    total = 0
    for ele in n:
        ele = int(ele)
        total += ele * i
        i -= 1
    total %= 11
    # print(total)
    return total == 0


##print(check('810230'))
##print(check('371025'))
##print(check('483095'))
##print(check('438095'))

'''
b) One typical error is entering the wrong ID due to human error
   such as 438095 (not valid). By doing the inputing the entry,
   the program will do the calculations and return a 6, which is not
   0 and thus return False

c) To verify the ID, the entry form can prompt the user to input the
   ID again and check if the two entries are equal and if they are not,
   it will prompt the user to input the entry again and reverify it again.
'''
