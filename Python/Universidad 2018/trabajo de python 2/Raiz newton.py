## Raíz cuadrada método de Newton-Raphson
## Versión 0
def raizNR0 (num, error):
    
  ## aproximar un número intermedio
    def aproximar_mejor (apr):
        return (apr + (num / apr)) / 2.0

  ## determinar si raíz es una buena aproximación
    def es_aceptable (aproximación):
        return abs (num - (aproximación * aproximación)) < error

  ## iniciar
    aprox = num / 2.0 
  #print ("aprox", aprox)
    lista=[]
    x = 0
  ## buscar raíz por tangente (Newton-Raphson)
    while not (es_aceptable (aprox)):
        x = x +1
        lista.append(aprox)
        aprox = aproximar_mejor (aprox)
    #print ("aprox", aprox)
  ## la raíz
    if x >= 1:
        tupla = (lista,lista[(x-1)],x)
    else:
        tupla = ([aprox], aprox,1)
    return tupla
def imprimir_tupla (tupla):
        print ("Secuencia de aproximaciones generadas por el algoritmo es:")
        print (tupla[0])
        print ("--------------")
        print ("El valor calculado por la raiz cuadrada es:")
        print (tupla[1])
        print ("--------------")
        print ("La cantiidad de interaciones que hizo oel método fueron")
        print (tupla[2])
##Para imprimir la tumpla tiene que seguir el siguiente formato
## imprimir_tupla (raizNR0 (num, error))

def pruebas_mul_cuadrado (e,a):
    import random
    ## e es el error aceptable deseado
    ## a es la cantidad de números a los cuales quiere que se le aplique la prueba
    """
    Pruebas
    """
    datos = []
    for i in range(a):
        datos.append(random.randint(0, 20))
    error_aceptable = e

    for x in datos:
        print ("PROBAMOS")
        print ("Entradas: ", "x = ", x, "error aceptable", error_aceptable)
        a = (raizNR0(x,error_aceptable))
        res = a[1]
        print ("<----- RESULTADO ----->")
        print ("raíz cuadrada", res, ", al cuadrado", res*res)
        print ("------------------------------------------------------------------------------------")
        print ()
def pruebas_comp_python (d,c):
    import math
    
    import random
    ## d es el error aceptable deseado
    ## c es la cantidad de números a los cuales quiere que se le aplique la prueba
    """
    Pruebas
    """
    datos = []
    for i in range(c):
        datos.append(random.randint(0, 20))
    error_aceptable = d

    for x in datos:
        print ("PROBAMOS")
        print ("Entradas: ", "x = ", x, "error aceptable", error_aceptable)
        a = (raizNR0(x,error_aceptable))
        res = a[1]
        print ("<----- RESULTADO ----->")
        print ("raíz cuadrada", res, ", raiz calculada por python", math.sqrt(x))
        print ("resultado de la resta: ", (res-math.sqrt(x)))
        print ("------------------------------------------------------------------------------------")
        print ()
def pruebas_comp_python_sin_random (k,j):
    import math
    
    ## k es el error aceptable deseado
    ## j es el número al que quiere aplicarle la prueba
    """
    Pruebas
    """
    datos = []
    datos.append(j)
    error_aceptable = k

    for x in datos:
        print ("PROBAMOS")
        print ("Entradas: ", "x = ", x, "error aceptable", error_aceptable)
        a = (raizNR0(x,error_aceptable))
        res = a[1]
        print ("<----- RESULTADO ----->")
        print ("raíz cuadrada", res, ", raiz calculada por python", math.sqrt(x))
        print ("resultado de la resta: ", (res-math.sqrt(x)))
        print ("------------------------------------------------------------------------------------")
        print ()
    
