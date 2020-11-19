import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('Clinic')
col = db.get_collection('Patient')


def get_input():
    while True:
        name = input('Patient name:')
        valid = True
        for ele in name:
            if not (ele.isalpha() or ele == ' '):
                valid = False
                break
        if valid:
            break  

    while True:
        date = input('Appointment Date <DDMMYYYY>:')
        if len(date) == 8 and date.isdigit():
            day, month, year = date[:2], date[2:4], date[4:]
            if 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
                break

    while True:
        start = input('Appointment Start Time <HHMM>:')
        if len(start) == 4 and start.isdigit():
            h, m = start[:2], start[2:]
            if 1 <= int(h) <= 24 and 0 <= int(m) <= 59:
                break

    while True:
        doctor = input('Doctor to be Assigned:')
        valid = True
        for ele in name:
            if not (ele.isalpha() or ele == ' '):
                valid = False
                break
        if valid:
            break

    return name, date, start, doctor



def main():
    name, date, start, doctor = get_input()
    IDs = []
    for ele in col.find():
        if ele['PatientID'] not in IDs:
            IDs.append(ele['PatientID'])
    IDs.sort()
    newID = int(IDs[-1]) + 1

    info = {'PatientID':newID,
            'Name':name,
            'Appointment_Date':date,
            'Appointment_Start_Time':start,
            'Doctor_Assigned':doctor
            }
    col.insert_one(info)
