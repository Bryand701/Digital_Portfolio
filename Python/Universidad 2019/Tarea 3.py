"""
TAREA 3: PRÁCTICAS PARA EXAMEN 1
Bryand Brenes Zúñiga
2018093347
"""

"""
Función para contar los dígitos de un número
"""
def digitos (n):
    
    if isinstance(n, int) == False: 
        return False
    if n == 0: 
        return 1
    n = abs(n) 
    d = 0
    while n != 0:
        n = n // 10
        d = d + 1
    return d
"""
Función para descomponer fechas por año, mes y día
Las restricciones de estas funciones están en los programas utilizados
"""

def dec_fecha (fecha):
    if fecha >= 10012000:
        dd = fecha // 1000000
        mm = (fecha % 1000000) // 10000
        aaaa = fecha % 10000

        return dd,mm,aaaa
    else:
        dd = fecha // 1000000
        mm = (fecha % 100000) // 10000
        aaaa = fecha % 10000

        return dd,mm,aaaa

"""
Ejercicio 1: palindromo
Esta función lo que hace verificar si un número es palindromo (que se lea igual para ambos lados)
Resive un número entero
Retorna un valor voleano de True si el número es palindromo
Si el número no es palindromo se retorna un False
En caso de que no se cumplan las condiciones se retorna un mensaje de error
"""

