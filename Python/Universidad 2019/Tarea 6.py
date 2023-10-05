"""
Bryand Brenes Zúñiga
2018093347
"""

"""
Ejercicio 1: suma_digitos
la función resive un número natural, se verifica que si lo sea,
en caso de que no lo sea se retorna un mensaje de error
Si lo es, se retorna la suma de todos sus digitos
"""


def suma_digitos (n):
    if isinstance (n,int) == False:
        return "ERROR: NÚMERO DEBE SER NATURAL"

    else:
        return suma_digitos_aux (n,0)

def suma_digitos_aux (n,c):
    if n == 0:
        return c
    else:
        return suma_digitos_aux (n//10,n%10 +c)


"""
Ejercicio 2: multiplica_con_sumas
La función resive dos números, el primero puede ser natural o flotante
el segundo soo puede ser natural
En caso de que las restricciones no se cumpla, se retorna un mensaje de error
En caso contrario, se retorna la multiplicacion de los números

"""

def multiplica_con_sumas (a,b):
    if isinstance (b,int) == False:
        return "ERROR: SEGUNDO ARGUMENTO DEBE SER ENTERO"
    elif isinstance (a,int) == False and isinstance(a,float) == False:
        return "ERROR: PRIMER ARGUMENTO DEBE SER NÚMERO"
    else:
        d = abs(b)
        if a < 0 and b < 0:
            a = abs(a)
            b = abs(b)
        return multiplica_con_sumas_aux (a,b,0,d)

def multiplica_con_sumas_aux (a,b,c,d):

    if d == 0:
        return c
    else:
        if a < 0 or b < 0:
            return multiplica_con_sumas_aux (a,b,c - abs(a),d-1)

        else:
            return multiplica_con_sumas_aux (a,b,c + a,d-1)

"""
Ejercicio 3: transpuesta
La función resive una matriz, y retorn la transpuesta de dicha
matriz, utilizando dos funciones auxiliares como si fueran dos for
"""

def transpuesta(matriz):
    return transpuesta_aux(matriz, len(matriz), len(matriz[0]), 0, 0)
def transpuesta_aux(matriz, total_f, total_c, cont_f, cont_c):
    if cont_c == total_c:
        return []
    else:

        return [transpuesta_aux2(matriz, total_f, total_c, cont_f, cont_c)] + transpuesta_aux(matriz, total_f, total_c, 0, cont_c+1)


def transpuesta_aux2(matriz, total_f, total_c, cont_f, cont_c):
        if cont_f == total_f:
            return []
        else:
            return [matriz[cont_f][cont_c]] + transpuesta_aux2(matriz, total_f, total_c, cont_f+1, cont_c)


"""
Ejercicio 5: extrae_diagonal
La función resive dos datos
El primero es una matriz cuadrada, en caso de que lo lo sea,
retorna un mensaje de error
El segundo dato es un número que tiene que ser estar entre 0 y el
len de la matriz -1, en caso de que no lo esté se retorna un mensaje
de error
En caso de que todo esté bien se retorna una lista con los datos de
la diagonal solicitada
"""

def verificar_matriz(lista):
    tamaño = len(lista)
    for x in lista:
        if len(x)!=tamaño:
            return False
    return True

def extrae_diagonal (lista, diagonal):
    v = verificar_matriz(lista)
    if v == False:
        return "Error: no es cuadrada"
    if abs(diagonal) > len(lista):
        return "ERROR: NO EXISTE LA DIAGONAL"

    if diagonal >= 0:
        return extrae_diagonal_aux1(lista,len(lista)-1,0,diagonal)
    else:
        return extrae_diagonal_aux2(lista,len(lista)-1,abs(diagonal),0)
    
def extrae_diagonal_aux1 (lista,tamaño,c,diagonal):
    if diagonal > tamaño:
        return []
    else:
        j = [lista[c][diagonal]]
        return j + extrae_diagonal_aux1 (lista,tamaño,c+1,diagonal+1)

def extrae_diagonal_aux2 (lista,tamaño,diagonal,c):
    print (diagonal, tamaño)
    if diagonal > tamaño :
        return []
    else:
        j = [lista[diagonal][c]]
        print (diagonal,c)
        return j + extrae_diagonal_aux2 (lista,tamaño,diagonal+1,c+1)    


"""
Ejercicio 11:serie
Lafunción resive una lista con números,
se retorna el número formado por la suma de los números de la lista al reves
"""

def serie (lista):

    return serie_aux(lista,lista[0],0)

def serie_aux(lista,analizar,c):
    
    if analizar != 0:
        m = (len(str(analizar)))-1
        return (analizar//10**m)*10**c + serie_aux(lista,analizar%10**m,c+1)
    else:
        lista = lista[1:]
        if lista == []:
            return 0
        else:
            analizar = lista [0]
            return 0 + serie_aux (lista,analizar,c)
    































