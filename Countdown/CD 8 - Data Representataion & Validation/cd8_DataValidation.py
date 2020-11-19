'''
1 - SBA1234 - 0 - Valid registration Number
2 - SBA12345 - 1- Length not 7
3 - STBLW43 - 2 - Last 4 characters are not digits
4 - SC24567 - 3 - 2nd & 3rd characters not letters
5 - SIB1234 - 4 - 2nd & 3rd letters are invalid letters
6 - TAB1234 - 5 - not a private vehicle
'''

def ValidateRegNo(ThisRegNo):
    if len(ThisRegNo) != 7:
        return 1
    elif not ThisRegNo[3:].isdigit():
        return 2
    elif not ThisRegNo[1:3].isalpha():
        return 3
    elif 'I' in ThisRegNo[1:3] or 'o' in ThisRegNo[1:3]:
        return 4
    elif ThisRegNo[0] != 'S':
        return 5
    else:
        return 0

def main():
    reg = input('Enter registration number')
    i = ValidateRegNo(reg)
    if i == 0:
        print('Valid Registration Number')
    elif i == 1:
        print('Invalid: Lenght not 7')
    elif i == 2:
        print('Invalid: Last 4 characters not letters')
    elif i == 3:
        print('Invalid: 2nd & 3rd characters not letters')
    elif i == 4:
        print('Invalid: 2nd & 3rd letters are invalid letters')
    else:
        print('Invalid: Not a private vehicle')
    


class PassengerVehicle():
    def __init__(self, RegNo, NoOfSeats, VehicleType):
        self.RegNo = RegNo
        self.NoOfSeats = NoOfSeats
        self.VehicleType = VehicleType
    
    def get_RegNo(self):
        return self.RegNo
    def get_NoOfSeats(self):
        return self.NoOfSeats
    def get_VehicleType(self):
        return self.VehicleType
    
    def set_RegNo(self, new):
        self.RegNo = new
    def set_NoOfSeats(self, new):
        self.NoOfSeats = new
    def set_VehicleType(self, new):
        self.VehicleType = new
        
    def display(self):
        print('\n\n')
        print('RegNo: ', self.RegNo)
        print('NoOfSeats: ', self.NoOfSeats)
        print('VehicleType: ', self.VehicleType)    

class Bus(PassengerVehicle):
    def __init__(self, RegNo, NoOfSeats, VehicleType):
        super().__init__(RegNo, NoOfSeats, VehicleType)
        self.MaxStanding = None
        
    def get_MaxStanding(self):
        return self.MaxStanding

    def set_MaxStanding(self, data):
        self.MaxStanding = data

    def display(self):              # not required
        super().display()
        print('MaxStanding: ', self.MaxStanding)
        
class Coach(PassengerVehicle):
    def __init__(self, RegNo, NoOfSeats, VehicleType):
        super().__init__(RegNo, NoOfSeats, VehicleType)
        self.MaxStanding = 0
        self.SeatBeltsFitted = None   # boolean
        
    def get_MaxStanding(self):
        return self.MaxStanding
          
    def get_SeatBeltsFitted(self):
        return self.SeatBeltsFitted

    def set_SeatBeltsFitted(self, data):
        self.SeatBeltsFitted = data
        
    def display(self):              # not required
        super().display()
        print('MaxStanding: ', self.MaxStanding)
        print('SeatBeltsFitted: ', self.SeatBeltsFitted)
        




# Step 5 : Final touch up, include 1st line in UVEHICLE.dat

def main2():

    file = open('VEHICLE.dat')
    lines = file.readlines()
    
    output = open('UVEHICLE.dat', 'w')    # create a new dat file
    output.write(lines[0])                # copy from 1st line in 'VEHICLE.dat'
    
    for line in lines[1:]:
        [Reg, Seat, Type] = line.strip().split('|')
        
        if Type == 'B':
            vehicle = Bus(Reg, Seat, Type)
            vehicle.display()
            
            while True:
                entry = input('Max Standing <15 or less> : ')
                if entry.isdigit():
                    entry = int(entry)
                    if 0 <= entry <= 15:
                        break
            
            vehicle.set_MaxStanding(entry)
            
            #vehicle.display()  # not required
            
            output.write(vehicle.get_RegNo()+'|'\
                         +str(vehicle.get_NoOfSeats())+'|'\
                         +vehicle.get_VehicleType()+'|'\
                         +str(vehicle.get_MaxStanding())+'\n')       # include newline
            
        
        elif Type == 'C':
            vehicle = Coach(Reg, Seat, Type)
            vehicle.display()
            
            while True:
                entry = input('Seat belts fitted (Y/N): ').upper()
                if entry == 'Y':
                    entry = True
                    break
                elif entry == 'N':
                    entry = False
                    break
            vehicle.set_SeatBeltsFitted(entry)
            #vehicle.display()  # not required
            
            output.write(vehicle.get_RegNo()+'|'\
                         +str(vehicle.get_NoOfSeats())+'|'\
                         +vehicle.get_VehicleType()+'|'\
                         +str(vehicle.get_MaxStanding())+'|'\
                         +str(vehicle.get_SeatBeltsFitted())+'\n')  # include newline
            
    file.close()
    output.close()

main2()
