#question 1
class Rectangle:
    def __init__(self, base, side):
        self.base = base
        self.side = side

    def get_base(self):
        return self.base

    def get_side(self):
        return self.side

    def set_base(self, new_base):
        self.base = new_base

    def set_side(self, new_side):
        self.side = new_side

    def calc_perimeter(self):
        p = (self.base * 2) + (self.side * 2)
        return p

    def calc_area(self):
        a = self.base * self.side
        return a

    def is_regular(self):
        return self.side == self.base


r1=Rectangle(6,7)
b1=r1.get_base()
s1=r1.get_side()
a1=r1.calc_area()
p1=r1.calc_perimeter()
reg=r1.is_regular()


##print(b1)
##print(s1)
##print(a1)
##print(p1)
##print(reg)








#quuestion 2
import math

class Rhombus:
    def __init__(self, side, angle):
        self.side = side
        self.angle = angle

    def get_side(self):
        return self.side

    def get_angle(self):
        return self.angle

    def set_side(self, new_side):
        self.side = new_side

    def set_angle(self, new_angle):
        self.angle = new_angle

    def calc_perimeter(self):
        p = self.side * 4
        return p

    def calc_area(self):
        a = self.side * (self.side * math.sin(self.angle * (math.pi/180)))
        return a

    def is_square(self):
        return self.angle == 90


r1=Rhombus(6,45) #side 6, angle 45

s1=r1.get_side()
t1=r1.get_angle()
a1=r1.calc_area()
p1=r1.calc_perimeter()
reg=r1.is_square()

##print(s1)
##print(round(a1, 2))
##print(p1)
##print(t1)
##print(reg)







#question 3
class Parallelogram:
    def __init__(self, base, side, angle):
        self.base = base
        self.side = side
        self.angle = angle

    #getters

    def get_base(self):
        return self.base

    def get_side(self):
        return self.side

    def get_angle(self):
        return self.angle

    #setters

    def set_base(self, new_base):
        self.base = new_base

    def set_side(self, new_side):
        self.side = new_side

    def set_angle(self, new_angle):
        self.angle = new_angle

    #utilities

    def calc_perimeter(self):
        p = (self.base * 2) + (self.side * 2)
        return p

    def calc_area(self):
        a = self.side * (self.side * math.sin(self.angle * (math.pi/180)))
        return a

    def is_regular(self):
        return self.side == self.base
    

##p1=Parallelogram(3,4,90)
##s1=p1.get_side()
##a1=p1.get_angle()
##p1.set_base(4)
##b1=p1.get_base()
##peri1=p1.calc_perimeter()
##area1=p1.calc_area()
##reg=p1.is_regular()

##print(s1)
##print(b1)
##print(a1)
##print(peri1)
##print(area1)
##print(reg)


#question 4

##Rectangle subclass
class Rectangle(Parallelogram):
    def __init__(self, base, side):
        super().__init__(base, side, angle = 90)
    


##Rhombus subclass
class Rhombus(Parallelogram):
    def __init__(self, side, angle):
        super().__init__(side, side, angle)

    def is_square(self):
        return self.get_angle() == 90

    def set_side(self, new_side):
        self.side = side
        self.base = side

    def set_base(self, new_base):
        self.base = new_base
        self.side = new_base

    

        

rec1=Rectangle(3,4)
s1=rec1.get_side()
rec1.set_base(4)
b1=rec1.get_base()
a1=rec1.get_angle()
peri1=rec1.calc_perimeter()
area1=rec1.calc_area()
reg1=rec1.is_regular()

rh2=Rhombus(3,120)
reg2=rh2.is_square()
s2=rh2.get_side()
rh2.set_base(4)
b2=rh2.get_base()
a2=rh2.get_angle()
peri2=rh2.calc_perimeter()
area2=rh2.calc_area()


##print(s1)
##print(b1)
##print(a1)
##print(peri1)
##print(area1)
##print(reg1)








#question 5
class Rectangle(Parallelogram):
    def __init__(self, base, side):
        super().__init__(base, side, 90)

    def calc_area(self):
        return super().get_side() * super().get_base()


rec1=Rectangle(3,4)
s1=rec1.get_side()
rec1.set_base(4)
b1=rec1.get_base()
a1=rec1.get_angle()
peri1=rec1.calc_perimeter()
area1=rec1.calc_area()
reg1=rec1.is_regular()








#question 6
##LibraryItem base class
import datetime

class LibraryItem:
    #constructor
    def __init__(self, title, author_artist, itemID, OnLoan, DueDate):
        self.title = title
        self.author_artist = author_artist
        self.itemID = itemID
        self.OnLoan = False
        self.DueDate = None
        
    
    #getters
    def get_title(self):
        return self.title

    def get_author_artist(self):
        return self.author_artist

    def get_itemID(self):
        return self.itemID

    def get_OnLoan(self):
        return self.OnLoan

    def get_DueDate(self):
        return self.DueDate

    #setters
    
    
    
    #utility
    def Borrowing(self):
        self.OnLoan = True
        self.DueDate = datetime.date.today() + datetime.timedelta(weeks=3)

    def Returning(self):
        self.OnLoan = False
        self.DueDate = None

    def PrintDetails(self):
        print('Title:' + str(self.title))
        print('Author/Artist:' + str(self.author_artist))
        print('Item ID:' + str(self.itemID))
        print('On Loan:' + str(self.OnLoan))
        print('Due Date:' + str(self.DueDate))
        
    


##Book subclass

class Book(LibraryItem):
    #constructor
    def __init__(self, title, author, itemID):
        OnLoan = False
        DueDate = None
        super().__init__(title, author, itemID, OnLoan, DueDate)
        self.IsRequested = False
    
    #getters
    def get_IsRequested(self):
        return self.IsRequested


    #setters
    def set_IsRequested(self):
        self.IsRequested = True
    
    
    #utility
    



##CD subclass

class CD(LibraryItem):
    #constructor
    def __init__(self, title, artist, itemID):
        OnLoan = False
        DueDate = None
        super().__init__(title, artist, itemID, OnLoan, DueDate)
        self.genre = None
    
    #getters
    def get_genre(self):
        return self.genre

    #setters    
    def set_genre(self, new_genre):
        self.genre = new_genre
    
    #utility



#####Do not remove:
Book1=Book("Harry Potter & the sorcerer's stone", "JK Rowling", "978-3-16-148410-0")
title1=Book1.get_title()
Book1.Borrowing()
date1=Book1.get_DueDate()
ISBN1=Book1.get_itemID()
Book1.set_IsRequested()
requested=Book1.get_IsRequested()
Book1.Returning()
loan1=Book1.get_OnLoan()


CD1=CD("Purpose", "Justin Bieber", "123-3-16-148410-0")
CD1.set_genre("pop")
genre1=CD1.get_genre()
cdtitle1=CD1.get_title()
CD1.Borrowing()
cddate1=CD1.get_DueDate()
cdID1=CD1.get_itemID()
CD1.Returning()
CD1=CD1.get_OnLoan()


print(title1)
print(date1)
print(ISBN1)
print(loan1)
print(requested)
print(genre1)
print(cdtitle1)

