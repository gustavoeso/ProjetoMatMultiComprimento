import math
sen = math.sin
cos = math.cos
pi = math.pi
sqrt = math.sqrt
v_inicial = 0
v_final = 6*pi
referencia = []

n = 1000000

def funcao(t):
    resposta = (7*sqrt(25-24*cos((4/3)*t)))/3
    return resposta


h = (v_final - v_inicial) / n

i = v_inicial+h
while i <= v_final:
    referencia.append(funcao(i))
    i += h

somatoria = sum(referencia)

resposta = (h/2) * (funcao(v_inicial) + 2*(somatoria) + funcao(v_final))
print(resposta)
