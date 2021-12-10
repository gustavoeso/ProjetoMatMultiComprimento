from math import *

def funcao_1(x,d):
    res = []
    while x < 0:
        y = -7*(sin(x/2))-4*(sin(7*x/6))
        if y <= 0.00001 and y >= -0.00001:
            res.append(x)
        x+=d
    return res


#print(funcao_1(-18,1e-6))

def funcao_2(x,d):
    res = []
    while x < 0:
        y = 7*cos(3*pi/2)*sin(x/2)-4*cos(3*pi+pi/2)*sin(7*x/6)
        if y == 0:
            res.append(x)
        x+=d
    return res



#print(funcao_2(-18,1e-6))
def funcao_3(x,d):
    res = []
    while x < 0:
        y = -7*(sin(x/2))+4*(sin(7*x/6))
        if y <= 0.00001 and y >= -0.00001:
            res.append(x)
        x+=d
    return res

#print(funcao_3(-18,1e-6))

def funcao_4(x,d):
    res = []
    while x < 0:
        y = 7*(sin(x/2))+4*(sin(7*x/6))
        if y <= 0.00001 and y >= -0.00001:
            res.append(x)
        x+=d
    return res
#print(funcao_4(-18,1e-6))

def funcao_5(x,d):
    res = []
    while x < 0:
        y = 7*(sin(x/2))-4*(sin(7*x/6))
        if y <= 0.00001 and y >= -0.00001:
            res.append(x)
        x+=d
    return res
#print(funcao_5(-18,1e-6))

def soma(a,b):
    y = a+b
    x = y/2
    z = a - x
    return y,x,z
#print(soma(28.274,1.194))


def curva(t):
    lis = []
    x = 7*cos(t) - 4*cos(7*t/3)
    y = 7*sin(t) - 4*sin(7*t/3)
    lis.append(x)
    lis.append(y)
    return lis


#print(curva(14.734))