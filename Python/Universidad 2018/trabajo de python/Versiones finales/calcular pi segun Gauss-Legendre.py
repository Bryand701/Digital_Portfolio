"""
Aproximación de pi por el algoritmo de Gauss Legendre.
https://es.wikipedia.org/wiki/Algoritmo_de_Gauss-Legendre
"""
import math
pi = math.pi

limite = 1e-11

def raiz_4 (x):
    return math.sqrt(math.sqrt (x))

def pi_aprox ():

    a = 1
    b = 1 / math.sqrt(2)
    t = 1 / 4
    p = 1
    # dif=0
    # pi=0   
    c = 0
    
    while  abs(a - b) > limite   : 

        x = (a + b) / 2
        y = math.sqrt(a*b)
        t = t-p*((a-x)**2)
        a = x    
        b = y 
        p = 2*p
    
        pi = ((a+b)**2)/(4*t)
        dif= math.pi-pi

        c = c +1
        
        print("El valor de pi calculado por el la función pi_aprox () es: ", pi,"El valor de pi calculado por math.pi es: ", math.pi, "la diferencia es: ",dif)
        
        
        print ("")
    print("La cantidad de veces que se a repetido el ciclo para que el marjen de error sea aceptable es: ",c)
    
    
   
    















