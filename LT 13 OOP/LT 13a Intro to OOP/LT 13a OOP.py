    #question 2

###Constructors
def make_person(id,name,hp,dob,email):
    return (id, name, hp, dob, email)


###accessors
def get_id(person): 
    return person[0]

def get_name(person):
    return person[1]
    
def get_hp(person):
    return person[2]
    
def get_dob(person):
    return person[3]
    
def get_email(person):
    return person[4]



###modifiers

def set_hp(person,hp):
    return make_person(get_id(person), get_name(person), hp, get_dob(person), get_email(person))
    
def set_email(person,email):
    return make_person(get_id(person), get_name(person), get_hp(person), get_dob(person), email)





########Do Not remove/modify#######
James= make_person('C1', 'James', '93344556', '01-02-1979','james123@gmail.com')
Lily= make_person('C2', 'Lily', '89903552', '21-11-1983','lilyangle21@gmail.com')
name1=get_name(James)
email2=get_email(Lily)
Lily=set_hp(Lily, '91127654')
hp2=get_hp(Lily)
James=set_email(James,'james@gmail.com')
email1=get_email(James)




##print(name1)
##print(email2)
##print(hp2)
##print(email1)











#question 3
##1) create 3 new customer contacts 
Mickey= make_person('C3', 'Mickey', '98765412', '18-11-1982', 'mickey@disney.com')

Goofy= make_person('C4', 'Goofy', '83041737', '29-12-1975', 'goofy@disney.com')

Donald= make_person('C5', 'Donald', '93280456', '07-06-1973', 'donald@disney.com')

#2) assign the email of Mickey to the variable email3 
email3= get_email(Mickey)

#3) assign the hp of Goofy to the variable hp4
hp4= get_hp(Goofy)

#4) assign the dob of Donald to the variable dob5
dob5= get_dob(Donald)

#5) change the hp of Mickey to 98765413
Mickey= set_hp(Mickey,'98765413')

#6) change the email of Donald to 'donald@gmail.com'
Donald= set_email(Donald, 'donald@gmail.com')



##print(email3)
##print(hp4)
##print(dob5)





#question 6 
#1) instantiate 3 new Person objects, Mickey, Goofy and Donald with the following set of attributes:

#C3, Mickey, 98765412, 18-11-1982, mickey@disney.com (done for you)
#C4, Goofy, 83041737, 29-12-1975, goofy@disney.com
#C5, Donald, 93280456, 07-06-1973, donald@disney.com
##
##Mickey= Person('C3', 'Mickey', '98765412', '18-11-1982', 'mickey@disney.com')
##
##
##Goofy= Person('C4', 'Goofy', '83041737', '29-12-1975', 'goofy@disney.com')
##
##Donald= Person('C5', 'Donald', '93280456', '07-06-1973', 'donald@disney.com')
##
###2) get and assign the email of Mickey to the variable email3 (done for you)
##email3=  Mickey.get_email()   
##
###3) get and assign the hp of Goofy to the variable hp4
##hp4= Goofy.get_hp()
##
###4) get and assign the dob of Donald to the variable dob5
##dob5= Donald.get_dob()
##
###5) change the hp of Mickey to 98765413 (done for you)
##Mickey.set_hp('98765413')
##
###6) change the email of Donald to donald@gmail.com
##Donald.set_email('Donald@gmail.com')








#question 7

##Person class
class Person(object):
    #constructor
    def __init__(self,id,name,hp,dob,email):
        self.id = id
        self.name = name
        self.hp = hp
        self.dob = dob
        self.email = email
    #getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_dob(self):
        return self.dob

    def get_email(self):
        return self.email


    #setters
    def set_id(self, new_id):
        self.id = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_hp(self, new_hp):
        self.hp = new_hp

    def set_dob(self, new_dob):
        self.dob = new_dob

    def set_email(self, new_email):
        self.email = new_email
        
    #utility
    def display(self):
        print('ID:', self.id)
        print('Name:', self.name)
        print('DOB:', self.DOB)
        print('Email:', self.email)
        print('Hp:', self.hp)
    
#####Do not remove:
James= Person('C1', 'James', '93344556', '01-02-1979','james123@gmail.com')
Lily= Person('C2', 'Lily', '89903552', '21-11-1983','lilyangle21@gmail.com')
name1=James.get_name()
email2=Lily.get_email()
Lily.set_hp('91127654')
hp2=Lily.get_hp()
name2=Lily.get_name()
hp1=James.get_hp()
James.set_email('james@gmail.com')
email1=James.get_email()

##print(name1)
##print(email1)
##print(email2)
##print(hp2)
