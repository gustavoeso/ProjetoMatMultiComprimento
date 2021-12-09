import math

sen = math.sin
cos = math.cos
pi = math.pi
sqrt = math.sqrt
v_inicial = 0
v_final = 6*pi
lista = []
lista2 = []

n = 1000000

def funcao(t):
    x = 7*cos(t)-4*cos((7*t)/3)
    y = 7*sen(t)-4*sen((7*t)/3)

    return x, y


h = (v_final - v_inicial) / n

lista.append(funcao(v_inicial))

for i in range(n):
    v_inicial += h
    lista.append(funcao(v_inicial))
    lista2.append(sqrt((lista[0][0] - lista[1][0])**2 + (lista[0][1] - lista[1][1])**2))
    lista.pop(0)


print(sum(lista2))
