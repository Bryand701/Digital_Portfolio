##Calcular Cos

import math
pi = math.pi

limite = 1e-11

def cos (x):
    k = 0
    num = x
    den = 1
    s = 1
    term = s * num / den
    suma = 1
    x2 = x * x

    while abs (term) > limite:
        k = k + 2
        num = num * x2
        den = den * (k-1) * k
        s = s * -1
        term = s * num / den
        suma = suma + term
    return suma

#pruebas

a = -2*pi
incr = pi / 8
pi_por_2 = 2 * pi + 1e-10

while a < pi_por_2 :
    print ("ángulo", a, "|| cos", cos(a+(pi/2)), "|| cos", math.cos(a), "Diferencia" , abs(cos(a)) - abs (math.cos(a)))
    a = a + incr
        
