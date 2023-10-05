"""
Bryand Brenes Zúñiga
2018093347
Tarea 5
"""

import random

"""
Ejecicio 1:suma_digitos
La función secibe un número entero
y retorna la suma de los digitos de ese número
Si no es un número entero retorna un mensaje de error
"""

def suma_digitos (n):
    if isinstance (n,int) == False:
        return "ERROR: NÚMERO DEBE SER NATURAL"
    else:
        return suma_digitos_aux (n)

def suma_digitos_aux (n):

    if n == 0:
        return 0
    else:
        return n%10 + suma_digitos (n//10)


"""
Ejercicio 2: multiplica_con_sumas
La función secibe dos valores
El primero es el número al que hay que multiplicar, tiene que ser entero o flotante
El segundo las veces que hay que multiplicarlo, tiene que entero
Si se cumplen las condiciones se retorna la multiplicación
De lo contrario, se retorna un mensaje de error
"""

def multiplica_con_sumas (a,b):
    if isinstance (b,int) == False :
        return "ERROR: SEGUNDO ARGUMENTO DEBE SER ENTERO"

    elif isinstance (a,float) == False and isinstance (a,int) == False:
        return  "ERROR: PRIMER ARGUMENTO DEBE SER NÚMERO"

    if b < 0:
        a = a * -1
        b = b * -1

    return multiplica_con_sumas_aux(a,b)


def multiplica_con_sumas_aux(a,b):

    if b == 0:
        return 0
    else:
        return a + (multiplica_con_sumas_aux(a,b-1))


"""
Ejercicio 3: palindromo
La función secibe un número entero
Si no es entero se retorna un mensaje de error
De lo contrario revisa que el número sea un palindromo
comparando el primero numero con el ultimo número y descomponiendolo
Se retorna un True si el número es un palindromo y un False si el número no lo es.
"""
def digitos (n):

    c = 0
    if n == 0: 
        c = 1 
    
    while n != 0:
        n = n //10
        c += 1

    return c

def palíndromo(n):
    if isinstance(n,int)==False:
        return "ERROR:EL DATO DEBE SER UN ENTERO"
    elif n == True:
        return "ERROR:EL DATO DEBE SER UN ENTERO"
    elif n == False:
        return "ERROR:EL DATO DEBE SER UN ENTERO"
    
    n=abs(n)
    if digitos(n)== 1:
        return True
    else:
        return palindromo_aux(n)
        
def palindromo_aux(n):
    if n%10 != n//(10**(digitos(n)-1)):
        return False
    elif digitos(n)== 1:
        return True        
    else:
        return palindromo_aux(((n%10**(digitos(n)-1))//10))
    

"""
Ejercicio 4: aleatorios
La función secibe tres valores
El primero es la cantidad de números aleatoreos que se deben adjuntar en la lista
El segundo es el número menor que puede salir del aleatorio
El tercero es el número mayor que puede salir del aleatorio
Se retorna la lista con los numero ya agregados
"""

def aleatorios (n, minimo, maximo):

    lista = []
    if n == 0:
        return lista

    else:
        aleatorios_aux(n, minimo, maximo, lista)
        return lista

def aleatorios_aux (n, minimo, maximo, lista):
    j = random.randint(minimo,maximo)
    if n == 1:
        return lista.append (j)
    else:

        lista.append (j)
        return aleatorios_aux (n-1, minimo, maximo, lista)
"""
Ejercicio 5: elimina_digito
La función secibe dos valores
El primero es un número al que hay que eliminar del segundo
número todas las veces que este aparesca
Se retorna el número final ya sin el número que hay que eliminar
"""
def elimina_digito(elimina,numero):
    numero = abs(numero)
    if numero==elimina:
        return "queda sin digitos"
    else:
        c = 0
        j = elimina_digito_aux(elimina,numero,c)
        if j == 0:
            return "queda sin digitos"
        else:
            return j
        
def elimina_digito_aux(elimina,numero,c):
    if numero == 0:
        return 0
    elif elimina == numero%10:
        return elimina_digito_aux(elimina,numero//10,c) 
    else:
        return numero%10 * 10**c + elimina_digito_aux(elimina,numero// 10,c+1)



"""
Ejercicio 6:doble_factoria
La función secibe un número natural
Se retorna el doble factorial de este número

"""
def doble_factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return doble_factoria_aux (n)

def doble_factoria_aux (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * doble_factoria_aux (n-2)

"""
Ejercicio 7: solo_digitos
La función secibe un string
Al cual hay que seleccionar todos los número que contenga
y retoanr todos esos números en uno solo
"""
def solo_digitos(x):
    try:
        return int(solo_digitos_aux(x))
    except:
        return ""

def solo_digitos_aux(x):
    
    a="1234567890"
    if x != "":
        if x[0] in a:
            return x[0] + solo_digitos_aux(x[1:])
        else:
            return solo_digitos_aux(x[1:])
    else:
        return ""

"""
Ejercicio 8: dígitos_en_comun
La función secibe dos números
La funcion busca si entre alguno de los dos
se encuentra al menos un digito repetido
retorna los digitos repetidos como uno solo

"""

def digitoEnNumero(d, n):
    if n == 0 and d == 0:
        return True
    return digitoEnNumeroAux(d, n)

def digitoEnNumeroAux(d, n):
    if n == 0:
        return False
    return n % 10 == d or digitoEnNumeroAux(d, n // 10)

def digitos_en_comun(a,b):
    resultado = 0
    hayComun = False
    if digitoEnNumero(1, a) and digitoEnNumero(1, b):
        hayComun = True
        resultado = resultado * 10 + 1
    if digitoEnNumero(2, a) and digitoEnNumero(2, b):
        hayComun = True
        resultado = resultado * 10 + 2
    if digitoEnNumero(3, a) and digitoEnNumero(3, b):
        hayComun = True
        resultado = resultado * 10 + 3
    if digitoEnNumero(4, a) and digitoEnNumero(4, b):
        hayComun = True
        resultado = resultado * 10 + 4
    if digitoEnNumero(5, a) and digitoEnNumero(5, b):
        hayComun = True
        resultado = resultado * 10 + 5
    if digitoEnNumero(6, a) and digitoEnNumero(6, b):
        hayComun = True
        resultado = resultado * 10 + 6
    if digitoEnNumero(7, a) and digitoEnNumero(7, b):
        hayComun = True
        resultado = resultado * 10 + 7
    if digitoEnNumero(8, a) and digitoEnNumero(8, b):
        hayComun = True
        resultado = resultado * 10 + 8
    if digitoEnNumero(9, a) and digitoEnNumero(9, b):
        hayComun = True
        resultado = resultado * 10 + 9
    if digitoEnNumero(0, a) and digitoEnNumero(0, b):
        hayComun = True
        resultado = resultado * 10
    if hayComun:
        return resultado
    return False
"""
Ejercicio 9: serie
La función recibe dos números
La función suma todos los número que hay entre el primer
número y el segundo incluyendolos
retorna un solo numero con los números como
uno solo

"""

def serie (inicio,final):

    if isinstance (inicio, int) == False or isinstance (final,int) == False:
        return "Las entradas deben ser números enteros"
    elif inicio >= final:
        return "El número de inicio debe ser menor al número final"
    else:
        c = 0
        final += 1 
        inicio = str(inicio)
        final = str(final)
        return int(serie_aux(inicio,final))
    
def serie_aux(inicio,final):
    if inicio == final:
        return ""
    else:
        j = inicio
        inicio = int(inicio)
        return j + serie_aux(str(inicio +1),final)
        
"""
Ejercicio 10: intersecta
La función secibe dos números
La funcion busca si entre alguno de los dos
se encuentra al menos un digito repetido
retorna los digitos repetidos como uno solo
si no hay números en común se retorna
False
"""

def digitoEnNumero(d, n):
    if n == 0 and d == 0:
        return True
    return digitoEnNumeroAux(d, n)

def digitoEnNumeroAux(d, n):
    if n == 0:
        return False
    return n % 10 == d or digitoEnNumeroAux(d, n // 10)

def intersecta(a,b):
    resultado = 0
    hayComun = False
    if digitoEnNumero(1, a) and digitoEnNumero(1, b):
        hayComun = True
        resultado = resultado * 10 + 1
    if digitoEnNumero(2, a) and digitoEnNumero(2, b):
        hayComun = True
        resultado = resultado * 10 + 2
    if digitoEnNumero(3, a) and digitoEnNumero(3, b):
        hayComun = True
        resultado = resultado * 10 + 3
    if digitoEnNumero(4, a) and digitoEnNumero(4, b):
        hayComun = True
        resultado = resultado * 10 + 4
    if digitoEnNumero(5, a) and digitoEnNumero(5, b):
        hayComun = True
        resultado = resultado * 10 + 5
    if digitoEnNumero(6, a) and digitoEnNumero(6, b):
        hayComun = True
        resultado = resultado * 10 + 6
    if digitoEnNumero(7, a) and digitoEnNumero(7, b):
        hayComun = True
        resultado = resultado * 10 + 7
    if digitoEnNumero(8, a) and digitoEnNumero(8, b):
        hayComun = True
        resultado = resultado * 10 + 8
    if digitoEnNumero(9, a) and digitoEnNumero(9, b):
        hayComun = True
        resultado = resultado * 10 + 9
    if digitoEnNumero(0, a) and digitoEnNumero(0, b):
        hayComun = True
        resultado = resultado * 10
    if hayComun:
        return resultado
    return False

"""
Ejercicio 11:pares_impares
La función resive un número entero
Hay que retornar una tupla con los la cantidad de
números pares e impares que tiene el numero incial
Si el número no es entero se retorna un mensaje de error
"""

def pares_impares (a):

    if isinstance (a,int) == False:
        return "ERROR: ENTRADA DEBE SER UN NÚMERO NATURAL"
    if a == 0:
        return (1,0)

    a = abs(a)
    c = 0
    j = pares(a,c)
    g = str(a)
    h = len(g)

    return j, (h-j)

def pares (a,c):
    b = a % 10
    if a == 0:
        return 0

    if b % 2 != 0:
        return pares(a// 10,c)

    else:
        return 1 + pares(a// 10,c+1)


    
    

    





































