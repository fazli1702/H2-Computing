#question 1
###Insert import queue_module here:####
from queue_module import*

##### construct a queue, my_queue
###remove the pass and write your command statement
my_queue = make_empty_queue()
###'Jane' joins the queue
enqueue(my_queue, 'Jane')
###'Asyraf' joins the queue
enqueue(my_queue, 'Asyraf')
###Cafe out of coffee. All customers left the queue.
clear(my_queue)
###'Sam' joins the queue
enqueue(my_queue, 'Sam')
###'Sally' joins the queue
enqueue(my_queue, 'Sally')
### Served a customer
dequeue(my_queue)
### 'Wen Jie' joins the queue
enqueue(my_queue, 'Wen Jie')
###'Penelope' joins the queue
enqueue(my_queue, 'Penelope')
### 'Thor' joins the queue
enqueue(my_queue, 'Thor')
### Served a customer
dequeue(my_queue)
### 'Loki' joins the queue
enqueue(my_queue, 'Loki')
###Served a customer
dequeue(my_queue)
### manager asked for the size of the queue. Assign it to size1
size1 = size(my_queue)
### Served a customer
dequeue(my_queue)
### 'Tony' joins the queue
enqueue(my_queue, 'Tony')
### 'Bruce' joins the queue
enqueue(my_queue, 'Bruce')
### Served 2 customers
dequeue(my_queue)
dequeue(my_queue)

### manager asked for the size of the queue. Assign it to size2
size2 = size(my_queue)



##print(size1)
##print(size2)
##print(my_queue)








#question 2
######Network printer ADT ######
####import queue_module here:
from queue_module import*

####Constructors###########
def make_print_queue():
    return make_empty_queue()

#####Modifiers##########
def send_job(queue,job):
    enqueue(queue, job)
    return queue


def print_job(queue):
    if len(queue) == 0:
        return None
    else:
        return dequeue(queue)


def cancel_job(queue,job):
    if queue.count(job) == 0:
        return None
    elif queue.count(job) == 1:
        queue.remove(job)
        return queue
    else:
        while queue.count(job) > 1:
            queue.remove(job)
        return queue
        
            

def clear_all(queue):
    clear(queue)


######Accessors#########
def next_job(queue):
    return front(queue)


def size(queue):
    return len(queue)


def is_empty(queue):
    return is_empty_queue(queue)


######################################
#######Do not modify the test cases below####
                        
q1=make_print_queue()
empty1=is_empty(q1)
send_job(q1,"phys quiz")
send_job(q1,"maths quiz")
send_job(q1,"chem quiz")
send_job(q1,"econs quiz")
cancel_job(q1,"econs quiz")
print1=print_job(q1)
size1=size(q1)
next1= next_job(q1)



##print(empty1)
##print(size1)
##print(print1)
##print(next1)













#question 3
#####Construct an empty print queue for my_printer and jammed_queue:
my_printer = make_print_queue()

jammed_jobs = make_print_queue()


##### define paper_jam here:
def paper_jam(jobs):
    jam = make_print_queue()
    
    for job in jobs:
        send_job(my_printer, job)
        if size(my_printer) == 7:
            send_job(jammed_jobs, job)
            send_job(jam, job)
            clear_all(my_printer)
        else:
            continue     
    return jam  
    
            
    






###########Do NOT remove/modify the test cases##############################
jam1=paper_jam([1,2,3,4,5,6,7,8,9,10,11,12,13])
size1=size(jammed_jobs)
jam2=paper_jam([14,15,16,17,18])
size2=size(jammed_jobs)
jam3=paper_jam(['phys','chem','gp','maths','geo'])


##print(jammed_jobs)
##print(size1)
##print(size2)
##print(jam1)
##print(jam2)
##print(jam3)










#question 4
def current_song(n, playlist):
    music = make_empty_queue()
    for song in playlist:
        enqueue(music, song)

    if n < 4:
        return front(music)

    else:
        for i in range(n // 4):
            enqueue(music, dequeue(music))
        
        return front(music)
    



jay_chou = ['silent', 'rainbow', 'nocturne', 'excuse']
MJ = ['Thriller', 'Billie Jean', 'Smooth Criminal', 'Black or White', 'Dangerous']

##print(current_song(90, jay_chou))
##print(current_song(45, jay_chou))












#question 5
def who_wins(m, players):
    winner = make_empty_queue()
    counter = 0
    for player in players:
        enqueue(winner, player)

    while size(winner) > m-1:

        if counter == m:
            dequeue(winner)
            counter = 0

        else:
            counter += 1
            enqueue(winner, dequeue(winner))

    return winner



        
        
            


print(who_wins(2, ['poo', 'ste', 'sim', 'nic', 'luo', 'ibr', 'sie', 'zhu']))
print(set(who_wins(3, ['val', 'hel', 'jam', 'jin', 'tze', 'eli', 'zha', 'lic'])))          
