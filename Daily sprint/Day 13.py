def isLeap(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(isLeap(2010))
print(isLeap(2000))
print(isLeap(1800))
print(isLeap(2012))
print(isLeap(2017))             
