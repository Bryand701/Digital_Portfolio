"""
Bryand Brenes Zúñiga
2018093347
"""

"""
Fuunción para contar sumar los dígitos de un número
"""
def suma_digitos (n):

    c = 0
    suma = 0
    d = digitos (n)

    while c < d:
        suma += ((n//10**c)%10)
        c += 1

    return suma
"""
Función para contar los digitos de un número
"""
def digitos (n):

    c = 0

#esta parte aría falta en caso de que entre un 0, para poder contarlo
#no lo puse porque en el primer ejercicio el número debe ser mayor o igual a uno y no hacía falta
#pero lo utilize en los otros ejercicios y se me olvidó agregar esta parte
    #if n == 0: 
        #c = 1 
    
    while n != 0:
        n = n //10
        c += 1

    return c


#Ejercicio 1

"""
Esta función resive un número de entero que es la cantidad de número bonitos
que quiere que imprima la función
La restricciones son que el número sea entero y mayor o igual a 2
Imprime los número bonitos que calcule segun la formula
"""

def numeros_bonitos (n):
    #en el examen escribí insistance 
    if isinstance (n, int) == False:
        return "Error, el número debe ser entero"

    if n < 1:
        return "Error, el número debe ser mayor o igual a uno"

    c = 0
    c_2 = 8


    while c < n:

        s_formula = suma_digitos(3 * c_2 + 11)

        if s_formula == suma_digitos (c_2):
            print (c+1,".", c_2) #me faltó el "."
            c += 1

        c_2 += 1


# Ejercicio 2
"""
Resive un número(entre 0 y 9) que es el que hay que verificar si esta en la función resive
otro número(>=0) que es la cantidad de veces que hay que repetir ese número si es que está
y por ultimo resive el número(>=0) en el que hay que hacer todas las operaciones
Retorna el número ya operado
"""
def apariciones_seguidas (repetido,veces,numero):

    entero=0
    d = digitos (numero)
    c = 0
    c_2 = 0
    
    if numero == 0:
        return 0

    while c < d:
#d_actual es digito actual abrebiado
        d_actual = (numero//10**c)%10

        if d_actual != repetido:

            entero += d_actual * 10**c_2
            
            c_2 += 1
        else:
            j=0
            while j < veces:
                entero += d_actual * 10**c_2
                c_2 += 1
                j += 1
        c += 1

    return entero


#Ejercicio 4
"""
Esta función verifica si el número es primo
"""
def primo (n):

    c = 2

    while c < n:

        if n%c == 0:
            return False

        c += 1

    return True

"""
Esta función factoria el número(>0) que resive y va sumando los primos que lo dividen
con un cero a la izquierda
Retorna ya el número formado
"""

def secuencia_factores_primos (n):

    c = 2
    c_2 = 0
#para que el programa esté correcto debe ser entero = 0, no  = 1
    entero = 1

    while n != 1:
       
        if n % c == 0 and primo (c) == True:
#para que funciones tiene que ser "entero += c * 10** c_2"
            entero += c ** c_2

            n = n//c

            c_2 = digitos(entero) + 1

            c = 2
        else :
            c += 1
            

    return entero


#Ejercicio 3, el programa nunca va a servir porque revisa de derecha a izquierda, y es de izquierda a derecha, ademas de otros fallos de sintaxis menores
#Dichos errores estarán marcados
#Hice una version diferente que si funciona, esta funciona correctamente y la envié al profesor al correo por aparte
#De igual manera está incluida en este archivo
"""
Esta función resive un número que tiene que verificar si esta repetido
El segundo número que resive es sobre el cual hay que trabajar
El tercer numero es por el que hay que remplazar el repetido
Se supone que tiene que revisar el número de derecha a izquierda y remplazar
el número segun lo encuetre
Retorna el número ya arreglado
"""
def reemplazar (repetido, numero, rempla):

    d_n = digitos(numero)
    d_repe = digitos (repetido)
    #d_rem = digitos (rempla)
    d_rem = digitos (remplazar)

    c = 0
    c_2 = 0
    entero = 0

    while c < d_n:

        n_ex = ((numero//10**c) % 10 ** d_repe)
        print (n_ex)

        if n_ex == repetido:
            #entero += rempla * 10** c_2
            entero += rempla + 10** c_2
            c_2 += d_rem
            c += d_rem + 1
        else:
            entero += (n_ex%10)* 10 ** c_2
            c_2 += 1
            #c+=1
            c + 1
        
    return entero


"""
Esta función resive un número que tiene que verificar si esta repetido
El segundo número que resive es sobre el cual hay que trabajar
El tercer numero es por el que hay que remplazar el repetido
Revisa el número de derecha a izquierda y remplazael número segun lo encuetre
Retorna el número ya arreglado
"""
#Versión correcta del ejercicio 3 del exámen
def reemplazar (repetido, numero, rempla):

    d_n = digitos(numero)
    d_repe = digitos (repetido)
    d_rem = digitos (rempla)
    c = 0
    #Faltaria c_2 pero llegado a un punto me di cuenta que no lo utilicé y lo borré
    c_3 = d_n - d_repe
    entero = 0
    if repetido > numero:
        return numero
    while c < d_n:
        if c_3 >= 0:
            n_ex = ((numero//10**c_3) % 10 ** d_repe)
            if n_ex == repetido:
                entero = (entero*10**d_rem)+ rempla

                c_3 -=d_repe
                if d_rem < d_repe:
                    c += d_rem + 1

                elif d_rem == d_repe:
                    c += d_rem
                else:
                    c += d_rem - 1

            else:
                entero = (entero*10) + (n_ex// 10**(d_repe-1))

                c_3 -=1
                c += 1
        else:
            n_ex = (numero % 10 ** (d_repe-1))

            if n_ex == repetido:
                entero = (entero*10**d_rem)+ rempla

                c_3 -=d_repe
                c += d_rem + 1
            else:
                entero = (entero*10) + n_ex

                c_3 -=1
                c += 1
    return entero






















    
