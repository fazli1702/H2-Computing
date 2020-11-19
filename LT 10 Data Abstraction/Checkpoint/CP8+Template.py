
# coding: utf-8

# # Check Point 8 - Data Abstraction, Stack and Queue ADT

# ## Question 1 : Data Abstraction  (12 marks)

# In[ ]:

from module import*

table = read_csv("data.csv")      # Do not remove this line


# In[ ]:


def count(lst,gender):
    total = 0
    for ele in lst:
        if gender == get_gender(ele):
            total += 1
        else:
            continue
    return total
            
        


# In[ ]:


##print(count(table, 'F'))


# In[ ]:


def ave_height(lst):
    total = 0
    for ele in lst:
        total += get_height(ele)
        ave = total  / get_size(lst)
    return round(ave, 2)


# In[ ]:


##print(ave_height(table))


# In[ ]:


def max_weight(lst):
    max_w = 0
    for ele in lst:
        if max_w < get_weight(ele):
            max_w = get_weight(ele)
        else:
            continue
    return round(max_w, 2)
        


# In[ ]:


##print(max_weight(table))


# In[ ]:


def bmi_list(lst):
    bmi = 0
    tup = ()
    for ele in lst:
        bmi = round(get_weight(ele) / (get_height(ele)**2), 2)
        tup += ((get_name(ele), bmi),)
    return tup
        


# In[ ]:


##print(bmi_list(table)[48:53])


# ## Question 2 : An Application of Stack ADT  [10 marks]

# In[ ]:


from stack_module import *

def minim(stack):
    minim = stack[0]
    for ele in stack:
        if minim > ele:
            minim = ele
        else:
            continue
    return minim
    

def merge(seq1, seq2):
    stk1 = make_stack(seq1)       # Do not remove
    stk2 = make_stack(seq2)       # Do not remove
    stk = stk1 + stk2
    desc = make_empty_stack()
    empty = make_empty_stack()

    while size(stk) > 0:

        if peek(stk) == minim(stk):
            push(desc, pop(stk))

            while size(empty) > 0:
                push(stk, pop(empty))

        else:
            push(empty, pop(stk))

    return desc
            
        
        
        
    


# In[ ]:


##print(merge([7,5,3,1],[9,8,6,5,4,2]))


# In[ ]:


##print(merge('YUSNJIHC','VONNIA'))


# ## Question 3 : Queue ADT  [8 marks]

# In[ ]:


def make_queue():
    return []

def enqueue(queue, item):
    queue.append(item)
    return queue

def dequeue(queue):
    if len(queue) == 0:
        return None
    else:
        return queue.pop(0)

def size(queue):
    if len(queue) == 0:
        return None
    else:
        return len(queue)


# In[ ]:
lst = make_queue()
print(enqueue(lst, 1))
print(enqueue(lst, 2))
print(enqueue(lst, 3))
print(enqueue(lst, 4))
print(dequeue(lst))
print(lst)
print(size(lst))
# Write your test cases :



# ## Question 4 : Application of Queue ADT : Buffer  [5 marks]
# 
# Write a program code to:
# 
# ·         construct a new empty queue named buffer
# 
# ·         add three test data into the buffer
# 
# ·         remove and output two elements from buffer
# 
# ·         output the size of the buffer

# In[ ]:


# Write your program code:
buffer = make_queue()
enqueue(buffer, 123)
enqueue(buffer, 'abc')
enqueue(buffer, True)
##print(buffer)
##print(dequeue(buffer))
##print(dequeue(buffer))
##print(size(buffer))