def palindromo (numero):

    if isinstance (numero, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"

    dig= digitos (numero)
    c = 0
    exponente = dig - 1

    numero = abs(numero)
    
    while (dig//2) > c:

        
        
        if (numero//(10**exponente))%10 != (numero//(10**c))%10:           
            return False
        
        exponente -= 1
        c +=1
        
    return True


"""
Ejercicio 2: divisores_propios
Esta función imprime todos los divisores de un número eceptuandolo a si mismo
resive un número entero mayor o igual a 2
Imprime todos los divisores que calcule, eceptuandolo a si mismo
En caso de que no se cumplan las condiciones se retorna un mensaje de error
"""


def divisores_propios (numero):

    if isinstance (numero, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"
    if numero < 2:
        return "El número tiene que ser mayor a dos"

    c = 1

    while numero != c:

        if numero%c == 0:
            print (c, end="   ")

        c += 1
    

"""
Ejercicio 3:suma_divisores_propios
Esta función resive un número entero mayor o igual 2
Primero se saca los divesores del número y se suman
Se retorna la suma de los divisores y los divisores
"""

def suma_divisores_propios (numero):

    if isinstance (numero, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"
    if numero < 2:
        return "El número tiene que ser mayor a dos"
    
    c = 1
    c2 = 1
    suma = 0
    while numero != c:

        if numero%c == 0:
            suma += c

        c += 1

    return suma

    

"""
Ejercicio 4: elimina_digito
Esta función resve dos valores
Un dígito entero entre 0 y 9
Otro número entero mayor o igual a 0
Si las restricciones no se cumplen se retorna un mensaje de error
en caso contrario se descomponen la variable numero
si es difirente  de digito se suma a "suma" multiplicado por diez elevado a elevar2
de lo contrario se omite
al final se retorna suma
"""

def elimina_digito (digito, numero):

    if isinstance (numero, int) == False or isinstance (digito, int)  == False:
        return "ERROR: DATOs DE ENTRADA DEBEn SER ENTEROS"

    if 0 > digito or digito > 10:

        return "ERROR EN DIGITO"
    
    elevar = 0
    c = 0
    entero = 0
    suma = 0
    elevar2 = 0


    while 1+c <= digitos (numero):
            
        entero = (numero//(10**c))%(10)
        if entero != digito:
            suma += entero * (10**elevar2)
            elevar2 += 1
        elevar += 1

        c += 1

    if suma == 0:
        return False
            
    return suma        
                
        
"""
Ejercicio 5: primo
Esta función resive un número entero mayor o igual a 2
si no se cumplen las restricciones se retorna un mensaje de error
De lo contrario calcula la elevación de n**1/2 para calcular la raiz cuadrada del número
Se retorna True si el no se encuentra que divida a n y de residuo 0
De lo contrario se retorna un False
"""

def primo (n):

    if isinstance (n, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"
    if n < 2:
        return "ERRRO: EL NÚMERO DEBE SER MAYOR O IGUAL A 2"
    
    c = 0

    while c != n**1/2:
        if c+2 == n:
            return True
        if n%(c+2) == 0:
            return False
        c += 1
    

"""
Ejercicio 6: contar_pares_impares
Esta fuunción resive un número entero mayor o igual a 0
Si no se cumplen las restricciones se retorna un mensaje de error
De lo contrario se analiza uno a uno los digitos y se separan por pares o impares
Se retornan los pares e impares, si no hay alguno de los dos se retorna un mensaje de "No hay"
en el lugar donde deberia estar.
"""

def pares_impares (n):

    if isinstance (n, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"
    if n < 0:
        return "ERRRO: EL NÚMERO DEBE SER MAYOR O IGUAL A 0"
    

    pares=0
    impares=0
    c = 0
    cpares = 0
    cimpares = 0
    while digitos (n) > c:
        

        if ((n//(10**c))%10)% 2 == 0:
            pares += ((n//(10**c))%10)* (10**cpares)
            cpares += 1
            print (pares)
        else:
            impares += ((n//(10**c))%10)* (10**cimpares)
            cimpares += 1
        c += 1

    if  pares == 0:
        return "no hay", impares
    elif impares == 0:
        return pares, "no hay"
    else:
        return pares, impares
    
"""
Ejercicio 8: rombo
Esta función resive un  numero entero mayor o igual a 2
Si no se cumplen las restricciones retorna un mensaje de error
De lo contrario imprime espacios y * en funcion al numero que metió
el usuario en la función
"""

def rombo (n):

    if isinstance (n, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"
    if n < 2:
        return "ERRRO: EL NÚMERO DEBE SER MAYOR O IGUAL A 2"

    a = 0
    b = 0
    c = n - 3
    d = n - 3
    e = n -1
    f = 1
    g = 0
    while a < n:
        
        while b < n:
            print ("", end = " ")
            b += 1
        while g < f:
            print ("*", end = "")
            g += 1

        f += 2
        g = 0
        print ("")
        a += 1
        b = a
    a -=1
    f -= 4
    while a > 0:
        
        while c < e:
            print ("", end = " ")
            c += 1
        while g < f:
            print ("*", end = "")
            g += 1

        f -= 2
        g = 0
        print ("")
        d -= 1
        c = d
        a -= 1
        b = a 
        
"""
Ejercicio 9: intesección
Esta función resive dos nueros enteros
Si no cumplen la restriccion se retorna un mensaje de error
De lo contrario verifica si entre el primer numero hay alguno que
se repita en el segundo numero, si es así los suma junta en un solo numero,
luego verifica que el numero formado no tenga digitos repetidos, si es así los elimina
luego retorna el numero ya sin los numero repetidos(en caso de que hubiera alguno)
"""
        
def interseccion (n1, n2):

    if isinstance (n1, int) == False or isinstance (n2, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"

    n1 = abs(n1)
    n2 = abs(n2)
    
    digitos_n1 = digitos(n1)
    digitos_n2 = digitos(n2)
    
    c = 0
    c2 = 0
    c3 = 0
    entero = 0
    
    while c < digitos_n1:
        d = (n1//(10**c))%10

        while c2 < digitos_n2:
            if d == (n2//(10**c2))%10:
                entero += d * (10**c3)
                c3 += 1

            c2 += 1

        c2 = 0
        c += 1

    c = 0
    c2 = 0
    c3 = 0
    c4 = 0
    r = 0
    entero2 = 0
    if entero == 0:
        return False

    while c <digitos(entero):
        
        d = (entero//(10**c))%10
        c3 = c
      
        while c2 < digitos(entero)-c:
            
            if d == (entero//(10**(c3+1)))%10:
                
                r = 1

            c3 += 1
            c2 += 1

        if r == 0:
            entero2 += d * (10**c4)
            c4 += 1
            
 
        r = 0
        c2 = 0
        c +=1
    
    return entero2


"""
Ejercicio 10: sumatoria
esta función resive dos numeros enteros
Si no cumplen la restriccion se retorna un mensaje de error
De lo contrario retorna "enetero"
"""


def sumatoria (inicio, fin):

    if fin < inicio:
        return "ERROR: El segundo número debe ser mayor al primero"

    if isinstance (fin, int) == False or isinstance (inicio, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"

    entero = inicio

    while inicio < fin:
        inicio +=1
        entero += inicio
    
    return entero

"""
Ejercicio 11: doble_factorial
Esta funcion resive un numero entero mayor o igual a  0
Si no cumplen la restriccion se retorna un mensaje de error
de lo contrario calcual si el numero es par o impar
Si es par empieza a multiplica todos los número pares desde 2 hasta
el numero dado y retorna la el resultado
Si es impar hace lo mismo pero empesando desde 1
"""

def doble_factorial (n):

    if isinstance (n, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"
    if n < 0:
        return "ERRRO: EL NÚMERO DEBE SER MAYOR O IGUAL A 0"

    entero = 1
    if n%2 == 0:
        c = 2
    else:
        c = 1

    while c < n+2:
        
        entero *= c
        c +=2

    return entero
        

"""
Ejercicio 12: diferencia
Esta función resive dos nueros enteros
Si no cumplen la restriccion se retorna un mensaje de error
De lo contrario verifica si entre el primer numero hay alguno que
se repita en el segundo numero, si no se repite lo va agregando al "entero"
en la pocisión correspondiente
Al final reetorna al entero
"""
#En este programa no esta la restricción de que los número a la hora de retornalos
#no puenden estar repetidos
def diferencia (n1, n2):
    if isinstance (n1, int) == False or isinstance (n2, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"

    n1 = abs(n1)
    n2 = abs(n2)
    
    digitos_n1 = digitos(n1)
    digitos_n2 = digitos(n2)
    
    c = 0
    c2 = 0
    c3 = 0
    r = 0
    c4 = 0
    entero = 0
    
    while c < digitos_n1:
        d = (n1//(10**c))%10

        while c2 < digitos_n2:

            if d == (n2//(10**c2))%10 and c4 == 0:
                r = 1
                c4 = 1
            c2 += 1        

        if r != 1:
            
            entero += d * (10**c3)
            c3 += 1

            c2 += 1

        r = 0
        c4 = 0
        c2 = 0
        c += 1

    if entero == 0:
        return False
    return entero



"""
Ejercicio 13: encriptar
Esta función resive dos numero entero, el primero entre 0 y 9
el segundo entre 0 y 999999999
Si las restricciones no se cumplen se imprime un mensaje de error
De lo contrario se calcula el número encriptado y se retorna
"""

def encriptar (n1, n2):
    if isinstance (n1, int) == False or isinstance (n2, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"
    if 0 > n1 or n1 > 9:
        return "ERROR: el primer número debe estar entre 0 y 9"
    if 0 > n2 or n2 > 999999999:
        return "ERROR: el segundo número debe estar entre 0 y 999999999"

    d = digitos(n2)
    c = 0
    entero = 0

    while c < d:
        entero += ((n2 // 10**c % 10) + n1) % 10 * 10**c
        c +=1
    entero += d * 10**c
    return entero

"""
Ejercicio 14
Esta función resive dos numero entero, el primero entre 0 y 9
el segundo entre 0 y 999999999
Si las restricciones no se cumplen se imprime un mensaje de error
De lo contrario se calcula el número desencriptado y se retorna
"""

def desencriptar (n1, n2):
    if isinstance (n1, int) == False or isinstance (n2, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"
    if 0 > n1 or n1 > 9:
        return "ERROR: el primer número debe estar entre 0 y 9"
    if 0 > n2 or n2 > 999999999:
        return "ERROR: el segundo número debe estar entre 0 y 999999999"

    d = digitos(n2)
    c = 0
    entero = 0
    n2 = n2 - (10**(d-1) * (d - 1))
    d -= 1
    while c < d:
        r = (n2 // 10**c % 10) - n1
        if r == -1:
            entero += 9 * 10**c
        elif r == -2:
            entero += 8 * 10**c
        elif r == -2:
            entero += 8 * 10**c
        elif r == -3:
            entero += 7 * 10**c
        elif r == -4:
            entero += 6 * 10**c
        elif r == -5:
            entero += 5 * 10**c
        elif r == -6:
            entero += 4 * 10**c
        elif r == -7:
            entero += 3 * 10**c
        elif r == -8:
            entero += 2 * 10**c
        elif r == -9:
            entero += 1 * 10**c
        else:
            entero += r * 10**c
        c += 1
    return entero


"""
Ejercicio 15: diferencia_simetrica
Esta función resive dos nueros enteros
Si no cumplen la restriccion se retorna un mensaje de error
De lo contrario verifica si entre el primer numero hay alguno que
se repita en el segundo numero, si no se repite lo va agregando al "entero"
en la pocisión correspondiente
Al final reetorna al entero
"""
#En este programa no esta la restricción de que los número a la hora de retornalos
#no puenden estar repetidos
def diferencia_simetrica (n2, n1):
#Se cambia de n1 a n2 para no cambiar mucho a la funcion diferencia y reutilizar parte del codigoZ
    if isinstance (n1, int) == False or isinstance (n2, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"

    n1 = abs(n1) 
    n2 = abs(n2)
    
    digitos_n1 = digitos(n1)
    digitos_n2 = digitos(n2)
    
    c = 0
    c2 = 0
    c3 = 0
    r = 0
    c4 = 0
    c5 = 0
    entero = 0
    
    while c < digitos_n1:
        d = (n1//(10**c))%10

        while c2 < digitos_n2:

            if d == (n2//(10**c2))%10 and c4 == 0:
                r = 1
                c4 = 1
            c2 += 1        

        if r != 1:
            
            entero += d * (10**c3)
            c3 += 1

            c2 += 1

        r = 0
        c4 = 0
        c2 = 0
        c += 1   
    
    while c5 < digitos_n2:
        
        d = (n2//(10**c5))%10
        while c2 < digitos_n1:

            if d == (n1//(10**c2))%10 and c4 == 0:
                r = 1
                c4 = 1
            c2 += 1        

        if r != 1:
            
            entero += d * (10**c3)
            c3 += 1

            c2 += 1

        r = 0
        c4 = 0
        c2 = 0
        c5 += 1

    if entero == 0:
        return False
    return entero


"""
Ejercicio 16:cuenta_celular
Este ejercicio esta divido en 4 funciones
La función cuenta_celular es la función prinsipal,
no resive nada ni retorna nada, pero solicita un número entero
entre 1 y  4 para elegir que accion realizar
La función recargas resive saldo que inicialmente es 0 y recarga que
el usuario digita, retorna saldo 
La función consumo resive saldo y consumo el cual el usuario digita
retorna saldo
La función estado resive saldo, imprime la sumatoria de todas las recargas,
consumos y el saldo actual
"""

def cuenta_celular():
    saldo = 0
    global c_consumo, c_recarga
    c_consumo = 0
    c_recarga = 0
    c = 0
    print("Digite un número segun el tramite que desea realiza ")
    print("1: Recargas ")
    print("2: Consumos ")
    print("3: Estado de cuenta ")
    print("4: Fin " )
    opcion = int(input("Digite el numero del tramite que desea realizar: "))
    while opcion != 4:
        if c == 1:
            print("Digite un número segun el tramite que desea realiza ")
            print("1: Recargas ")
            print("2: Consumos ")
            print("3: Estado de cuenta ")
            print("4: Fin " )
            opcion = int(input("Digite el numero del tramite que desea realizar: "))
        if opcion == 1:
            c = 1
            recarga = int(input("Cuánto desea recargar?: "))
            saldo = recargas(saldo, recarga)
        elif opcion == 2:
            c = 1
            consumo = int(input("¿Cuánto consumió?: "))
            saldo = consumos(saldo, consumo)
        elif opcion == 3:
            c = 1
            estado(saldo)
        elif opcion == 4:
            break
        else:
            print("opcion no valida, por favor digitar un numero del uno al cuatro")
            opcion = int(input("digite el numero de la opcion que desea: "))


def recargas(saldo,recarga):
    global c_recarga
    saldo += recarga
    c_recarga += recarga
    return saldo


def consumos(saldo,consumo):
    global c_consumo
    if saldo - consumo < 0:
        print("SALDO INSUFICIENTE")
        return saldo
    else:
        saldo -= consumo
        c_consumo += consumo
        return saldo
def estado (saldo):
    global c_consumo, c_recarga
    print ("Consumo: ", c_consumo)
    print ("Recargas: ", c_recarga)
    print ("Saldo: ", saldo)


"""
Ejercicio 17: calcular_fin_proceso
Se crearon tres funciones para este ejercicio
La funcion bisiesto lo que hace es verificar si un año es o no bisiesto
La función valida_fecha es para vereficar que la fecha esté correcta
La función calcular_fin_proceso resive una fehca en formato ddmmaaaa, y un número entero entre 0 y 15
Si no cumplen con las restricciones retorna un mensaje de error
En caso contrario, calcula los días el mes y el año segun se de el caso
Retorna la fecha ya con los días sumados
"""

def calcular_fin_proceso (fecha, dias):
# La verdad no tengo idea de donde meter un while en esta función
    dd,mm,aaaa= dec_fecha(fecha)
    
    if isinstance (fecha, int) == False or isinstance (dias, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"
    if 0 > dias or dias > 15:
        return "ERROR: los días deben estar entre 0 y 15"

    if aaaa < 2000:
        return "ERROR: el año debe ser mayor o igual a 2000"
    if valida_fecha (fecha) == False:
        return "ERROR: la fecha está incorrecta"

    dd += dias
    c = 0
    if bisiesto (aaaa) == True: #En Caso de que sea bisiesto

        if  dd > 29:
            dd -= 29
            c += 1

     
    elif mm == 2:  

        if  dd > 28:
            dd -= 28
            c += 1
                        
    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:

        if  dd > 31:
            dd -= 31
            c += 1

    if mm == 4 or mm == 6 or mm == 9 or mm == 11:

        if dd > 30:
            dd -=  30
            c += 1
   
    if c == 1:
        mm +=1

    if mm > 12:
        mm -= 12
        aaaa += 1

    return dd * 1000000 + mm * 10000 + aaaa
        

    

def bisiesto (año):

    if año >= 2000:

        if año % 4 == 0:
            return True
        else:
            return False
    else:
        return "ERROR: AÑO DEBE SER >= 2000"

#función de la tarea anterior para validar que la fecha esté correta, mejorada (según yo XD)

def valida_fecha (fecha):

    if fecha < (1012000):
        return False
        """
        A pesar de que la fecha tiene que ser de 8 dijitos para poner una fecha que empieza com primero de algun mes no se puede porner 
        01032009 por ejemplo, porque que el programa pyton da error por lo que la fechas que empiezan con primero tienen que ponerse con
        7 dijitos
        """
        
    dd,mm,aaaa = dec_fecha (fecha)

    if aaaa < 2000:
        return False

    if 1 > mm or mm > 12:
        return False

    if bisiesto (aaaa) == True: #En Caso de que sea bisiesto

        if mm == 2:  

            if 1 > dd or  dd > 29:

                return False
            else:
                return True
    if mm == 2:  

        if 1 > dd or dd > 28:

            return False
        else:
            return True
                        
    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:

        if 1 > dd or dd > 31:

            return False
        else:
            return True

    if mm == 4 or mm == 6 or mm == 9 or mm == 11:

        if 1 > dd or dd > 30:
            
            return False
        else:
            return True
            
    return True

"""
Ejercicio 18: igualdad
Esta función resive dos numero esteros
Si no cumplen con las restricciones retorna un mensaje de error
Retrona un True si los digitos que hay en el primero número son los mismos que
estan en el segundo número sin importar el orden
En caso contrario retorna un False
"""

def igualdad (n1, n2):

    if isinstance (n1, int) == False or isinstance (n2, int) == False:
        return "ERROR: DATO DE ENTRADA DEBE SER UN ENTERO"

    n1 = abs(n1)
    n2 = abs(n2)
    
    digitos_n1 = digitos(n1)
    digitos_n2 = digitos(n2)
    
    c = 0
    c2 = 0
    c3 = 0
    entero = 0
    
    while c < digitos_n1:
        d = (n1//(10**c))%10

        while c2 < digitos_n2:
            if d == (n2//(10**c2))%10:
                entero += d * (10**c3)
                c3 += 1

            c2 += 1

        c2 = 0
        c += 1

    if entero != n1:
        return False
 
    
    c = 0
    c2 = 0
    c3 = 0
    entero2 = 0
    
    while c < digitos_n2:
        d = (n2//(10**c))%10

        while c2 < digitos_n1:
            if d == (n1//(10**c2))%10:
                entero2 += d * (10**c3)
                c3 += 1

            c2 += 1

        c2 = 0
        c += 1

    if entero2 != n2:
        return False

    return True















































