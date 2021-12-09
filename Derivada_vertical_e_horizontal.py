from math import *

def funcao_3(x,d):
    res = []
    while x < 6*pi:
        y = -7*cos(x)+(28/3)*cos(7*x/3)
        if y <= 0.00001 and y >= -0.00001:
            res.append(x)
        x+=d
    return res

print (funcao_3(0, 0.000001))
