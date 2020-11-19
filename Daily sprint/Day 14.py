import datetime
import calendar

def whatday(date, mth):
    month = ['Jan', 'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i in range(len(month)):
        if month[i] == mth:
            mnth = i+1
            break

    year = 2017
    born = datetime.date(year, mnth, date) 
    return born.strftime("%A")[:3]




print(whatday(1,'Jun'))
print(whatday(28,'Feb'))
print(whatday(31,'Dec'))


