#question 1
##Circle class
import math

class Circle:
    #constructor
    def __init__(self, radius):
        self.radius = radius
    
    #getters
    def get_radius(self):
        return self.radius

    #setters    
    def set_radius(self, new_radius):
        self.radius = new_radius
    
    #utility
    def calc_circumference(self):
        return self.radius * math.pi * 2

    def calc_area(self):
        return math.pi * (self.radius ** 2)

    
C1=Circle(5)
r=C1.get_radius()
C1.set_radius(7)
a=C1.calc_area()
c=C1.calc_circumference()


##print(r)
##print(a)
##print(c)



#question 2
#circle1: a circle of radius 10
circle1 = Circle(10)

#circle2: a circle of radius 20
circle2 = Circle(20)

#circle3: a circle of radius 30
circle3 = Circle(30)


##print(type(circle1))









#question 3
##Book class
import datetime

class Book:
    #constructor
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.OnLoan = False
        self.DueDate = ''
    
    #getters
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_ISBN(self):
        return self.ISBN

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

    def PrintDetails(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('ISBN:', self.ISBN)
        print('On Loan:', self.OnLoan)
        print('Due Date:', self.DueDate)



Book1=Book("Harry Potter & the sorcerer's stone", "JK Rowling", "978-3-16-148410-0")
title1=Book1.get_title()
Book1.Borrowing()
date1=Book1.get_DueDate()
ISBN1=Book1.get_ISBN()


print(title1)
print(date1)
print(ISBN1)
print(loan1)
