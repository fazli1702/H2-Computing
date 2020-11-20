#question 1
#intro
import csv
def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        content = csv.reader(csvfile)
        #next(content)                             # skip the header
        for row in content:
            #print(row)
            rows += (tuple(row), )
    return rows
#table = read_csv("abc.csv")
##print(table)


def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        content = csv.reader(csvfile)
        #next(content)                             # skip the header
        for row in content:
            #print(row)
            rows += (tuple(row), )
    return rows
computing_class = read_csv("result.csv")
##print(table)
 




#question 2
def get_class(student):
    return int(student[0])

def get_name(student):
    return student[1]

def get_gender(student):
    return student[2]

def get_level(student):
    return int(student[3])

def get_score(student):
    return int(student[4])

def size(lst):
    total = 0
    for ele in lst:
        total += 1
    return total


computing_class = read_csv("result.csv")[1:]







#question 3
def total_score(lst):
    total = 0
    for ele in lst:
        total += int(ele[4])
    return total

def ave_score(lst):
    return round(total_score(lst)/size(lst),2)

def ave_level(lst):
    total = 0
    for ele in lst:
        total += int(ele[3])
    return round(total/size(lst),2)

##print(total_score(computing_class))
##print(ave_score(computing_class))
##print(ave_level(computing_class))





#question 4
def gender_list(lst, gender):
    tup = ()
    for ele in lst:
        if get_gender(ele) == gender:
            tup += (get_name(ele),)
    return tup

def class_list(lst, ctg):
    tup = ()
    for ele in lst:
        if get_class(ele) == ctg:
            tup += (get_name(ele),)
    return tup

##print(gender_list(computing_class,'F'))
##print(class_list(computing_class,119))






#question 5
def add_student(lst, ctg, name, gender, level, score):
    tup = (str(ctg), name, gender, str(level), str(score))
    lst += (tup,)
    return lst

new_list = add_student(computing_class, 120, "James", "M", 10, 1449)

##print(new_list[-1])
##print(len(new_list))
##print(len(computing_class))












