"""
Cálculo del seno de un ángulo (en grados), por aproximaciones sucesivas.
Usamos serie de Taylor para aproximar la función seno.
"""
import math
pi = math.pi

def conversion (x):
    grad= x*180/pi
    return grad
limite = 1e-18

def seno (x):

   
    k = 1                      
    num = x                    
    den = 1                    
    s = 1                      
    term = s * num / den        
    suma = term                
    x2 = x * x                  
   
    while abs(term) > limite:
        k = k + 2
        num = num * x2
        den = den * (k-1) * k
        s = s * -1
        term = s * num / den
        suma = suma + term
    return suma
a = -2*pi                      ## ángulo inicial
incr = pi / 8                  ## incremento entre ángulos probados
pi_por_2 = 2 * pi + 1e-10      ## calcular sólo una vez el ángulo final (límite para repeticiones)

while a < pi_por_2 :
    
    x = conversion(a)
    print ("grádos", conversion (x), "|| seno", seno(x), "|| sin", math.sin(x), "DIFERENCIA", abs(seno(x) - math.sin(x)))
    a = a + incr

## Fin pruebas
