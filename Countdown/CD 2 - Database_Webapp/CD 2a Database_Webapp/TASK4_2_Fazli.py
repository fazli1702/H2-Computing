import sqlite3

def laptop():
    Type = 'Laptop'
    # read file
    with open('LAPTOPS.txt') as f:
        data = f.readlines()
        laptops = [ele.strip().split(',') for ele in data]

    # insert into db
    db = sqlite3.connect('equipment.db')
    c = db.cursor()

    for SerialNumber, Model, Location, DateOfPurchase, WrittenOff, WeightKg in laptops:
        device_info = [SerialNumber, Type , Model, Location, DateOfPurchase, WrittenOff]
        laptop_info = [SerialNumber, WeightKg]

        # insert into device table
        c.execute('''INSERT INTO Device VALUES 
            (:SerialNumber, :Type, :Model, :Location, :DateOfPurchase, :WrittenOff)''', device_info)
        db.commit()

        # insert into laptop table
        c.execute('''INSERT INTO Laptop VALUES (:SerialNumber, :WeightKg)''', laptop_info)
        db.commit()

    db.close()


def monitor():
    Type = 'Monitor'
    with open('MONITORS.txt') as f:
        data = f.readlines()
        monitor = [ele.strip().split(',') for ele in data]


    db = sqlite3.connect('equipment.db')
    c = db.cursor()

    for SerialNumber, Model, Location, DateOfPurchase, WrittenOff, DateCleaned in monitor:
        device_info = [SerialNumber, Type , Model, Location, DateOfPurchase, WrittenOff]
        monitor_info = [SerialNumber, DateCleaned]

        # insert into device table
        c.execute('''INSERT INTO Device VALUES 
            (:SerialNumber, :Type, :Model, :Location, :DateOfPurchase, :WrittenOff)''', device_info)
        db.commit()

        # insert into monitor table
        c.execute('''INSERT INTO Monitor VALUES (:SerialNumber, :DateCleaned)''', monitor_info)
        db.commit()

    db.close()



def printer():
    Type = 'Printer'
    with open('PRINTERS.txt') as f:
        data = f.readlines()
        printer = [ele.strip().split(',') for ele in data]

    db = sqlite3.connect('equipment.db')
    c = db.cursor()

    for SerialNumber, Model, Location, DateOfPurchase, WrittenOff, Toner, DateChanged in printer:
        device_info = [SerialNumber, Type , Model, Location, DateOfPurchase, WrittenOff]
        printer_info = [SerialNumber, Toner , DateChanged]

        # insert into device table
        c.execute('''INSERT INTO Device VALUES 
            (:SerialNumber, :Type, :Model, :Location, :DateOfPurchase, :WrittenOff)''', device_info)
        db.commit()

        # insert into monitor table
        c.execute('''INSERT INTO Printer VALUES (:SerialNumber, :Toner , :DateChanged)''', printer_info)
        db.commit()

    db.close()



def main():
    laptop()
    monitor()
    printer()
    
main()
