import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('OUTLETS')
col = db.get_collection('GEM')

with open('INVENTORY_SERIAL.txt') as f:
    data = f.readlines()
    info = [ele.strip().split('\t') for ele in data]
    for serialNo, name, ptype, pprice, sprice, n in info:
        info2 = {'SerialNo':serialNo,
                 'Name':name,
                 'Type':ptype,
                 'PurchasePrice':pprice,
                 'SellingPrice':sprice,
                 'Quantity':n
                 }
        col.insert_one(info2)
