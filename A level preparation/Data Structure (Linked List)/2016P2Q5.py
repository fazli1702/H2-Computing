Data = ['' for i in range(3001)]
Data[0] = None
Ptr = [-1 for i in range(3001)]
Ptr[0] = None

def NextFree():
    global Data
    for i, ele in Data:
        if ele == '':
            return i
    return -1

def InsertListItem(NewSurname : str):
    if NextFree() == -1:
        print('List is full')
    else:
        if StartPtr == 0:
            StartPtr = NextFree()
            Data[StartPtr] = NewSurname
        else:
            Temp = NextFree()
            current = 1
            prev = 0
            found = False

            while not (Found or current == 0):
                if NewSurname < Data[current]:
                    Data[Temp] = NewSurname
                    Ptr[Previous] = Temp
                    Found = True
                else:
                    prev = current
                    current = Ptr[current]

            if current == 0:
                Data[Temp] = NewSurname
                Ptr[Previous] = 0
