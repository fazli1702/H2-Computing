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


def get_real(z): #z1 and z2 can be either cartesian or polar form
    if z[2] == True:
        return z[0]
    else:
        polar2cart(z[0],z[1])
        return z[0]
        




def get_img(z): #z1 and z2 can be either cartesian or polar form
    if z[2] == True:
        return z[1]
    else:
        polar2cart(z[0], z[1])
        return z[0]




def add(z1, z2): #z1 and z2 can be either cartesian or polar form
    if z1[2] == True and z2[2] == True:
        real = get_real(z1) + get_real(z2)
        img = get_img(z1) + get_img(z2)
        return make_cart(real, img)
    elif z1[2] == False:
        polar2cart(z1[0], z1[1])
        real = get_real(z1) + get_real(z2)
        img = get_img(z1) + get_img(z2)
        return make_cart(real, img)
    elif z2[2] == False:
        polar2cart(z2[0], z2[1])
        real = get_real(z1) + get_real(z2)
        img = get_img(z1) + get_img(z2)
        return make_cart(real, img)
    else:
        polar2cart(z2[0], z2[1])
        polar2cart(z1[0], z1[1])
        real = get_real(z1) + get_real(z2)
        img = get_img(z1) + get_img(z2)
        return make_cart(real, img)



def subtract(z1, z2): #z1 and z2 can be either cartesian or polar form
    if z1[2] == True and z2[2] == True:    
        real = get_real(z1) - get_real(z2)
        img = get_img(z1) - get_img(z2)
        return make_cart(real, img)
    elif z1[2] == False:
        polar2cart(z1[0], z1[1])
        real = get_real(z1) - get_real(z2)
        img = get_img(z1) - get_img(z2)
        return make_cart(real, img)
    elif z2[2] == False:
        polar2cart(z2[0], z2[1])
        real = get_real(z1) - get_real(z2)
        img = get_img(z1) - get_img(z2)
        return make_cart(real, img)
    else:
        polar2cart(z2[0], z2[1])
        polar2cart(z1[0], z1[1])
        real = get_real(z1) - get_real(z2)
        img = get_img(z1) - get_img(z2)
        return make_cart(real, img)




def multiply(z1, z2): #z1 and z2 can be either cartesian or polar form
    if z1[2] == True and z2[2] == True:    
        real = (get_real(z1) * get_real(z2)) - (get_img(z1) * get_img(z2))
        img = (get_real(z1) * get_img(z2)) + (get_real(z2) * get_img(z1))
        return make_cart(real, img)
    elif z1[2] == False:
        polar2cart(z1[0], z1[1])
        real = (get_real(z1) * get_real(z2)) - (get_img(z1) * get_img(z2))
        img = (get_real(z1) * get_img(z2)) + (get_real(z2) * get_img(z1))
        return make_cart(real, img)
    elif z2[2] == False:
        polar2cart(z2[0], z2[1])
        real = (get_real(z1) * get_real(z2)) - (get_img(z1) * get_img(z2))
        img = (get_real(z1) * get_img(z2)) + (get_real(z2) * get_img(z1))
        return make_cart(real, img)
    else:
        polar2cart(z2[0], z2[1])
        polar2cart(z1[0], z1[1])
        real = (get_real(z1) * get_real(z2)) - (get_img(z1) * get_img(z2))
        img = (get_real(z1) * get_img(z2)) + (get_real(z2) * get_img(z1))
        return make_cart(real, img)





def divide(z1, z2): #z1 and z2 can be either cartesian or polar form
    if z1[2] == True and z2[2] == True:    
        real = ((get_real(z1) * get_real(z2)) + (get_img(z1) * get_img(z2))) / ((get_real(z2)**2) + (get_img(z2)**2))
        img = ((get_img(z1) * get_real(z2)) - (get_real(z1) * get_img(z2)) / ((get_real(z2)**2) + (get_img(z2)**2))) 
        return make_cart(real, img)
    elif z1[2] == False:
        polar2cart(z1[0], z1[1])
        real = ((get_real(z1) * get_real(z2)) + (get_img(z1) * get_img(z2))) / ((get_real(z2)**2) + (get_img(z2)**2))
        img = ((get_img(z1) * get_real(z2)) - (get_real(z1) * get_img(z2)) / ((get_real(z2)**2) + (get_img(z2)**2))) 
        return make_cart(real, img)
    elif z2[2] == False:
        polar2cart(z2[0], z2[1])
        real = ((get_real(z1) * get_real(z2)) + (get_img(z1) * get_img(z2))) / ((get_real(z2)**2) + (get_img(z2)**2))
        img = ((get_img(z1) * get_real(z2)) - (get_real(z1) * get_img(z2)) / ((get_real(z2)**2) + (get_img(z2)**2))) 
        return make_cart(real, img)
    else:
        polar2cart(z2[0], z2[1])
        polar2cart(z1[0], z1[1])
        real = ((get_real(z1) * get_real(z2)) + (get_img(z1) * get_img(z2))) / ((get_real(z2)**2) + (get_img(z2)**2))
        img = ((get_img(z1) * get_real(z2)) - (get_real(z1) * get_img(z2)) / ((get_real(z2)**2) + (get_img(z2)**2))) 
        return make_cart(real, img)




def power(z, n): #taking z to be in any form, calculates z^n and returns the result as polar form.
    if z[2] == False:
        mod = get_mod(z) ** n
        arg = principal_arg(get_arg(z) * n)
        return make_polar(mod, arg)
    else:
        cart2polar(z[0], z[1])
        mod = get_mod(z) ** n
        arg = principal_arg(get_arg(z) * n)
        return make_polar(mod, arg)
        
