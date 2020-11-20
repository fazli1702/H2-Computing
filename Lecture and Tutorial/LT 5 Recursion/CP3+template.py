###Checkpoint 3 template####
###Qn 1
def product_even(n):
    if n < 2:
        return 1
    elif n % 2 == 0:
        return n * product_even(n-1)
    else:
        return product_even(n-1)





####Please uncomment the following (Alt+4) to run test cases
print("---Qn 1---")
print(product_even(4)==8)
print(product_even(7)==48) 
print(product_even(8)==384)       
####feel free to include your own test cases

'''-----------------------------------------------------------'''

###Qn 2
def reverse_string(string):
    if string == '':
        return ''
    else:
        return string[-1] + reverse_string(string[:-1])
        





####Please uncomment the following (Alt+4) to run test cases
print("---Qn 2---")
print(reverse_string("wow")=="wow")        
print(reverse_string("live")=="evil")       
print(reverse_string("stressed")=="desserts")   
####feel free to include your own test cases

'''------------------------------------------------------------'''

###Qn 3
def is_palindrome(string):
    if string == reverse_string(string):
        return True
    else:
        return False





####Please uncomment the following (Alt+4) to run test cases
print("---Qn 3---")
print(is_palindrome("time")==False)        
print(is_palindrome("willow")==False)      
print(is_palindrome("madam")==True)       
print(is_palindrome("redder")==True)
####feel free to include your own test cases

'''------------------------------------------------------------'''

###Qn 4
def is_abecedarian(string):
    if len(string) <= 1:
        return True
    elif string[len(string)-1] >= string[len(string)-2]:
        return is_abecedarian(string[:-1])
    else:
        return False


                                                             
                                                        
####Please uncomment the following (Alt+4) to run test cases
print("---Qn 4---")
print(is_abecedarian("hippy")==True)      
print(is_abecedarian("hippo")==False)      
print(is_abecedarian("almost")==True)        
####feel free to include your own test cases

'''------------------------------------------------------------'''

###Qn 5 Bonus
def power_10(k):
    if k < 10:
        return 0
    else:
        return 1 + power_10(k/10)

def reverse_num(k):
    if k < 10:
        return k
    else:
        return (k % 10) * (10 ** power_10(k)) + reverse_num(k//10)
    


####Please uncomment the following (Alt+4) to run test cases
print("---Qn 5 Bonus---")
print(reverse_num(123)==321)      
print(reverse_num(87)==78)      
print(reverse_num(62574373)==37347526)        
####feel free to include your own test cases


