from module import principal_arg
from math import*

def make_cart(real, img):    # Constructor
    return [real, img, True] #True for cartesian, False for polar

def is_cart(z): #predicate to check if it is in a cartesian form
    return z[2]

def get_real(z): #returns the real part of complex no z
    return z[0]

def get_img(z): #returns the imaginary part of complex no z
    return z[1]

def set_real(z, num):  #changes the real part of complex no z to num
    z[0] = num
    return z

def set_img(z, num):  #changes the imaginary part of complex no z to num
    z[1] = num
    return z

def print_cmplx(z):
    if z[2]==True: #if cartesian, string is a+bi
        string = str(round(get_real(z),3))+' + '+str(round(get_img(z),3))+'i'
    else:          #if polar, string is re^i(theta)
        string = str(round(z[0],3))+' e^i('+str(round(z[1],3))+')'
    return string

def add(z1, z2): #adds 2 complex numbers and returns the resulting complex no
    real = get_real(z1) + get_real(z2)
    img = get_img(z1) + get_img(z2)
    return make_cart(real, img)

def subtract(z1, z2): #perform z1 - z2 and returns the complex number result
    real = get_real(z1) - get_real(z2)
    img = get_img(z1) - get_img(z2)
    return make_cart(real, img)

def multiply(z1, z2): #perform z1 * z2 and returns the complex number result
    real = (get_real(z1) * get_real(z2)) - (get_img(z1) * get_img(z2))
    img = (get_real(z1) * get_img(z2)) + (get_real(z2) * get_img(z1))
    return make_cart(real, img)

def divide(z1, z2): #perform z1 / z2 and returns the complex number result
    real = ((get_real(z1) * get_real(z2)) + (get_img(z1) * get_img(z2))) / ((get_real(z2)**2) + (get_img(z2)**2))
    img = ((get_img(z1) * get_real(z2)) - (get_real(z1) * get_img(z2)) / ((get_real(z2)**2) + (get_img(z2)**2))) 
    return make_cart(real, img)
           
def mod(z): #returns the modulus of the complex number
    mod = ((get_real(z)**2)+(get_img(z)**2))**(1/2)
    return mod

############Cartesian functions complete#######
############Polar form starts here#############

def arg(z): #returns the argument of the complex number
    a = atan(abs(get_real(z)/get_img(z)))
    if get_real(z) > 0 and get_img(z) > 0:
        return a
    elif get_real(z) > 0 and get_img(z) < 0:
        return pi - a
    elif get_real(z) < 0 and get_img(z) > 0:
        return -a
    else:
        return -(pi -a)

def make_polar(mod, arg):
    return [mod, arg, False]

def is_polar(z):
    return not z[2]
    
def get_mod(z): #returns the modulus of the polar form of the complex number
    return z[0]

def get_arg(z): #returns the arugment of the polar form of the complex number
    return z[1]

def cart2polar(real, img): #converts a cartesian complex number to polar form
    z = make_cart(real, img)
    mod = mod(z)
    arg = arg(z)
    return make_polar(mod, arg)


def polar2cart(mod, arg): #comverts a polar complex number to cartesian form
    z = make_polar(mod, arg) 
    real = get_mod(z) * cos(get_arg(z))
    img = get_mod(z) * sin(get_arg(z))
    return make_cart(real, img)

def power(z, n): #taking z to be in polar form, calculates z^n and returns the result as polar form.
    mod = get_mod(z) ** n
    arg = principal_arg(get_arg(z) * n)
    return make_polar(mod, arg)


### We will test with these constructors
### Do not remove

z1=make_cart(3,4)
z2=make_cart(-5,-12)
z3=make_cart(0,0)
z4=make_cart(-5,2)
z5=make_cart(2,-5)
z6=make_polar(5,2.1)
z7=make_polar(0,2)
z8=make_polar(3.2,-0.3)
z9=make_cart(1,1)
set_real(z9,20)
set_img(z9,-5)




    
