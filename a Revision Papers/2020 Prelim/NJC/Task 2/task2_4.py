import json

def isInside(restaurants, r):
    for ele in restaurants:
        if ele[0] == r:
            return True
    return False

def read():
    with open('RESTAURANTS.JSON') as f:
        data = json.load(f)
        restaurants = []
        for ele in data:
            if not isInside(restaurants, ele['name']):
                name = ele['name']

                if type(ele['rating']) == str:  # no rating
                    restaurants.append([ele['name'], 0])
                else:  # have rating
                    restaurants.append([ele['name'], ele['rating']])
                    
    return restaurants


def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    lst = []
    while len(left) != 0 and len(right) != 0:
        if left[0][1] > right[0][1]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
            
    if len(left) != 0:
        lst += left
        
    if len(right) != 0:
        lst += right
        
    return lst


restaurants = read()
sorted_restaurants = mergeSort(restaurants)

import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)

# create db
db = client.get_database('Entertainment')
col = db.get_collection('restaurants')

# insert sorted data
col.insert_many(sorted_restaurants)


