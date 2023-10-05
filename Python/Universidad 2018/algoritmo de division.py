## Algoritmo de division
def dividir (n,d):
## Inicializaci[on
## p : lo pendiente por procesar
## q : cociente, que al final será el sesultado deseado
    p = n
    q = 0
## repetición condicionada
    while p >= d :
        p =  p - d
        q = q+1
    
    return q
