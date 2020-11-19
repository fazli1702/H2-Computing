import datetime
import calendar

def whatday(date, mth, year):
    month = ['Jan', 'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i in range(len(month)):
        if month[i] == mth:
            mnth = i+1
            break

    born = datetime.date(year, mnth, date) 
    return born.strftime("%A")[:3]


print(whatday(12,'Dec',2017))
print(whatday(14,'Feb',2021))
print(whatday(31,'Dec',2055))

    
