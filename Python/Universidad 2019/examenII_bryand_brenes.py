"""
Segundo examen
Bryand Brenes Zúñiga
2018093347
"""

"""
Problema 1: validar_contraseña
La función recibe un string con una contraseña la cual hay que verificar que esté correcta
Hay que verificar que tenga por lo menos una letra mayuscula, una minuscula, un número y
algún otro caracter
Un mismo caracter no puede estar más de dos veces en la contraseña
Y la contraseña debe tener al menos 8 caracteres
Si no cumple con alguna de las condiciones se retorna un False
De lo contrario se retorna un True
"""

def validar_contraseña (contraseña):
    condicion1 = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    condicion2 = ("abcdefghijklmnñopqrstuvwxyz")
    condicion3 = ("123456789") #Me faltó incluir el 0

    if len(contraseña) < 8:
        return False

    c_condicion1 = 0
    c_condicion2 = 0
    c_condicion3 = 0
    c_condicion4 = 0

    for x in contraseña:
        
        if contraseña.count(x)>2:
            return False

        #Para que funcione hay que borrar los == True de las siguientes condiciones

        if x in condicion1 == True:
            c_condicion1 = 1
        elif x in condicion2 == True:
            c_condicion2 = 1
        elif x in condicion3 == True:
            c_condicion3 = 1
        else:
            c_condicion4 = 1
    if c_condicion1 != 1:
        return False
    elif c_condicion2 != 1:
        return False
    elif c_condicion3 != 1:
        return False
    elif c_condicion4 != 1:
        return False

    return True
"""
Problema 3
La función recibe dos valores numéricos
Hay que contar todos lo primos gemelos que estén desde el primer
valor dado hasta el segundo valor, y agregar estos valores a una lista
y retornarla
"""

def primo (x):

    c = 2

    while c < x-1:
        if x % c == 0:
            return False
        # Falta poner c += 1

    return True

def primos_gemelos (a,b):

    lista = []

    while a < b:

        tupla = ()

        if primo (a) == True and primo (a + 2) == True:

            if a+2 > b:
                pass
            else:
                tupla = (a,a+2)
                lista.append(tupla)

        a += 1

    return lista

"""
Problema 2
la función recibe un string
Hay que hacer una lista con sublistas de
las primeras letras de cada palabra en el string,
a su vez, debe haber lista en cada sublista con todas
las palabras que empiecen con esa letra
Hay que retorna la lista final con todos los datos
"""

def indice_alfabetico (oracion):

    lista = []
    lista2 = []

    oracion2 = oracion.split()

    for x in (oracion2):

        v = x[0]
        if lista == []:
            lista.append(v)
        elif v not in lista:
            lista.append(v)
            

    for x in (lista):
        j = [x,[]]
        lista2.append(j)

    for x in (oracion2):

        v = x[0]

        for y in (lista2):

            b = y[0]

            if v == b:

                if x not in y[1]:
                    y[1].append(x)
    return lista2
            

