#question 3
def make_stack(seq):
    return list(seq)


def make_empty_stack():
    return []
    

def is_empty_stack(stack):
    if len(stack) > 0:
        return False
    else:
        return True
    
    
s1 = make_empty_stack()					 
s2 = make_stack((2, 4, 5))				 
s3 = make_stack([3, 5, 7, 8])            
s4 = make_stack('string')                
				
is_empty1 = is_empty_stack(s1) #True	 
is_empty2 = is_empty_stack(s2) #False	 
is_empty3 = is_empty_stack(s3) #False

##print(is_empty1)
##print(is_empty2)
##print(is_empty3)





#question 4
def make_empty_stack():
    return []

def push(stack, item):
    stack += [item]

def pop(stack):
    if stack == []:
        return None
    else:
        return stack.pop()


s = make_empty_stack()                   #
first = pop(s) #None                     #
                                         #
push(s, 1)                               #
push(s, 2)                               #
                                         #
second = pop(s) #2                       #
third = pop(s)  #1                       #
push(s, 3)                               #
fourth = pop(s) #3

##print(first)
##print(second)
##print(third)
##print(fourth)







#question 5

def peek(stack):
    if stack == []:
        return None
    else:
        return stack[-1]

def clear(stack):
    del stack[:]
    return stack


s1 = make_empty_stack()                  #
s2 = make_stack((2, 4, 5))               #
                                         #
peek1 = peek(s1) #None                   #
peek2 = peek(s2) #5                      #
                                         #
clear(s2)                                #
peek3 = peek(s2) #None                   #


##print(peek1)
##print(peek2)
##print(peek3)
