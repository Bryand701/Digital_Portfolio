import math
pi = math.pi


"""
Cálculo del seno de un ángulo (en radianes), por aproximaciones sucesivas.
Usamos serie de Taylor para aproximar la función seno.
"""
## importar pi
import math
pi = math.pi

## valor aceptable del error, para converger alrededor del valor exacto
limite = 1e-11

def conversion_a_rad (x):
    rad = x*pi/180
    return rad
"""
Ver Wikipedia: https://es.wikipedia.org/wiki/Seno_(trigonometr%C3%ADa)#Seno_en_an%C3%A1lisis_matem%C3%A1tico
  \sen x =
  \sum^{\infin}_{n=0} \; (-1)^n \; \frac{x^{2n+1}}{(2n+1)!}
"""

## Nuestra implementacion de la función seno dará resultados aceptables si el ángulo está entre -2*pi y 2*pi radianes

def seno (x):

    ## inicialización de variables de trabajo
    ## n = 0, esta variable es innecesaria, ver fórmula en https://es.wikipedia.org/wiki/Seno_(trigonometr%C3%ADa)#Como_serie_de_Taylor
    j = 1
    k = 1  ## k = (2*n + 1) para trabajar con potencias y factoriales impares
    if j == 1:
        x = conversion_a_rad (x)
    j = 2   
    num = x                    ## el numerador de cada término. Siempre será x^k
    den = 1                    ## el denominador de cada término.  Siempre será k!
    s = 1                      ## el signo de cada término.  Alternará entre +1 y -1.
    term = s * num / den        ## el término, que es un sumando en la serie de Taylor para aproximar el seno.
    suma = term                ## la sumatoria inicia con el primer término.
    x2 = x * x                  ## pre-calculamos el cuadrado de x, para evitar hacer multiplicaciones en el ciclo while.
    veces = 0

    ## repetir hasta lograr una aproximación suficientemente precisa, cercana al valor exacto
    while abs(term) > limite:
        ## actualizar el impar (para potencia de x en el numerador y factorial en el denominador)
        ## n = n + 1
        k = k + 2
        ## calcular siguiente término de la serie
        num = num * x2
        den = den * (k-1) * k
        s = s * -1
        term = s * num / den
        ## sumar el término a la serie
        suma = suma + term
        veces = veces + 1
        #print ("veces", veces, "aproximación",suma)

    ## devolver resultado
    print ("veces", veces)
    return suma


## Pruebas

a = -2*180                     ## ángulo inicial
incr = 180 / 6                  ## incremento entre ángulos probados
pi_por_2 = 2 * 180 + 1e-10     ## calcular sólo una vez el ángulo final (límite para repeticiones)

while a < pi_por_2 :
    print ("ángulo", a, "|| seno", seno(a), "|| sin", math.sin(conversion_a_rad (a)), "DIFERENCIA", abs(seno(a)) - abs(math.sin(conversion_a_rad (a))))
    a = a + incr

## Fin pruebas
