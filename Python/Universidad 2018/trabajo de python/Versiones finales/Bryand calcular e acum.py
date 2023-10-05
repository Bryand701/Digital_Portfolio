 ## Calcular e

import math
e = math.e

limite = 1e-11


def cal_e ():

    
    e = 1
    c = 0
    acum = 1
       
    
    while limite < math.e-e:

        c = c + 1
        acum = acum * c
        e = e + (1/acum)
    
        print ("El valor de e calculado por el programa es " + str(e) + " Y el valor calculado por python es ", math.e ," La diferencia es: " + str(math.e-e) )
    print("la cantidad de veces que se tuvo que repetir el proceso para aproximar e fue: " + str(c))
    
## https://es.wikipedia.org/wiki/Número_e
