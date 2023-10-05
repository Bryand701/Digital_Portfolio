"""
Bryand Brenes Zúñiga
2018093347
Quiz 5
"""
"""
Ejercicio 1
La función resive una matriz, a la vual hay que verificar que la
suma en diagonal, horizontal y vertical de sus números, de siempre el
mismo resultado
"""
def cuadrado_magico (matriz):
    comparar = 0
    c = 0
    while c < len(matriz):
        suma = 0
        for matriz in matriz[c]:
            suma += matriz
        if comparar == 0:
            comparar = suma
        elif comparar != suma:
            return False
        c += 1
    c = 0
    while c < len(matriz):
        suma = 0
        for matriz in range (len(matriz)):
            suma += matriz[c][matriz]
        if comparar != suma:
            return False
        c += 1

    c = 0
    while c < 2:
        suma = 0
        if c == 0:
            for matriz in range (len(matriz)):
                suma += matriz[matriz][matriz]        
        else:
            t = len(matriz)-1
            for matriz in range (len(matriz)):
                suma += matriz[matriz][t]
                t -=1
        if comparar != suma:
            return False
        c += 1
    return True


def cuadrado_magico_p(matriz):
    if horizontal(matriz,0,0,len(matriz),0) == False:
        return False
    elif vertical(matriz,0,0,len(matriz),0) == False:
        return False
    elif diagonal(matriz,2,0,len(matriz),0) == False:
        return False
    return True

def horizontal (matriz,c,suma,tamaño,comparar):
    if c == tamaño:
        if comparar != suma:
            return False
        else:
            return True
    else:
        suma = sumas_horizontal(matriz[c],0,0)
        if comparar == 0:
            comparar = suma
        if comparar != suma:
            return false
        else:
            return horizontal (matriz,c+1,suma,tamaño,comparar)
            
        
def sumas_horizontal (lista,c,suma):
    if c == len(lista):
        return suma
    else:
        suma += lista[c]
        return sumas_horizontal (lista,c+1,suma)

def vertical (matriz,c,suma,tamaño,comparar):
    if c == tamaño:
        if comparar != suma:
            return False
        else:
            return True
    else:
        suma = sumas_vertical(matriz,c,0,0)
        if comparar == 0:
            comparar = suma
        if comparar != suma:
            return false
        else:
            return vertical (matriz,c+1,suma,tamaño,comparar)

def sumas_vertical (matriz,c,c2,suma):
    if c2 == len(matriz):
        return suma
    else:
        suma += matriz[c][c2]
        return sumas_vertical (matriz,c,c2+1,suma)


def diagonal(matriz,c,suma,tamaño,comparar):
    if c == 3:
        if comparar != suma:
            return False
        else:
            return True
    else:
        if c == 0:
            suma = sumas_diagonal_1(matriz,c,0,0)
        else:
            suma = sumas_diagonal_2(matriz,0,len(matriz)-1,0)
        if comparar == 0:
            comparar = suma
  
        if comparar != suma:
            return False
        else:
            return diagonal (matriz,c+1,suma,tamaño,comparar)
            

def sumas_diagonal_1 (matriz,c,c2,suma):
    if c == len(matriz):
        return suma
    else:
        suma += matriz[c][c2]
        return sumas_diagonal_1 (matriz,c+1,c2+1,suma)

def sumas_diagonal_2 (matriz,c,c2,suma):
    if c == len(matriz):
        return suma
    else:
        suma += matriz[c][c2]
        return sumas_diagonal_2 (matriz,c+1,c2-1,suma)



"""
Ejercioio 2
la función resive una matriz y un número, si el número es uno
se sustitullen todos los elemento de la matriz que estén debajo de la diagonal
principal por 0
si es dos todos los que estén por encima
y si es 3 todos los que estén por encima y por debajo
"""



#POO

"""
Ejercicio 9
En este ejercicio hay que crea una clase para administrar una cuenta de un banco
Tambien hay que crea un menú para trabajar con esta cuenta
Dentro de las opciones pdel menú están
Crear cuenta
Depositar dinero
Retirar dinero
Ver saldo
Ver estado de la cuenta
Desactivar cuenta
Activar cuenta
Cambiar cuenta
salir
"""

