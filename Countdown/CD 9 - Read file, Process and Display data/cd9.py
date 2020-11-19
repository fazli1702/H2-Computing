with open('DIVE1.txt') as f:
    data = f.readlines()
    countries = [row.strip().split(',') for row in data]

def find_min(arr):
    minim = arr[0]
    minim_i = 0
    for i, ele in enumerate(arr):
        if ele < minim:
            minim = ele
            minim_i = i
    return minim_i


def find_max(arr):
    maxim = arr[0]
    maxim_i = 0
    for i, ele in enumerate(arr):
        if ele > maxim:
            maxim = ele
            maxim_i = i
    return maxim_i



rank = []
for country in countries:
    scores = [float(ele) for ele in country[2:]]
##    print(scores)
    scores.pop(find_min(scores))
    scores.pop(find_max(scores))
##    print(scores)
    raw = sum(scores)
    dif = float(country[1])
    total = round(raw * dif, 2)
    rank.append([country[0], total])

for j in range(3):
    maxim = rank[0][1]
    maxim_i = 0
    for i, country in enumerate(rank):
        if country[1] > maxim:
            maxim = country[1]
            maxim_i = i
            
    if j == 0:
        print('%-15s %-15s %-15s' % ('Gold:', rank[maxim_i][0], rank[maxim_i][1]))
    elif j == 1:
        print('%-15s %-15s %-15s' % ('Silver:', rank[maxim_i][0], rank[maxim_i][1]))
    elif j == 2:
        print('%-15s %-15s %-15s' % ('Bronze:', rank[maxim_i][0], rank[maxim_i][1]))
    rank.pop(maxim_i)        




with open('DIVE2.txt') as f:
    data = f.readlines()
    countries2 = [row.strip().split(',') for row in data]
    for ele in countries2:
        print(ele)
        print(len(ele))
    
    

