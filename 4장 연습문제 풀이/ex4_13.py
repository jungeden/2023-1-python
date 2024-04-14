#ex4_13

π=3.14
def cube(s): #정육면체 부피 
    return s**3

def rectangular_p(w,h,l): #직육면체 부피 
    return l*w*h

def cone(r,h): #원뿔 부피 
    return (1/3)*π*(r**2)*h

def sphere(r): #구 부피 
    return (4/3)*π*(r**3)

def cylinder(r,h): #원기둥 부피 
    return π*(r**2)*h


print('(1) : {}'.format(cube(12)))
print('(2) : {}'.format(cube(20)))
print('(3) : {}'.format(rectangular_p(3,5,6)))
print('(4) : {}'.format(cone(20,10)))
print('(5) : {}'.format(sphere(15)))
print('(6) : {}'.format(cylinder(20,10)))


