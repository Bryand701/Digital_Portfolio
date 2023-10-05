"""
Examen III
Bryand Brenes Zúñiga
2018093347
"""

"""
Ejercicio 1: extrae diagonal
La función resive dos variables
La primera el una matriz, a la cual hay que verificar que sea cuadrada
Segundo, una diagonal, la cual hay que retornar, también hay que verificar que la diagonal
si exista
En caso de que no se cumpla ninguna de las restricciones se retorna un mensaje de error
En caso contrario, se retorna la lista solicitada
"""
def extrae_diagonal (matriz,diagonal):
    if verificar_matriz (matriz,0) == False:
        return "Error: No es cuadrada"
    if abs(diagonal) > len(matriz)-1:
        return "Error: No existe la diagonal"

    if diagonal >= 0:
        return extrae_diagonal_aux1(matriz,len(matriz)-1,0,diagonal)
    else:
        return extrae_diagonal_aux2(matriz,len(matriz)-1,abs(diagonal),0)

def extrae_diagonal_aux1 (matriz,tamaño,c,diagonal):
    if diagonal > tamaño:
        return []
    else:
        j = [matriz[c][diagonal]]
        return j + extrae_diagonal_aux1 (matriz,tamaño,c+1,diagonal+1)

def extrae_diagonal_aux2 (matriz,tamaño,diagonal,c):
    if diagonal > tamaño:
        return []
    else:
        j = [matriz[diagonal][c]]
        return j + extrae_diagonal_aux2 (matriz,tamaño,diagonal+1,c+1)

def verificar_matriz(matriz,c):
    if c == len(matriz):
        return True
    else:
        if len(matriz) == len(matriz[c]):
            return verificar_matriz(matriz,c+1)
        else:
            return False

"""
Ejercicio 2: compactar
la función resive un lista
a la cual hay que contar los números consecutivos
y agregarlos a una tupla
al final retornar la lista con las tuplas de los
números iguales consecutivos
"""

def compactar (lista):
    tamaño = len(lista)
    return compactar_aux(lista,tamaño)

def compactar_aux(lista,tamaño):

    if lista == []:
        return []
    else:
        n = lista[0]
        c = contar(lista,n,0,0)
        lista = remover(lista,n,0)
        j = [(n,c)]
        return j + compactar_aux(lista,tamaño)
def remover(lista,n,c):
    if n not in lista:
        if c == 0:
            return lista
        else:
            return []
    elif n == lista[0]:
        lista.remove(n)
        return [] + remover (lista,n,c)
    else:
        try:
            j = [lista[c]]
            return j + remover(lista,n,c+1)
        except:
            return []

def contar(lista,n,c,j):
    if c == len (lista):
        return 0
    else:
        if j == 0:
            if lista[c] == n:
                return 1 + contar(lista,n,c+1,j)
            else:
                return 0 + contar(lista,n,c+1,j+1)
        else:
            return 0 + contar(lista,n,c+1,j)




"""
Ejercicio 4: crea lista
La función resive una lista
La función crea una lista con sublista
cuando los de una forma creciente o drececiente
basado en la lista original
"""

def crea_listas (lista):
    lista_f = [[]]
    c = 0
    n = 0
    while c < len(lista) :     

        if c == 0:
            anterior = lista [0]
            lista_f[n].append(anterior)
            c += 1

        elif c == len(lista)-1:
            anterior = lista[c-1]
            actual = lista[c]
            ante_anterior = lista[c-2]
            if ante_anterior <= anterior <= actual:
                lista_f[n].append(acutal)
                
            elif ante_anterior >= anterior >= actual:
                lista_f[n].append(actual)
            elif len(lista_f[n]) == 1:
                lista_f[n].append(actual)
            else:
                n += 1
                lista_f.append([])
                lista_f[n].append(actual)
            c += 1
        elif c == 1:
            actual = lista[1]
            lista_f[n].append(actual)
            c += 1
        elif len(lista_f[n]) == 1:
            actual = lista[c]
            lista_f[n].append(actual)
            c += 1
            
        else:
            ante_anterior = lista[c-2]
            anterior = lista[c-1]
            actual = lista[c]

            if ante_anterior <= anterior <= actual:
                lista_f[n].append(actual)
            elif ante_anterior >= anterior >= actual:
                lista_f[n].append(actual)
            else:
                n += 1
                lista_f.append([])                                
                lista_f[n].append(actual)
            c += 1
        
        
    return lista_f 
                
                
"""
Ejercicio 3: materias
La función resive un diccionario con las notas de los estudiantes
Hay que generar un nuevo diccionario por materias con una lista
de tuplas del nombre, carne, nota de cada estudiante
se retorna el nuevo diccionario
"""

def crear_dicc(lista,c,tamaño,d):
    if tamaño == c:
        return d
    else:
        j = lista[c][1]
        if j not in d:
            d[j] = []
            return crear_dicc(lista,c+1,tamaño,d)
        else:
            return crear_dicc(lista,c+1,tamaño,d)

def sacar_materias (lista,tamaño,c,n_list):
    if c == tamaño:
        return n_list
    else:
        j = sacar_materias_aux(lista[c],1,[])
        #para que funcione sustiuir todo la signación al valor de j y el n_lista = .....por
        #n_list.append(lista[c][1])
        return sacar_materias (lista,c+1,n_list)
def sacar_materias_aux(lista,c,n_lista):
    if c == len(lista):
        return n_lista
    else:
        n_lista.append(lista[c][1])
        return sacar_materias_aux(lista,c,n_lista+1)
        
def materias(diccionario):

    carne = list(diccionario.keys())
    lista_n = list(diccionario.values())
    d = {}
    materias_lista = sacar_materias(lista_n,len(lista_n),0,[])
    nuevo_d = crear_dicc(materias_lista,0,len(materias_lista),d)
    lista_f = lista_completa(carne,lista_n,0,[])
    return materias_aux(d,lista_f,0)

def materias_aux(diccionario,lista,c):
    if c ==len(lista):
        return diccionario
    else:
        diccionario = actualizar_dicc(diccionario,lista[c],2)
        return materias_aux(diccionario,lista,c+1)

def actualizar_dicc(diccionario,lista,c):

    if c > len(lista[1]):
        return diccionario
    else:
        materia = lista[1][c-1][1]

        estudiante = [(lista[0],lista[1][0],lista[1][1][0])]

        diccionario[materia] = diccionario[materia] + estudiante

        return actualizar_dicc(diccionario,lista,c+1)

def lista_completa (lista1,lista2,c,lista):

    if c == len (lista1):

        return lista
    else:
        j = [lista1[c]] + [lista2[c]]
        lista.append(j)
        return lista_completa (lista1,lista2,c+1,lista) 
        





















































