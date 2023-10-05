## Algoritmo de residuo
def residuo (n,d):
## Inicializaci[on
## p : lo pendiente por procesar, y el residuo
## q : cociente, que va aumentando a medidad que avanza nuestro algoritmo
    p = n
    q = 0
## repetición condicionada
    while p >= d :
        p =  p - d
        q = q+1
    
    return p
