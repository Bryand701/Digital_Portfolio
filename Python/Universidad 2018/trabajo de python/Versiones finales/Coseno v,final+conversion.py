## Formula sacada de https://es.wikipedia.org/wiki/Coseno
## Espesificamente en Cálculo por serie de potencias, Formula en sumatoria
## importar pi
import math
pi = math.pi
## valor aceptable del error, para converger alrededor del valor exacto
limite = 1e-11


def conversion_a_rad (x):
    rad = x*pi/180
    return rad

def fact(n):
    
    producto = 1
   
    for k in range (n, 0, -1):  
        producto = producto * k
    return producto

def coseno (x):
    
    n = 0
    if n == 0:
        x = conversion_a_rad (x)
    s = ((-1)**n)
    num = (x**(2*n))
    den = fact(2*n)
    term = s * num / den
    suma = 0
    
    while abs(term) > limite:
        s = ((-1)**n)
        num = (x**(2*n))
        den = fact(2*n)
        term = s * num / den
        suma = suma + term
        n = n + 1
    print ("Veces que se repitió el ciclo", n)
    return suma  
##pruebas
a = -2*180
incr = 180 / 6
pi_por_2 = 2 * 180 + 1e-10

while a < pi_por_2 :
    print ("grados", a, "|| cos", coseno(a), "|| cos", math.cos(conversion_a_rad (a)), "Diferencia" , abs(coseno(a)) - abs (math.cos(conversion_a_rad (a))))
    a = a + incr
