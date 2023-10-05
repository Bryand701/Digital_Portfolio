"""
Tarea 4
Bryand Brenes Zúñiga
2018093347
"""

"""
Ejercicio 1
La duncion resive un número entero mayor o igual a 1
Retorna una lista con los divisores de ese número
"""
def divisores (n):
    c = 1
    lista = []
    while c <= n:
        if n%c == 0:
            lista.append(c)
        c += 1
    return lista

"""
Ejercicio 2
La función resive una lista con números
Retorna una lista con dos listas adentro de esta
La primero con los número positivos de la lista original y la otra con los negativos
"""

def positivos_negativos (lista):
    if isinstance (lista, list) == False:
        return "Error, el dato resivido debe ser una lista"
    if lista ==  []:
        return "Error, la lista no puede estar vacia"

    lista_positos= []
    lista_negativos = []
    lista_final = []
    for x in lista:
        if x  >= 0:
            lista_positos.append (x)
        else:
            lista_negativos.append (x)
    lista_final.append(lista_positos)
    lista_final.append(lista_negativos)
    return lista_final

"""
Ejercicio 3
Las tres funciones tienen que resiven un número y una lista
Si el número esta en la lista se agrega la posición en la que está a otra lista
Se retorna la lista con la posición donde se encuentre el número
"""

def indices_for (n,lista):
    lista_final = []
    c = 0
    for x in lista:
        if n == x:
            c = lista.index(n,c)
            lista_final.append (c)
            c += 1
    return lista_final

def indices_trozos (n,lista):
    c = 0
    lista_final = []
    while lista != []:
        if lista[0] == n:
            lista_final.append (c)
        c +=1
        lista = lista [1:]
    return lista_final

def indices_indice (n,lista):
    c = 0
    c_2 = 1
    lista_final = []
    n = [n]
    while c < len(lista):

        j = lista[c:c_2]
        if j == n:
            lista_final.append(c)

        c+=1
        c_2 += 1
    return lista_final
        

    
"""
Ejercicio 4
La función resive un número que es la cantidad de número de la secuencia de fibonacci
que quiere que tenga la lista final que se retorna
"""

def fibonacci (n):
    lista = []
    c = 0
    c_1 = 0
    c_2 = 0
    for x in range (n):
        if len(lista) < 2:
            lista.append (c)
            c += 1
        else:
            c_1 = lista[-1]
            c_2 = lista[-2]
            lista.append(c_1 + c_2)


    return lista
             
"""
Ejercicio 5
La función resive un string
Se eliminan los espacios en blacon y se cuentan
Se retorna el string sin los espacios en blanco y la cantidad de espacios en blanco

"""

def elimina_espacios (string):
    s = ""
    c = 0
    for x in string:
        if x != " ":
            s = s + x
        else:
            c += 1

    return s, c

"""
Ejercicio 6
Esta función resive dos listas
una con las palabras que hay que contar cuantas veces están repetidas
y otra con oraciones en las que debe contar estas palabras
Imprime la palabra y cuantas veces está repetida
"""
def cuenta_palabras (p_repetidas, oracion):

    for x in p_repetidas:
        c = 0
    
        for y in oracion:            
            c_2 = y.count (x)
            c = c + c_2

        print (x, ":", c)

"""
Ejercicio 7
La función resive una lista con números en cada elemento
Esta agrupa los números iguales en orden de aparición
Retorna la lista con los números de cada elemento ordenados
"""

def agrupar_for (lista):

    lista_final = []

    for x in lista:
        r = ""
        est = str (x)

        for y in est:
            c = est.count(y)
            if y not in r:
                while c != 0:
                    
                   r = r + y
                   c -= 1
                   
        lista_final.append(int(r))
    return lista_final


"""
Ejercicio 8
La función resive dos datos
1) un número entre 1 y 7
este dato hay que validarlo
2) una lista con número de cédulas
Retorna las cédulas que empiencen con el número dado
"""

def provincia (n,lista):

    if n < 1 or n > 7:
        return "ERROR: PROVINCIA DEBE ESTAR ENTRE 1 Y 7"

    j = str(n)
    lista_final = []
    for x in lista:

        c = str(x)

        if c[0] == j:

            c = int(c)
            lista_final.append (c)

    return lista_final