class cuenta_banco_class:
    numero_cuenta = 0
    nombre_cliente = ""
    saldo = 0
    total_depósitos  = 0
    contador_depositos = 0
    total_retiros = 0
    contador_retiros = 0
    estado_cuenta = True

    def asignar_datos(self,numero_cuenta,nombre_cliente):
        self.numero_cuenta = numero_cuenta
        self.nombre_cliente = nombre_cliente

    def depositar (self,dinero):
        if self.estado_cuenta:            
            self.saldo += dinero
            self.total_depósitos += dinero
            self.contador_depositos += 1
        else:
            print("Cuenta Inactiva")
            
    def retirar (self, dinero):
        if self.estado_cuenta:
            if dinero > self.saldo:
                print ("Fondos insuficientes")
            else:
                self.saldo -= dinero
                self.total_retiros += dinero
                self.contador_retiros += 1
        else:
            print("Cuenta Inactiva")
    def ver_saldo (self):
        return self.saldo
    def estado (self):
        lista = [self.numero_cuenta,self.nombre_cliente,self.saldo,self.total_depósitos,self.contador_depositos,self.total_retiros,self.contador_retiros,self.estado_cuenta]
        return lista
    def cerrar_cuenta(self):
        self.estado_cuenta = False
    def activar_cuenta(self):
        self.estado_cuenta = True
    def asignar (self,lista):
        self.numero_cuenta = lista[0]
        self.nombre_cliente = lista[1]
        self.saldo = lista[2]
        self.total_depósitos = lista[3]
        self.contador_depositos = lista[4]
        self.total_retiros = lista[5]
        self.contador_retiros = lista[6]
        self.estado_cuenta = lista[7]
        
        
def cuenta_banco ():
    from os import system
    cuenta_del_banco = cuenta_banco_class()
    dicc = {}
    cuenta = 0
    while True:
        print ("1. Crear cuenta")
        print ("2. Depositar dinero")
        print ("3. Retirar dinero")
        print ("4. Ver saldo")
        print ("5. Ver estado de la cuenta")
        print ("6. Desactivar cuenta")
        print ("7. Activar cuenta")
        print ("8. Cambiar cuenta")
        print ("9. salir")
        opcion = int(input("Escriba la opción que desea realizar: "))
        if opcion == 1:
            if cuenta != 0:
                dicc[cuenta] = cuenta_del_banco.estado()                
            nombre = str(input("Escriba su nombre: "))
            cuenta = int(input("Escriba su cuenta: "))
            cuenta_del_banco = cuenta_banco_class()
            cuenta_del_banco.asignar_datos(cuenta,nombre)
            dicc[cuenta] = cuenta_del_banco.estado()
        elif opcion == 2:
            dinero = int(input("Escriba la cantidad de dinero a depositar: "))
            cuenta_del_banco.depositar(dinero)
        elif opcion == 3:
            dinero = int(input("Escriba la cantidad de dinero a depositar: "))
            cuenta_del_banco.retirar(dinero)
        elif opcion == 4:
            print (cuenta_del_banco.ver_saldo())
        elif opcion == 5:
            tup = cuenta_del_banco.estado()
            print ("Nuemro de cuenta: ", tup[0])
            print ("Nombre del cliete: ", tup[1])
            print ("Saldo: ", tup[2])
            print ("Todal de depósitos: ", tup[3])
            print ("Cantida de depósitos: ", tup[4])
            print ("Total de retiros: ", tup[5])
            print ("Cantidad de retiros: ", tup[6])
            if tup[7]:
                print ("Estado de la cuenta: Activa")

            else:
                print ("Estado de la cuenta: Inactiva")           
        elif opcion == 6:
            cuenta_del_banco.cerrar_cuenta()
        elif opcion == 7:        
            cuenta_del_banco.cerrar_cuenta()
        elif opcion == 8:
            dicc[cuenta] = cuenta_del_banco.estado()
            cuenta_n = int(input("Escriba la cuenta con la que desea trabajar: "))
            if cuenta_n not in dicc:
                print ("La cuenta no existe, por favor creela primero")
            else:
                cuenta_del_banco.asignar(dicc[cuenta_n])                           
            
        elif opcion == 9:
            break
        else:
            print ("ERROR: No existe esa opción")
        print ("")
       
            
"""
Ejercicio 10
"""

class fracciones_class:
    numerador = 0
    denominador = 0

    def asignar_numerador(self,numero):
        print(numero)
        self.numerador = numero
    def asignar_denominador (self,numero):
        self.denominador = numero
    def mostrar_fraccion (self):
        print(numerador, r"/", denominador)
    def __add__ (self,obj):
        return self.numerador + obj.nuemerador, self.denominador + obj.denominador
    
    
def fracciones ():
    fracc_2 = fracciones_class

    numerador1 = int(input("Numerador fracción 1: "))
    denominador1 = int(input("Denominador fracción 1: "))
    
    fracc_1 = fracciones_class
    
    fracc_1.asignar_numerador(numerador1)
    
    fracci_1.asignar_denominador(denominador1)

    numerador2 = int(input("Numerador fracción 2: "))
    denominador2 = int(input("Denominador fracción 21: "))
    fracc_2.asignar_numerador(numerador2)
    fracci_2.asignar_denominador(denominador2)

    j = fracc_1 + fracc_2
    print(j)
        
        
    


























            
        
