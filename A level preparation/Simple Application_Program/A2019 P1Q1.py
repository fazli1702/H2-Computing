'task 1.1'

with open('TIDES.txt') as f:
    data = f.readlines()
    tides = [row.strip().split() for row in data]

low_height = []
high_height = []
for tide in tides:
    #print(tide)
    if tide[2] == 'LOW':
        low_height.append(tide[3])
    else:
        high_height.append(tide[3])

##print(max(high_height))
##print(min(low_height))


'task 1.2'
tidal_range = []
for i in range(len(tides)-1):
    tide_range = abs(float(tides[i][3])-float(tides[i+1][3]))
    info = (tides[i], tides[i+1], tide_range)
    tidal_range.append(info)

def getFirstTide(tide):
    return tide[0]

def getLastTide(tide):
    return tide[1]

def getTideRange(tide):
    return tide[2]

def getMaxTide(tidal_range):
    maxim = getTideRange(tidal_range[0])
    index = 0
    for i, ele in enumerate(tidal_range):
        if getTideRange(tidal_range[i]) > maxim:
            maxim = getTideRange(tidal_range[i])
            index = i

    return index

##print(getMaxTide(tidal_range))

def getMinTide(tidal_range):
    minim = getTideRange(tidal_range[0])
    index = 0
    for i, ele in enumerate(tidal_range):
        if getTideRange(tidal_range[i]) < minim:
            minim = getTideRange(tidal_range[i])
            index = i

    return index

##print(getMinTide(tidal_range))


# largest tide & date of second tide
max_i = getMaxTide(tidal_range)
max_tide = tidal_range[max_i]
##print(max_tide)
print(getTideRange(max_tide))
print(getLastTide(max_tide)[0])


# smallest tide & date of second tide
min_i = getMinTide(tidal_range)
min_tide = tidal_range[min_i]
##print(min_tide)
print(getTideRange(min_tide))
print(getLastTide(min_tide)[0])

