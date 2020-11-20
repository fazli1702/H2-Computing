def make_queue(seq):
    return list(seq)


def make_empty_queue():
    return []
    

def is_empty_queue(queue):
    if len(queue) == 0:
        return True
    else:
        return False
    
    
    
##########################################
# 		Do not modify test code 		 #				
##########################################
s1 = make_empty_queue()					 #
s2 = make_queue((2, 4, 5))				 #
s3 = make_queue([3, 5, 7, 8])            #
s4 = make_queue('string')                #
										 #
is_empty1 = is_empty_queue(s1) #True	 #
is_empty2 = is_empty_queue(s2) #False	 #
is_empty3 = is_empty_queue(s3) #False    #







def make_empty_queue():
    return []

def enqueue(queue, item):
    queue.append(item)
    return queue

def dequeue(queue):
    if len(queue) == 0:
        return None
    else:
        return queue.pop(0)
        


q = make_empty_queue()                   #
first = dequeue(q) #None                     #
                                         #
enqueue(q, 1)                               #
enqueue(q, 2)                               #
                                         #
second = dequeue(q) #1                       #
third = dequeue(q)  #2                       #
enqueue(q, 3)                               #
fourth = dequeue(q) #3



##print(first)
##print(second)
##print(third)
##print(fourth)






def front(queue):
    if len(queue) == 0:
        return None
    else:
        return queue[0]
    
def size(queue):
    return len(queue)
    
def clear(queue):
    del queue[:]
    return queue

    
##########################################
#       Do not modify test code          #              
##########################################
q1 = make_empty_queue()                  #
q2 = make_queue((2, 4, 5))               #
                                         #
front1 = front(q1) #None                   #
front2 = front(q2) #2  
size1 = size(q1) #0
size2 = size(q2) #3
                                         #
clear(q2)                                #
front3 = front(q2) #None                   #




print(front1)
print(front2)
print(front3)
print(size1)
print(size2)
