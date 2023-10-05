 ## Calcular e

import math
e = math.e

limite = 1e-11

def fact(n):
    
    producto = 1
   
    for k in range (n, 0, -1):
        
        producto = producto * k
    return producto



def cal_e ():

    
    e = 0
    c = 0
    

    
    
    while limite < math.e-e:
        
        e = e + (1/fact (c))
        c = c + 1

    
        print ("El valor de e calculado por el programa es " + str(e) + " Y el valor calculado por python es ", math.e ," La diferencia es: " + str(math.e-e) )
    print("la cantidad de veces que se tuvo que repetir el proceso para aproximar e fue: " + str(c))
    
## https://es.wikipedia.org/wiki/Número_e
