"""
Cálculo del coseno de un ángulo (en radianes), por aproximaciones sucesivas.
Usamos serie de Taylor para aproximar la función coseno.
"""
## importar pi
import math
pi = math.pi

## valor aceptable del error, para converger alrededor del valor exacto
limite = 1e-10



## Nuestra implementacion de la función seno dará resultados aceptables si el ángulo está entre -2*pi y 2*pi radianes

def coseno (x):

    ## inicialización de variables de trabajo
    ## i = 0, esta variable es innecesaria
    k = 0                     ## para trabajar con potencias y factoriales impares
    num = x                    ## el numerador de cada término. Siempre será x^k
    den = 1                    ## el denominador de cada término.  Siempre será k!
    s = 1                      ## el signo de cada término.  Alternará entre +1 y -1.
    term = s * num / den        ## el término, que es un sumando en la serie de Taylor para aproximar el seno.
    suma = term                ## la sumatoria inicia con el primer término.
    x2 = x * x                  ## pre-calculamos el cuadrado de x, para evitar hacer multiplicaciones en el ciclo while.

    ## repetir hasta lograr una aproximación suficientemente precisa, cercana al valor exacto
    while abs(term) > limite:
        ## actualizar el impar (para potencia de x en el numerador y factorial en el denominador)
        k = k + 2
        ## calcular siguiente término de la serie
        num = num * x2
        den = den * (k-1) * k
        s = s * -1
        term = s * num / den
        ## sumar el término a la serie
        suma = suma + term

    ## devolver resultado
    return suma


## Pruebas

a = -2*pi                      ## ángulo inicial
incr = pi / 8                  ## incremento entre ángulos probados
pi_por_2 = 2 * pi + 1e-10      ## calcular sólo una vez el ángulo final (límite para repeticiones)

while a < pi_por_2 :
    print ("ángulo", a, "|| coseno", coseno(a), "|| cos", math.cos(a), "DIFERENCIA", abs(coseno(a) - math.cos(a)))
    a = a + incr

## Fin pruebas