"""
Ejercicio 9
La función resive dos elementos
el primero es un número de carne
el segundo es una lista con tuplas de datos de estudiantes
la función retorna la tupla con la información del estudiante si
el número de carne está en la tupla con su información
Si el no encuentra el número del carne entre la lista con los datos
retorna un mensaje diciendo que el estudiante no existe
"""

def consulta_estudiante (consulta, lista):

    for x in lista:

        tupla = x
        if tupla [0] == consulta:
            return x
    return "ERROR: NO SE PUEDE CONSULTAR PORQUE NO EXISTE"


"""
Ejercicio 10
Esta función resive dos datos
Una tupla con datos de un estudiante
Una lista con tuplas de datos de estudiates
La funcion agrega a la lista la tupla del estudiante si es que este no
se encuentra en la lista original
Retorna la lista con las tuplas de los datos de los estudiantes mas la nueva tupla
Retorna un mensaje de error si el carne de estudiante ya existia en la lista
"""

def agrega_estudiante (nuevo_estudiante, lista):

    carne = nuevo_estudiante[0]
    for x in lista:

        tupla = x
        if tupla [0] == carne:
            return "ERROR: NO SE PUEDE AGREGAR PORQUE YA EXISTE"
    lista.append(nuevo_estudiante)
    return lista

"""
Ejercicio 11
La función resive dos datos
Un carne
Una lista con tuplas de datos de estudiantes
La función retorna la lista con los estudiantes excepto del estudiante
al que pertenesca el carne
Si el carne no pertenece a ningun estudiante retorna un mensaje de error
"""

def elimina_estudiante (carne, lista):
    nueva_lista = []
    existe = 0
    for x in lista:

        tupla = x
        if tupla [0] != carne:
            nueva_lista.append(x)
        else:
            existe = 1

    if existe == 0:
        return "ERROR: NO SE PUEDE MODIFICAR PORQUE NO EXISTE"
    return nueva_lista    

"""
Ejercicio 12
La función resive tres datos
El primero es un número de carné
El segundo un telefono
El tercero una lista con tuplas con información de estudiantes
Retorna la lista cambiando el número de telefono nuevo con el viejo
con el carné que corresponda
Si no escuentra un estudiante con ese carné retorna un mensaje de error
"""

def modifica_estudiante (carne,tel, lista):

    nueva_lista = []
    modifica = ()
    existe = 0
    t_tel = (tel,)
    for x in lista:
        tupla = x
        if tupla [0] != carne:
            nueva_lista.append(x)
        else:
            existe = 1
            modifica = modifica + x[:3] + t_tel
            nueva_lista.append(modifica)


    if existe == 0:
        return "ERROR: NO SE PUEDE MODIFICAR PORQUE NO EXISTE"
    return nueva_lista  

"""
Ejercicio 13
La funcón resive un string
Si el string que resive se lee de igual manera leyendolo de izquierda
a derecha y viceversa retorna un True
De lo contrario un False
"""

def palindromo (palabra):

    palabra_2 = palabra
    c = 0
    c_2 = -1

    while c < len (palabra):

        if palabra [c] != palabra_2 [c_2]:
            return False

        c += 1
        c_2 -= 1
        
    return True


"""
Ejercicio 14
La función resive un string
Retorna la cantidad de digitos que aparecen en el string
"""

def digitos (string):
    c = 0
    
    for x in string:
        try:
            y = int(x)
            c += 1

        except:
            pass
    return c

"""
Ejercicio 17
La función resive una lista con numeros
Retorna un lista con estos numeros convertidos a decimal por
el metodo de division 
"""

def decimal_a_binario (lista):
    j = 0
    c = 0
    lista_final = []
    for x in lista:
        r = ""
        n = x
        while n > 0:
            j = n % 2
            n = n // 2

            r =str(j) + r

        lista_final.append (int(r))
    return lista_final


"""
Ejercicio 18
La función resive dos strings
El primer string representa un conjunto universo
El segundo string representa un subconjunto de universo
Hay que verificar que ambos datos sean un string
Y que todos los elementos del subconjunto esten en universo
Retorna el complemento del subconjunto
"""

def complemento (universo, conjunto):

    if isinstance (universo,str) == False:
        return 1
    if isinstance (conjunto,str) == False:
        return 1

    string = ""
        
    for x in conjunto:

        if x not in universo:
            return 2 

    for x in conjunto:

        for y in universo:

            if y != x:
                string = string + y

        universo = string

        string = ""

    return universo











































