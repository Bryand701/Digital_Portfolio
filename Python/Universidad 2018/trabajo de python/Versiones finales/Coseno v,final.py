## Formula sacada de https://es.wikipedia.org/wiki/Coseno
## Espesificamente en Cálculo por serie de potencias, Formula en sumatoria
## importar pi
import math
pi = math.pi
## valor aceptable del error, para converger alrededor del valor exacto
limite = 1e-11
def fact(n):
    
    producto = 1
   
    for k in range (n, 0, -1):  
        producto = producto * k
    return producto
def coseno (x):
    n = 0
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
    
    print ("Veces que se reipitió el ciclo ",n)
    return suma
     
##pruebas
a = -2*pi
incr = pi / 6
pi_por_2 = 2 * pi + 1e-10

while a < pi_por_2 :
    print ("ángulo", a, "|| cos", coseno(a), "|| cos", math.cos(a), "Diferencia" , abs(coseno(a)) - abs (math.cos(a)))
    a = a + incr

