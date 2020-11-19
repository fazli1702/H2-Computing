def principal_arg(radians):
    pi = 3.141592653589793
    arg = radians%(pi*2)   #make arg be within 0 to 2pi
    if arg > pi:       #if it is in 3rd or 4th quadrant
        arg = arg - (2*pi)  #make it between -pi to 0
    return arg
