from math import *

def curva(t):
    lis = []
    x = 7*cos(t) - 4*cos(7*t/3)
    y = 7*sin(t) - 4*sin(7*t/3)
    lis.append(x)
    lis.append(y)
    return lis

print(curva(1.044078000004292))