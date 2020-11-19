#question 1
import csv

## Modify the following code to import the class_list.csv file:
def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows
    
table = read_csv("class_list.csv")
class_list = table


##print(class_list)
##print(class_list[2])
##print(len(class_list))






#question 2
def name(tup):
    return tup[1]

def binary_search(lst, student):
    l = 0
    h = len(lst) - 1
    while l <= h:
        m = (l + h) // 2
        if student == name(lst[m]):
            return lst[m][0]
        elif student < name(lst[m]):        #LHS
            h = m - 1
        else:                               #RHS
            l = m + 1                       
    return None

##print(binary_search(class_list, 'PATEL KRISH KADAMB'))
##print(binary_search(class_list, 'AHMAD SYAFIQ B ABD RAZAK'))
##print(binary_search(class_list, 'JACK'))
