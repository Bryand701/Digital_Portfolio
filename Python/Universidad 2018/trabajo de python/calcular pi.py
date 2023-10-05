"""
Aproximación de pi por el algoritmo de Borwein.
https://www.gaussianos.com/algoritmos-para-el-calculo-de-pi/  aporximar pi
"""
import math
pi = math.pi

limite = 1e-11

def raiz_4 (x):
    return math.sqrt(math.sqrt (x))

def pi ():


    a = 6 - 4*math.sqrt(2)
    y = math.sqrt(2) - 1
    pi_apr = 4                  
    k = 0

   
    while abs(pi - (1/a)) > limite:
        
        pi = 1 / a
        
        y = (1 - raiz4(1 - y ** 4)) / (1 + raiz4(1 - y ** 4))
        
        a = (a * (1 + y) ** 4) - 2 ** (2 * k + 3)* y * (1 + y + y*y)
        
        k = k + 1
        print ("aproximación de pi", 1 / a, "|| pi", math.pi, "DIFERENCIA", abs((1 / a) - math.pi))

    
    return 1 / a




