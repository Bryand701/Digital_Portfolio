"""
Bryand Brenes Zuuñiga
2018093347
Tarea 2. Prácticas de las estructuras secuenciales y condicionales
"""

"""
Función para descomponer número de cuatro dígitos
Se utiliza en los ejercicion 3,4, 11
Las restricciones de estas funciones están en los programas utilizados
"""
def descomponer (número):
    millar = número // 1000
    cente = (número // 100) % 10
    dece = (número // 10) % 10
    uni = número % 10

    return millar, cente, dece, uni

"""
Función para descomponer fechas por año, mes y día
utilizada en ejercicios 9, 10
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
Ejercicio 1: determinar notas
Esta función  analiza la nota para determinar si un estuduante aprueba o no
Primero se analiza si el número esta en rango, si esta fuera de rango se retorna una nota de error
Luego se clasifica y se retorna la letra que se le asigne a la nota
La entrada es un número entero
La salida es el retorno una letra en fuunción a la nota,
La restricción es que la nota tiene que ser mayor o igual a 0 y menor o igual a 100
"""
def nota (nota):

    if nota >= 0:
        if nota == 100:
            return "A"
        elif 80 <= nota <= 99:
            return "B"
        elif 70 <= nota <= 79:
            return "C"
        elif 60 <= nota <= 69:
            return "E"
        elif nota < 60:
            return "F"
      
    else:
        return "Error: Nota debe estar entre 0 y 100"


"""
Ejercicio 2: calcular paridad
Esta función determina si un par de números son pares o impares
Se clasifican los número que resiva la función
Segun si ambos son divisibles entre dos para determinar si es par
o si ambos no son divisivles entre dos para determinar imparidad
si solo uno es par o impar se retorna un falso
Las entradas son dos números
La salidas son el retorno de "Par" si el programa determina que los dos números son pares,
"Impar" si el programa determina que los dos números son impares y False si uno es par y el otro impar
Las restricciones: el enunciado dice "no valide los datos"
"""
def paridad (numero1,numero2):
   
    if numero1 % 2 == 0 and numero2 % 2 == 0:
        return "Par"

    elif numero1 % 2 != 0 and numero2 % 2 != 0:
        return "Impar"

    else:
         return False

"""
Ejercicio 3: pares_impares
Este programa separa un número de cuatro digitos y los divide en pares e impares
Primero se analiza si el número esta en rango, si esta fuera de rango se retorna una nota de error
Priemero se descompone el número
Luego se analizan todos los casos posibles para determinar su posicionamiento
Con el contador (cpares, cimpares) se decide su posicionamiento en el resultado final al sumar
un 1 y elevarlo a un 10 y luego multiplicarlo por el número (uni, dece, cente, millar)
La entrada es un número entero de 4 dígitos
La salida es un return con los número pares, números impáres
La restrición es si el número es de menos ó más de cuatro digitos, cuyo caso retorna un mensaje de error
"""
def pares_impares (número):

    if 1000 <= número < 10000:

        millar, cente, dece, uni = descomponer (número)

        pares = 0
        impares = 0
        cpares = 0
        cimpares = 0    
     
        if uni % 2 == 0:
            pares = uni
            cpares +=1
        else:
            impares = uni
            cimpares +=1

        if dece % 2 == 0:
            pares += dece * (10 ** cpares)
            cpares += 1
        else:
            impares += dece * (10 ** cimpares)
            cimpares += 1

        if cente % 2 == 0:
            pares += cente * (10 ** cpares)
            cpares += 1 
        else:
            impares += cente * (10 ** cimpares)
            cimpares += 1

        if millar % 2 == 0:
            pares += millar * (10 ** cpares)        
        else:
            impares += millar * (10 ** cimpares)
                
        if pares != 0 and impares != 0:
            return pares, impares
        elif pares == 0 and impares != 0:
            return "na hay", impares
        elif pares != 0 and impares == 0:
            return pares, "na hay"     
 
    else:
        return "Error: debe estar en el rango de 1000 a 9999"

"""
Ejercicio 4:  contar_pares_impares
Esta función cuanta la cantidad de número pares e impares que tiene un número de 4 digitos, el cual es la entrada
Primero se analiza si el número está en rango, si esta fuera de rango se retorna una nota de error
Segundo se descomponen los números
Luego se analiza si alguno de los números descompuestos es 0
Si es así se le resta un 1 a los pares, pues a la hora de procesarlo lo contará como par
Luego se analiza si el los números son pares o impares, se le suma un 1 al contador
Al final se retornan los contadores
"""

def contar_pares_impares (número):

    if 0 <= número < 10000:

        millar, cente, dece, uni = descomponer (número)

        pares = 0
        impares = 0

        if millar == 0:
            pares -= 1

        if cente == 0:
            pares -= 1

        if dece == 0:
            pares -= 1

        if uni == 0:
            pares -= 1
        
        if uni % 2 == 0:
            pares += 1
        else:
            impares += 1

        if dece % 2 == 0:
            pares += 1
        else:
            impares += 1

        if cente % 2 == 0:
            pares += 1
        else:
            impares += 1

        if millar % 2 == 0:
            pares += 1
        else:
            impares += 1

        return pares,impares
    
    else:
        return "Error: debe estar en el rango de 0 a 9999"

"""
Ejercicio 5: minicalculadora
Esta función es una calculadora
Las entradas son dos números y un operador
Primero se analiza si el operador está correcto, si es incorreto se retorna un mensaje de error
Luego se analiza que tipo de operador es y se prosede con la operación
Si el operador es un / se analiza que el dividendo sea diferente de 0
Si no lo es se retorna un mensaje de error
"""

def minicalculadora (numero1, numero2, operador):   

    if operador == "*" or operador == "+" or operador == "-" or operador == "/":        

        if operador == "+":           
            operacion = numero1 + numero2
            return operacion
        
        elif operador == "-":           
            operacion = numero1 - numero2
            return operacion
        
        elif operador == "*":         
            operacion = numero1 * numero2
            return operacion
        
        else:
            if numero2 != 0:
                operacion = numero1 / numero2
                return operacion
            
            else:
                return "Error: el divisor debe ser diferente de cero"
                
    else:

        return "Error: código de operación debe ser +, -, / o *"


"""
Ejercicio 6: mayor
Esta función resive tres números y analiza cual es el mayor de los tres
Primero se compara el primer número con los otror dos, si es el mayor, se asigna a superior 
(la variable no está escrita como mayor si no como superior para evitar problemas, ya que la función se llama mayor)
Si no, se compara el segundo con el tercero
Y si no se asigna el tercer número como el mayor
"""

def mayor (numero1, numero2, numero3):

    if numero1 > numero2 and numero1 > numero3:
        superior = numero1
    elif numero2 > numero3:
        superior = numero2
    else:
        superior = numero3

    return superior
        
"""
Ejercicio7: orden_descendente
Esta función resive tres números y los ordena de mayor a menor
Primero se utiliza la función creada en el ejercicio anterior para determinar al mayor
Luego se se comparan los otros dos números para determinar el orden
"""

def orden_descendente (numero1, numero2, numero3):

    superior = mayor (numero1, numero2, numero3)
    
    if numero1 == superior:

        if numero2 > numero3:
            return numero1, numero2, numero3

        else:
            return numero1, numero3, numero2
        
    elif numero2 == superior:
        
        if numero1 > numero3:
            return numero2, numero1, numero3

        else:
            return numero2, numero3, numero1
    else:
        
        if numero1 > numero2:
            return numero3, numero1, numero2

        else:
            return numero3, numero2, numero1

"""
Ejercicio8: bisiesto
Esta funcion analiza si un año es bisiesto
Primero se analiza si el número esta en rango (mayor o igual a 2000), si esta fuera de rango se retorna una nota de error
Luego se analiza si el año es divisivbe por 4
Si asi es, se retorna un true, de lo contrario un false
"""

def bisiesto (año):

    if año >= 2000:

        if año % 4 == 0:
            return True
        else:
            return False
    else:
        return "ERROR: AÑO DEBE SER >= 2000"

"""
Ejercicio9: valida_fecha
Esta función analiza si una fecha esta correctamente escrita
Primero se analiza que la fecha esté en el rango establecido (primero de enero del 2000 en adelante)
Luego se descompone la fecha
despues se verifica que el año sea superior al 2000
despues que los meses esnten entre 1 y 12
luego se verifica si el año es bisiesto
luego se añaliza que el día este a corde con el mes
Se retorna un True si la fecha esta bien y un False en caso contrario
"""

def valida_fecha (fecha):

    if fecha >= (1012000):
        """
        A pesar de que la fecha tiene que ser de 8 dijitos para poner una fecha que empieza com primero de algun mes no se puede porner 
        01032009 por ejemplo, porque que el programa pyton da error por lo que la fechas que empiezan con primero tienen que ponerse con
        7 dijitos
        """
        
        dd,mm,aaaa = dec_fecha (fecha)

        if aaaa >= 2000:

            if 0 < mm < 13:

                if bisiesto (aaaa) == True: #En Caso de que sea bisiesto

                    if mm == 2:  

                        if 0 < dd < 30:

                            return True

                        else:
                            return False
                    
                        
                    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:

                        if 00 < dd < 32:

                            return True

                        else:
                            return False

                    if mm == 4 or mm == 6 or mm == 9 or mm == 11:

                        if 00 < dd < 31:

                            return True

                        else:
                            return False 
            
                else: #En caso de que no sea bisiesto
                    if mm == 2:  

                        if 0 < dd < 29:

                            return True

                        else:
                            return False
                    
                    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:

                        if 00 < dd < 32:

                            return True

                        else:
                            return False
                        
                    if mm == 4 or mm == 6 or mm == 9 or mm == 11:

                        if 00 < dd < 31:

                            return True

                        else:
                            return False           

            else:
                return False
           
        else:
            
            return False
    else:
        return False

"""
Ejercicio 10: fecha
Esta función resive una fecha (primero de enero del 2000 en adelante) con formato ddmmaaaa
primero se descompone la fecha
luego se valida que la fecha esté correcta con el ejercicio anterior
luego se analiza el mes y se retorna la fecha segun el mes
"""

def fecha (día_mes_año):

    dd,mm,aaaa = dec_fecha (día_mes_año)

    if valida_fecha (día_mes_año) == True:

        if mm == 1:
            return dd, "enero", aaaa
        elif mm == 2:
            return dd, "febrero", aaaa
        elif mm == 3:
            return dd, "marzo", aaaa
        elif mm == 4:
            return dd, "abril", aaaa
        elif mm == 5:
            return dd, "mayo", aaaa
        elif mm == 6:
            return dd, "junio", aaaa
        elif mm == 7:
            return dd, "julio", aaaa
        elif mm == 8:
            return dd, "agosto", aaaa
        elif mm == 9:
            return dd, "septiembre", aaaa
        elif mm == 10:
            return dd, "octubre", aaaa
        elif mm == 11:
            return dd, "noviembre", aaaa
        else:
            return dd, "diciembre", aaaa 

    else:
        return False

"""
Ejercicio 11: elimina_digito
Esta función resive un dígito menor a 10 y mayor a 0,  y un número de 4 dígitos
Primero se validan las restricciones
Luego se descompone el número
Luego se analiza que el número sea diferente del digito
Si así es, se suma al entero (que sería el número reconstrudo ya eliminado el digito)
Y se suma un 1 a la elevación para elevar al diez que seria la forma de saber
la ubicación del número ya reconstruido
Al final se retorna entero.
"""

def elimina_digito (digito, numero):

    elevar = 0
    entero = 0

    if (0 > digito or digito > 10)and (1000 > numero or numero > 10000):

        return "ERROR EN DÍGITO Y EN NÚMERO"

    elif 0 > digito or digito > 10:

        return "ERROR EN DIGITO"

    elif 1000 > numero or numero > 10000:

        return "ERROR EN NÚMERO"

    else:
        millar, cente, dece, uni = descomponer (numero)

        if uni != digito:

            entero = uni
            elevar += 1

        if dece != digito:
            entero += dece * (10 ** elevar)
            elevar += 1

        if cente != digito:
            entero += cente * (10 ** elevar)
            elevar += 1

        if millar != digito:
            entero += millar * (10 ** elevar)

        if entero == 0:
            entero = -1

        return entero


"""
Ejercicio 12: convertir_segundos
Esta función resive segundos, y un str con la conversión que quiere realisar
Se naliza a que quiere convertir el usuaro los segundos
En caso de que esté correcta la conversión que quiere se aplica la formula necesaria
y se retorna los segundos ya convertidos
De lo contrario se retorna un mensaje de error
"""

def convertir_segundos (segundos, conversion):

    if conversion == "segundos":

        return segundos

    elif conversion == "minutos":
        
        minutos = segundos / 60
        return minutos

    elif conversion == "horas":
        
        horas = segundos / 3600
        return horas

    elif conversion == "dias":

        dias = segundos / 86400
        return dias

    elif conversion == "semanas":
        semanas = segundos / 604800
        return semanas

    else:
        return "ERROR, LA CONVERSIÓN ES A: segundos, minutos, horas, dias y semanas"

"""
Ejercicio 13: digitos_en_comun
Esta funcion resive dos número mayores a 0 y menores a 1000
Primero se verifica que los números esten en rango, si no lo estan se retorna un mensaje de error
Si estan bien, se descomponen ambos número en unidades, decenas y centenas
Si en el primer número esta repetido alguno de los digitos se le asigna un -1 para que
no aparesca dos veces en el entero (resultado final de los números repetidos ya sumados)
Luego se analiza si los numero son iguales
Si así es, se suma al entero 
Y se suma un 1 a la elevación para elevar al diez que seria la forma de saber
la ubicación del número ya reconstruido
Al final se retorna el entero
"""
    
def digitos_en_comun (numero1, numero2):

    elevar = 0
    entero = 0

    if (0 >= numero1 or numero1 > 1000)and (0 >= numero2 or numero2 > 1000):

        return "ERROR EN DÍGITO1 Y EN DIGITO2"

    elif 0 >= numero1 or numero1 > 1000:

        return "ERROR EN DIGITO1"

    elif 0 >= numero2 or numero2 > 1000:

        return "ERROR EN DIGITO2"

    else:
        
        cente1 = numero1 // 100
        dece1 = (numero1 // 10) % 10
        uni1 = numero1 % 10

        cente2 = numero2 // 100
        dece2 = (numero2 // 10) % 10
        uni2 = numero2 % 10

        if dece1 == uni1 or dece1 == cente1:
            dece1 = -1

        if cente1 == uni1 or cente1  == dece1:
            cente1 = -1
        
        if uni1 == uni2 or uni1 == dece2 or uni1 == cente2:

            entero = uni1
            elevar += 1

        if dece1 == uni2 or dece1 == dece2 or dece1 == cente2:
            entero += dece1 * (10 ** elevar)
            elevar += 1

        if cente1 == uni2 or cente1 == dece2 or cente1 == cente2:
            entero += cente1 * (10 ** elevar)

        if entero == 0:
            entero = False

        return entero

"""
Ejercicio 14: dobleDeImpar
Esta función resive un número entero y verifica si su mitad es impar
Primero se divide el número entre dos
Luego al resultado de su división  se le calcula el residuo de dividirlo entre 2
Si es diferente a 0 es impar de los contrario es par
Se retorna un True si es impar y un false si es par
"""

#En los ejemplos del profesor dice que 21 y 15 da false pero 21 y 15 si son el doble de un impar
#Ya que sus mitades son 10.5 y 7.5 y son números impares, si quería que fuera el doble de un número impar entero
#Debió espesificarlo en las instrucciones
def dobleDeImpar (numero):

    if (numero / 2) % 2 != 0:
        return True

    else:
        return False

"""
Ejercicio 15: reforestar
Esta función resive un número entero mayor o igual a 0 para determinar la cantidad de
árboles se tienen que plantar
primero se verifica que los datos de entrada estén correctos, si están incorrectos se retorna un mensaje de error
luego se convierte las hectareas a metros
Se analiza a acual de las dos formas de distribución de arboles pertece
Luego se destribuyen los arboles segun su espacio designado
Se  retorna la cantidad de arboles plantados
"""
        
def reforestar (hectareas):

    if hectareas - int(hectareas) == 0:

        if hectareas >= 0:

            metros = hectareas * 10000
        
            if metros >= 100000:

                met_pinos = metros * 0.5
                met_eucalipto = metros * 0.3
                met_cedros = metros * 0.2
                
                pinos_plantados = int((met_pinos/10) * 8)
                eucaliptos_plantados = int(met_eucalipto)
                cedros_plantados = int((met_cedros/18) * 10)
                
                return "Cedros plantados: ",cedros_plantados,"Pinos plantados: ",pinos_plantados,"Eucaliptos plantados: ",eucaliptos_plantados

            else:
                met_pinos = metros * 0.4
                met_eucalipto = metros * 0.25
                met_cedros = metros * 0.35
                
                pinos_plantados = int((met_pinos/10) * 8)   
                eucaliptos_plantados = int(met_eucalipto)
                cedros_plantados = int((met_cedros/18) * 10)
                
                return "Cedros plantados: ",cedros_plantados,"Pinos plantados: ",pinos_plantados,"Eucaliptos plantados: ",eucaliptos_plantados

        else:
            return "ERROR: LAS HECTAREAS TIENEN QUE SER >= 0"

    else:
        return "ERROR: LAS HECTAREA TIENEN QUE SER UN NUMERO ENTERO"

"""
Ejercicio 16: cuenta_bancaria
Esta función es para manejar los ahorros de una cuenta bancaria
Resive  el saldo actual de la cuenta, un número representando la operación que desea realizar
y el monto con el que desea trabajar
Primero se analiza cual operación es requerida
En caso de que ponga un número que no corresponda a una operación se retorna un False
Despues se analiza que el monto desea retirar o depositar sea un multiplo de 5000
Si es se opera segun la operación y se retorna el saldo actualizado
Si no es multiplo del 5000 se retorna un False
"""

def cuenta_bancaria (saldo_actual, operacion, monto):

    if saldo_actual >= 0:

        if operacion == 1: #Deposito

            if monto % 5000 == 0 and monto >= 5000:

                saldo_actual += monto
                return saldo_actual
            
            else:
                return False
        
        elif operacion == 2: #Retiro

            if monto % 5000 == 0 and monto >= 5000:

                if monto < saldo_actual:

                    saldo_actual -= monto
                    return saldo_actual
                else:
                    return False
            
            else:
                return False

        else:
            return False

    else:
        return False

"""
Ejercicio 17: desglose
Esta función resive un número mayor o igual a 5000, y desglosa la cantidad minima de billetes
necesarios para  representar esa cantidad
Primero se analiza si el monto esta en el rango aceptable, si no lo está se retorna un false
De lo contrario se procede a dividir el monto en los billites
Luego se van imprimiendo uno a uno los billites empezando de mayor a menor
Si la cantidad de billetes es igual a 0, no se retorna el mensaje con la cantidad de ese billete
(eje: hay 0 billetes de 50000, no se  imprime el mensaje con "0 billetes de 50000")
"""

def desglose (monto):

    if monto % 5000 == 0 and monto >= 5000:

        cicuenta_mil =  monto//50000
        veinte_mil= (monto%50000)//20000
        diez_mil = ((monto%50000)%20000)//10000
        cinco_mil = (((monto%50000)%20000)%10000)//5000

        print ("Desglose de billetes:")

        if cicuenta_mil != 0:
            
            print (cicuenta_mil, " de 50000", "         ", 50000*cicuenta_mil)

        if veinte_mil != 0:
            
            print (veinte_mil, " de 20000", "         ", 20000*veinte_mil)

        if diez_mil != 0:
            
            print (diez_mil, " de 10000", "         ", 10000*diez_mil)

        if cinco_mil != 0:
            
            print (cinco_mil, " de 5000", "          ", 5000*cinco_mil)

        print ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
 
        print ("Total desglosado     ",  cicuenta_mil * 50000 + veinte_mil * 20000 + diez_mil * 10000 + cinco_mil * 5000)

    else:
        return False

"""
Ejercicio 18: cajero
Esta función es para manejar los ahorros de una cuenta bancaria
Resive  el saldo actual de la cuenta, un número representando la operación que desea realizar
y el monto con el que desea trabajar
Primero se le asigna a nuevo_saldo el retorno de la función cuenta_bancaria
Luego se analiza si el usuario retira dinero o deposita
En caso de retirar se imprime nuevo_saldo y se manda  el nuevo_saldo a la función desglose y se imprime
En caso contrario solo se imprime el nuevo saldo
Todo lo anterior en caso de que cumplan las restricciones, en caso contrario se retorna un False
"""

def cajero (saldo_actual, operacion, monto):

    nuevo_saldo = cuenta_bancaria (saldo_actual, operacion, monto)       

    if saldo_actual >= 0:

        if operacion == 1: #Deposito

            if monto % 5000 == 0 and monto >= 5000:

                print (nuevo_saldo)
            
            else:
                return False
        
        elif operacion == 2: #Retiro

            if monto % 5000 == 0 and monto >= 5000:

                if monto < saldo_actual:

                    print (nuevo_saldo)
                    print (desglose (nuevo_saldo))

                else:
                    return False
            
            else:
                return False

        else:
            return False

    else:
        return False


"""
Ejercicio 19: pago_celular
Esta función resive tres valores, los minutos gastados en llamandas, los mensajes enviados,
y el plan de internet que se tiene
Primero se asigna a tarifa 2750 pues es la tarifa base
Luego se valida si los minutos de llamadas y los mensajes estan bien, si no, se imprime un mensaje de error
Luego se analizan los minutos para si tienen minutos en exeso, y como se deben cobrar eso minutos en exeso
Luego se le suma a la tarifa el costo de los mensajes
Luego el plan al que pertenese, si el plan está mal digitado, se imprime un mensaje de error
Se aplican los impuestos
Se suman los 200 colones de la curz roja
Y se retorna la tarifa ya con todos los costos ya calculados
"""

def pago_celular(minutos, mensajes, plan):

    tarifa = 2750

    if minutos < 0:
        return "ERROR: LOS MINUTOS DE LLAMANDAS TIENEN QUE SER >= 0"

    elif mensajes < 0:
        return "ERROR: LOS MENSAJES TIENEN QUE SER >= 0"

    elif 121 > minutos > 60:

        tarifa += (minutos - 60) * 50

    elif 120 < minutos:

        tarifa += 60*50 + (minutos - 120) * 35

    tarifa += mensajes * 3

    if plan == 0:
        pass

    elif plan == 1:
        tarifa += 12000

    elif plan == 2:
        tarifa += 15000

    elif plan == 3:
        tarifa += 25000

    else:
        return "ERROR: EL PLAN TIENE QUE SER 0, 1, 2 ó 3"

    tarifa += (tarifa *0.13)
    tarifa += 200
        
    return tarifa


"""
Ejercicio 20: nombre_dia
Esta función resive una fecha en formato ddmmaaaa
primero se descompone la fecha
luego se valida que la fecha esté correcta, si no lo está e retorna un mensaje de error
luego se aplica la formula encontrada en la wikipedia
despues se le asigna un mes a mm
Luego se imprime dependiendo de lo que de la formula
"""

def nombre_dia (dia_mes_año):

    dd,mm,aaaa = dec_fecha (dia_mes_año)


    if aaaa < 2000: #La función valida_fecha solo sirve para años superiores al 2000, por lo se hace este arreglo para evitar problemas
                    # En este ejercicio no está esa restricción por lo que se debe corregir en caso de que se quiera buscar una fecha anterior al 2000
        
        dia_mes_año = dd * 1000000 + mm * 10000 + 2000


    if valida_fecha (dia_mes_año) == False:

        return "ERROR: FECHA INCORRECTA"

    a = int((14 - mm) / 12)


    y = aaaa - a

    m = mm + 12 * a - 2

    dia = int((dd + y + int(y/4) - int(y/100) + int(y/400) + (31*m)/12) % 7)

    if mm == 1:
        mes = "enero"

    elif mm == 2:
        mes = "febrero"

    elif mm == 3:
        mes = "Marzo"

    elif mm == 4:
        mes = "Abril"

    elif mm == 5:
        mes = "Mayo"

    elif mm == 6:
        mes = "Junio"

    elif mm == 7:
        mes = "Julio"

    elif mm == 8:
        mes = "Agosto"

    elif mm == 9:
        mes = "Septiembre"

    elif mm == 10:
        mes = "Octubre"

    elif mm == 11:
        mes = "Noviembre"

    else:
        mes = "Diciembre"


    if dia == 0:

        print ("Domingo", dd, "de", mes, "de", aaaa)

    elif dia == 1:

        print ("Lunes", dd, "de", mes, "de", aaaa)

    elif dia == 2:

        print ("Martes", dd, "de", mes, "de", aaaa)

    elif dia == 3:

        print ("Miércoles", dd, "de", mes, "de", aaaa)

    elif dia == 4:

        print ("Jueves", dd, "de", mes, "de", aaaa)

    elif dia == 5:

        print ("Viernes", dd, "de", mes, "de", aaaa)

    elif dia == 6:

        print ("Sabado", dd, "de", mes, "de", aaaa)

    





















    
