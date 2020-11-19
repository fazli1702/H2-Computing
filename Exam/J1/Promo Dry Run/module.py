### Question 4

import csv

def read_csv(filename):
    rows = ()
    with open(filename) as file:
        for ele in csv.reader(file):
            rows += (ele,)
        return rows

def get_speed(observation):
    return observation[0]

def get_stopdist(observation):
    return observation[1]
