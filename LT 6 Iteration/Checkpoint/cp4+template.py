###Checkpoint 4 template####

###Qn 1
def count_vowel(string):
    counter = 0                          #method 2
    for i in range(len(string))          #for ele in string:
        if string[i] == 'a':                #if ele == 'a' or .....
            counter += 1
        elif string[i] == 'e':
            counter += 1
        elif string[i] == 'i':
            counter += 1
        elif string[i] == 'o':
            counter += 1
        elif string[i] == 'u':
            counter += 1
        else:
            counter += 0
    return counter





        





####Please uncomment the following (Alt+4) to run test cases
##print("---Qn 1---")
##print(count_vowel("apple")==2)        
##print(count_vowel("rhythms")==0)       
##print(count_vowel('queueing')==5)   
####feel free to include your own test cases


'''-----------------------------------------------------------'''

###Qn 2
from module import lucas   ###do not remove/modify


def sum_odd_lucas(n):

    total = 0
    x = 1
    
    while lucas(x) <= n:
        if lucas(x) % 2 == 1:
            total += lucas(x)
        x += 1
    return total
        
            
####Please uncomment the following (Alt+4) to run test cases
##print("---Qn 2---")
##print(sum_odd_lucas(4))        
##print(sum_odd_lucas(21))
##print(lucas(5))
####feel free to include your own test cases





#question 3
def lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:

        lucas_0 = 2
        lucas_1 = 1
        total = 0

        for i in range(n-2):
            total = lucas_0 + lucas_1
            lucas_0, lucas_1 = lucas_1, total

        return total

def lucas_exceed(n):
    if n == 0 or n == 1:
        return 2
    else:
        x = 1
        while lucas(x) <= n:
            x += 1
        return lucas(x)













#question 4
def label(string, name):

    for i in range(len(string)):

        if string[i] == '%' and i == len(string):
            string = string[:i] + name
            continue

        elif string[i] == '%' and i == 0:
            string = name + string[1:]
            continue

        elif string[i] == '%':
            string = string[:i] + name + string[i+1:]
            continue

        else:
            continue

    return string


##print(label("Health Report On: %", "Joe Lim"))
##print(label("% is a garden city.", "Singapore"))
##print(label("Supercal%frag%l%st%cexp%al%doc%ous", "i"))
##print(label("%eter %i%er %icked a %eck of %ickled %e%%ers.", "p"))






