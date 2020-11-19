###########
# BST (Another implementation) #
###########
###########
###Initialized beforehand, do not modify:####
TreeData=['','','','','','','','','','']
LeftPtr=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
RightPtr=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
RootPtr=-1
NextEmptyIndex=0


def compare(data, data_i, i):
    
    global RootPtr
    global TreeData
    global LeftPtr
    global RightPtr
    global NextEmptyIndex

    if data < TreeData[i]:
        if LeftPtr[i] != -1:
            compare(data, data_i, LeftPtr[i])
        else:
            LeftPtr[i] = data_i

    else:
        if RightPtr[i] != -1:
            compare(data, data_i, RightPtr[i])
        else:
            RightPtr[i] = data_i 




def insert(data):
    
    global RootPtr
    global TreeData
    global LeftPtr
    global RightPtr
    global NextEmptyIndex

    if TreeData[-1] != '':
        return 'Tree is full'
    
    elif RootPtr == -1: ##if Tree is an empty tree
        #place data into TreeData at the position NextEmptyIndex
        TreeData[NextEmptyIndex] = data
        
        #update the RootPtr to 0 to signify that the Tree is now not empty
        RootPtr = 0
        
        #update the NextEmptyIndex to 1
        NextEmptyIndex += 1
    
    
    ##YOUR TASK#####
    else:
        ##inserting into Tree with one existing data (i.e Root)
        TreeData[NextEmptyIndex] = data
        
        ##compare new data with data at root
        ##if data < data at root, we update the LeftPtr of the root to the value given by NextEmptyIndex
        if data < TreeData[RootPtr]:
            if LeftPtr[RootPtr] != -1:
                compare(data, NextEmptyIndex, LeftPtr[RootPtr])
            else:
                LeftPtr[RootPtr] = NextEmptyIndex
            
            
        ##else, we update the RightPtr of the root to the value given by the NextEmptyIndex.
        else:
            if RightPtr[RootPtr] != -1:
                compare(data, NextEmptyIndex, RightPtr[RootPtr])
            else:
                RightPtr[RootPtr] = NextEmptyIndex
        ##lastly, update the NextEmptyIndex, increasing its value by 1
        NextEmptyIndex += 1
         

    
####Do NOT remove/modify#####
##a1=RootPtr
##a2=NextEmptyIndex
##insert('hello')
##b1=RootPtr
##b2=NextEmptyIndex
##c=TreeData[RootPtr]
##c2=RightPtr[RootPtr]
##insert('world')
##d1=NextEmptyIndex
##d2=RightPtr[RootPtr]
##insert('zoo')
##e1=NextEmptyIndex
##e2=RightPtr[RightPtr[RootPtr]]


##print(a1)
##print(a2)
##print(b1)
##print(b2)
##print(c)
##print(d1)
##print(c2)
##print(d2)
##print(e1)
##print(e2)


insert('hello')
insert('world')
insert('zoo')
insert('cow')
insert('apple')
insert('bob')
insert('cook')
insert('money')
insert('coins')
insert('life')



print('TreeData:', TreeData)
print('LeftPtr:', LeftPtr)
print('RightPtr:', RightPtr)
