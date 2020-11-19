import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('Clinic')
col = db.get_collection('Patient')

with open('PATIENTS.txt') as f:
    data = f.readlines()
    data = [ele.strip().split(',') for ele in data]


for Id, name, date, start, doctor, room, amount in data:
    info = {'PatientID':Id,
            'Name':name,
            'Appointment_Date':date,
            'Appointment_Start_Time':start,
            'Doctor_Assigned':doctor,
            'Room_Num ber':room,
            'Amount_Charged':amount
            }
    col.insert_one(info)

