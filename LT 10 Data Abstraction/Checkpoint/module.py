## You need not open to read this file ##

import csv

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for name, gender, ht_inch, wt_pd, ht_m, wt_kg in file_reader:
            rows += ((name, gender, float(ht_inch), float(wt_pd), float(ht_m), float(wt_kg)), )
    return rows

def get_name(person):
    return person[0]

def get_gender(person):
    return person[1]

def get_height(person):
    return person[4]

def get_height2(person):
    return person[2]

def get_weight(person):
    return person[5]

def get_weight2(person):
    return person[3]

def get_size(table):
    return len(table)

