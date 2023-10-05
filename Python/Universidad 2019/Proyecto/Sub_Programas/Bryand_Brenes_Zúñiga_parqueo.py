import tkinter
from tkinter import *
from tkinter import messagebox as mb
import time
import webbrowser


#Globales
global espacios, espacios_c, precio_hora, pago_minimo, redondeo, min_max, mon_1, mon_2, mon_3, billete_1, billete_2, billete_3, billete_4, billete_5
global c_mon_1, c_mon_2, c_mon_3 ,c_billete_1, c_billete_2, c_billete_3, c_billete_4, c_billete_5, s_mon_1, s_mon_2, s_mon_3, s_billete_1
global s_billete_2, s_billete_3, s_billete_4, s_billete_5, salidas_mon_1, salidas_mon_2, salidas_mon_3, salidas_billete_1, salidas_billete_2
global salidas_billete_3 ,salidas_billete_4 ,salidas_billete_5, total_mon_1, total_mon_2, total_mon_3
global total_billete_1, total_billete_2, total_billete_3, total_billete_4, total_billete_5, espacios_ocupados
espacios = [] #Lista de los espacios para carros
espacios_c = 0 #Numero de espacios para carros
precio_hora = 0 #Precio por hora del parqueo
pago_minimo = 0 #Pago minimo del parqueo
redondeo = 0 #Minutos redondeados para calcular el pago 
min_max = 0 #Minutos maximos para salir depues de pagar
mon_1 = 0 #Valor de la Moneda 1
mon_2 = 0 #Valor de la Moneda 2
mon_3 = 0 #Valor de la Moneda 3
billete_1 = 0 #Valor del billete 1
billete_2 = 0 #Valor del billete 2
billete_3 = 0 #Valor del billete 3
billete_4 = 0 #Valor del billete 4
billete_5 = 0 #Valor del billete 5
c_mon_1 = 0 #Cantidad demonedas 1, tomado como entrada
c_mon_2 = 0 #Cantidad demonedas 2, tomado como entrada
c_mon_3 = 0 #Cantidad demonedas 3, tomado como entrada
c_billete_1 = 0 #Cantidad de billetes 1, tomado como entrada
c_billete_2 = 0 #Cantidad de billetes 2, tomado como entrada
c_billete_3 = 0 #Cantidad de billetes 3, tomado como entrada
c_billete_4 = 0 #Cantidad de billetes 4, tomado como entrada
c_billete_5 = 0 #Cantidad de billetes 5, tomado como entrada
s_mon_1 = str(mon_1) #String de el valor de la moneda 1
s_mon_2 = str(mon_2) #String de el valor de la moneda 2
s_mon_3 = str(mon_3) #String de el valor de la moneda 3
s_billete_1 = str(billete_1) #String de el valor del billete 1
s_billete_2 = str(billete_2) #String de el valor del billete 2
s_billete_3 = str(billete_3) #String de el valor del billete 3
s_billete_4 = str(billete_4) #String de el valor del billete 4
s_billete_5 = str(billete_5) #String de el valor del billete 5
salidas_mon_1 = 0 #Salidas de la moneda 1
salidas_mon_2 = 0 #Salidas de la moneda 2
salidas_mon_3 = 0 #Salidas de la moneda 3
salidas_billete_1 = 0 #Salidas del billete 1
salidas_billete_2 = 0 #Salidas del billete 2
salidas_billete_3 = 0 #Salidas del billete 3
salidas_billete_4 = 0 #Salidas del billete 4
salidas_billete_5 = 0 #Salidas del billete 5
total_mon_1 = 0 #Entrada menos salidas de monedas
total_mon_2 = 0 #Entrada menos salidas de monedas
total_mon_3 = 0 #Entrada menos salidas de monedas
total_billete_1 = 0 # Entrada menos salidas de billetes
total_billete_2 = 0 # Entrada menos salidas de billetes
total_billete_3 = 0 # Entrada menos salidas de billetes
total_billete_4 = 0 # Entrada menos salidas de billetes
total_billete_5 = 0 # Entrada menos salidas de billetes
espacios_ocupados = 0 #Espacios que actualmente están ocupados


#Funciones

#Función para crear la cantidad de espacios con listas vacias
def espacio (c):
    global espacios
    espacios = []
    for x in range (c):
        espacios.append([])
    return espacios
        
#Funcion para habilitar las otras opciones del menu_prg despues de meter todos los datos obligatorios
def habilitar ():
    menubarra.entryconfig("Dinero del cajero", state="normal")
    menubarra.entryconfig("Entreda de vehículo", state="normal")
    menubarra.entryconfig("Cajero del Parqueo", state="normal")
    menubarra.entryconfig("Salida de vehículo", state="normal")

#Funciones para motrar un error
def error(x):
    x = str(x)
    r = mb.showwarning("!!ERROR!!", x + " no cumple con las condiciones solicitadas, ¡Reviselo por favor!")	

def error_2():
    r = mb.showwarning("!!ERROR!!","Algo de lo que digitaste no es un número o dejaste un espacio en blanco, ¡Reviselo por favor!")

#Función para mostrar el mensaje de que no hay espacios
def no_espacios():
    r = mb.showwarning("!!NO HAY ESPACIOS!!","Lo sentimos, en este momento no hay espacios, vuelva mas tarde")

#Función para mostrar un mensaje si la placa del vehículo ya se encuentra guardada
def placa_repe ():
    r = mb.showwarning("!!Placa repetida!!","La placa que ingresó ya se encuentra registrada, verifique que esté correcta porfavor")
    
#Función para verificar que los datos puestos en la configuración esten correctos
def verificar ():
    
    try:
        #La v en todas las variables de aquí en adelante significa verificar, el resto del nombre queda con el mismo significado
        v_espacios_c = int (textBoxEspacios.get())
        v_precio_hora = float (textBoxPrecio.get())
        v_pago_minimo = int (textBoxPago.get())
        v_redondeo = int (textBoxRedondeo.get())
        v_min_max = int (textBoxMinMax.get())
        v_mon_1 = int (textMoneda1.get())
        v_mon_2 = int (textMoneda2.get())
        v_mon_3 = int (textMoneda3.get())
        v_billete_1 = int (textBilletes1.get())
        v_billete_2 = int (textBilletes2.get()) 
        v_billete_3 = int (textBilletes3.get()) 
        v_billete_4 = int (textBilletes4.get()) 
        v_billete_5 = int (textBilletes5.get())
#Verificar todas las restricciones
        if v_espacios_c < 1:
            error ("Espacios en el parqueo")
            return False
        if v_precio_hora < 0:
            error ("Percio por hora")
            return False
        if v_pago_minimo < 0:
            error ("Pago minimo")
            return False
        if v_redondeo < 0 or v_redondeo > 60:
            error ("Redondear el cobro")
            return False
        if v_min_max < 0:
            error ("Minutos maximos")
            return False
        
        if v_mon_1 == 0:
            if v_mon_2 != 0:
                error ("Moneda 2")
                return False
            if v_mon_3 != 0:
                error ("Moneda 3")
                return False
        elif v_mon_2 == 0:
            if v_mon_3 != 0:
                error ("Moneda 3")
                return False
        elif v_mon_3 == 0:
            if v_mon_1 >= v_mon_2:
                error ("Moneda 1")
                error ("Moneda 2")
                return False
        elif v_mon_1 < 0:
            error ("Moneda 1")
            return False
        elif v_mon_1 >= v_mon_2:
            error ("Moneda 2")
            return False
        elif v_mon_2 >= v_mon_3:
            error ("Moneda 3")
            return False
        if v_billete_1 == 0:
            if v_billete_2 != 0:
                error ("Billete 2")
                return False
            elif v_billete_3 != 0:
                error   ("Billete 3")
                return False
            elif v_billete_4 != 0:
                error ("Billete 4")
                return False
            elif v_billete_5 != 0:
                error ("Billete 5")
                return False
        elif v_billete_2 == 0:
            if v_billete_1 < 0:
                error ("Billete 1")
                return False
            elif v_billete_3 != 0:
                error ("Billete 3")
                return False
            elif v_billete_4 != 0:
                error ("Billete 4")
                return False
            elif v_billete_5 != 0:
                error ("Billete 5")
                return False
        elif v_billete_3 == 0:
            if v_billete_1 < 0:
                error ("Billete 1")
                return False
            elif v_billete_1 >= v_billete_2:
                error ("Billete 2")
                return False
            elif v_billete_4 != 0:
                if v_billete_1 > v_billete_2:
                    error ("Billete 2")
                    error ("Billete 4")
                elif v_billete_2 > v_billete_3:
                    error ("Billete 3")
                    error ("Billete 4")
                else:
                    error ("Billete 4")
                return False
            elif v_billete_5 != 0:
                if v_billete_1 > v_billete_2:
                    error ("Billete 2")
                    error ("Billete 5")
                elif v_billete_2 > v_billete_3:
                    error ("Billete 3")
                    error ("Billete 5")
                elif v_billete_3 > v_billete_4:
                    error ("Billete 4")
                    error ("Billete 5")
                else:
                    error ("Billete 5")
                return False
        elif v_billete_4 == 0:
            if v_billete_1 < 0:
                error ("Billete 1")
                return False
            if v_billete_1 >= v_billete_2:
                error ("Billete 2")
                return False
            elif v_billete_2 >= v_billete_3:
                error ("Billete 3")
                return False
            elif v_billete_5 != 0:
                if v_billete_1 > v_billete_2:
                    error ("Billete 2")
                    error ("Billete 5")
                elif v_billete_2 > v_billete_3:
                    error ("Billete 3")
                    error ("Billete 5")
                elif v_billete_3 > v_billete_4:
                    error ("Billete 4")
                    error ("Billete 5")
                else:
                    error ("Billete 5")
                return False

        elif v_billete_5 == 0:
            if v_billete_1 < 0:
                error ("Billete 1")
                return False
            if v_billete_1 >= v_billete_2:
                error ("Billete 2")
                return False
            elif v_billete_2 >= v_billete_3:
                error ("Billete 3")
                return False
            elif v_billete_3 >= v_billete_4:
                error ("Billete 4")
                return False

        elif v_billete_1 < 0:
            error ("Billete 1")
            return False
        elif v_billete_1 >= v_billete_2:
            error ("Billete 2")
            return False
        elif v_billete_2 >= v_billete_3:
            error ("Billete 3")
            return False
        elif v_billete_3 >= v_billete_4:
            error ("Billete 4")
            return False
        elif v_billete_4 >= v_billete_5:
            error ("Billete 5")
            return False
        else:
           return True
        
    except:
        pass

#Función para remplazar los datos una ves ingresados en la configuración
def remplazar ():
    global espacios, espacios_c, precio_hora, pago_minimo, redondeo, min_max, mon_1, mon_2, mon_3, billete_1, billete_2, billete_3, billete_4, billete_5
    global c_mon_1, c_mon_2, c_mon_3 ,c_billete_1, c_billete_2, c_billete_3, c_billete_4, c_billete_5, s_mon_1, s_mon_2, s_mon_3, s_billete_1
    global s_billete_2, s_billete_3, s_billete_4, s_billete_5
    try:
        condicion =  verificar ()
        if condicion == False:
            pass
        else:
            espacios_c = int (textBoxEspacios.get())
            precio_hora = float (textBoxPrecio.get())
            pago_minimo = int (textBoxPago.get())
            redondeo = int (textBoxRedondeo.get())
            min_max = int (textBoxMinMax.get())
            mon_1 = int (textMoneda1.get())
            mon_2 = int (textMoneda2.get())
            mon_3 = int (textMoneda3.get())
            billete_1 = int (textBilletes1.get())
            billete_2 = int (textBilletes2.get()) 
            billete_3 = int (textBilletes3.get()) 
            billete_4 = int (textBilletes4.get()) 
            billete_5 = int (textBilletes5.get())
            s_mon_1 = str(mon_1)
            s_mon_2 = str(mon_2)
            s_mon_3 = str(mon_3)
            s_billete_1 = str(billete_1)
            s_billete_2 = str(billete_2)
            s_billete_3 = str(billete_3)
            s_billete_4 = str(billete_4)
            s_billete_5 = str(billete_5)
            
            espacio (espacios_c)
            habilitar ()
            cerrar_configuracion()
    except:
        error_2 ()

#Función para cargar la ventana de cargar cajero
def cargar ():
    global s_mon_1, s_mon_2, s_mon_3, s_billete_1
    global s_billete_2, s_billete_3, s_billete_4, s_billete_5

    labelMoneda_1.config(text = "Monedas de " + s_mon_1)
    labelMoneda_2.config(text = "Monedas de " + s_mon_2)
    labelMoneda_3.config(text = "Monedas de " + s_mon_3)
    labelBilletes_1.config(text = "Billetes de " + s_billete_1)
    labelBilletes_2.config(text = "Billetes de " + s_billete_2)
    labelBilletes_3.config(text = "Billetes de " + s_billete_3)
    labelBilletes_4.config(text = "Billetes de " + s_billete_4)
    labelBilletes_5.config(text = "Billetes de " + s_billete_5)
    calcular_total ()
    cargar_cajero.update()
    cargar_cajero.deiconify()
    p_principal.withdraw()

    

#Función para vereficar que los datos de entrada de cargar el cajero entén bien

def verificar_cargar ():

    global s_mon_1, s_mon_2, s_mon_3, s_billete_1, s_billete_2, s_billete_3, s_billete_4, s_billete_5

    try:
        v_c_mon_1 = int(textBoxCantidadMon1. get())
        v_c_mon_2 = int(textBoxCantidadMon2. get())
        v_c_mon_3 = int(textBoxCantidadMon3. get())
        v_c_billete_1 = int(textBoxCantidadBille1. get())
        v_c_billete_2 = int(textBoxCantidadBille2. get())
        v_c_billete_3 = int(textBoxCantidadBille3. get())
        v_c_billete_4 = int(textBoxCantidadBille4. get())
        v_c_billete_5 = int(textBoxCantidadBille5. get())

        if v_c_mon_1 < 0:
            error ("Moneda de " + s_mon_1)
            return False
        if v_c_mon_2 < 0:
            error ("Moneda de " + s_mon_2)
            return False
        if v_c_mon_3 < 0:
            error ("Moneda de " + s_mon_3)
            return False
        if v_c_billete_1 < 0:
            error ("Billete de " + s_billete_1)
            return False
        if v_c_billete_2 < 0:
            error ("Billete de " + s_billete_2)
            return False
        if v_c_billete_3 < 0:
            error ("Billete de " + s_billete_3)
            return False
        if v_c_billete_4 < 0:
            error ("Billete de " + s_billete_4)
            return False
        if v_c_billete_5 < 0:
            error ("Billete de " + s_billete_5)
            return False
        return True
    except:
        pass
    



#Función del boton de OK de cargar el cajero

def ok_cargar ():
    global c_mon_1, c_mon_2, c_mon_3 ,c_billete_1, c_billete_2, c_billete_3, c_billete_4, c_billete_5
    global mon_1, mon_2, mon_3, billete_1, billete_2, billete_3, billete_4, billete_5, salidas_mon_1, salidas_mon_2, salidas_mon_3
    global salidas_billete_1, salidas_billete_2, salidas_billete_3 ,salidas_billete_4 ,salidas_billete_5, total_mon_1, total_mon_1, total_mon_3
    global total_billete_1, total_billete_2, total_billete_3, total_billete_4, total_billete_5
    try:
        condicion = verificar_cargar ()
        if condicion == False:
            pass
        else:           
            
            revisar_saldo ()
            cerrar_cargar ()
            actualizar_cargar_cajero ()

    except:
        error_2()


#Función para actualizar la columna de Saldo (No actualiza ninguna variable solo muestra un suspuesto)
def revisar_saldo ():
    global c_mon_1, c_mon_2, c_mon_3 ,c_billete_1, c_billete_2, c_billete_3, c_billete_4, c_billete_5
    global mon_1, mon_2, mon_3, billete_1, billete_2, billete_3, billete_4, billete_5, total_mon_1, total_mon_2, total_mon_3
    global total_billete_1, total_billete_2, total_billete_3, total_billete_4, total_billete_5
    try:
        condicion = verificar_cargar ()
        if condicion == False:
            pass
        else:
            calcular_total ()
            
            labelMonedas1_SALDO .config (text = int(textBoxCantidadMon1. get()) + total_mon_1 )
            labelMonedas2_SALDO .config (text = int(textBoxCantidadMon2. get()) + total_mon_2 )
            labelMonedas3_SALDO .config (text = int(textBoxCantidadMon3. get()) + total_mon_3 )
            labelMonedas_Total_SALDO .config (text = int(textBoxCantidadMon1. get())  + total_mon_1  +
                                              int(textBoxCantidadMon2. get())  + total_mon_2 +
                                              int(textBoxCantidadMon3. get())  + total_mon_3 )
            
            labelBillete1_SALDO.config (text = int(textBoxCantidadBille1. get()) + total_billete_1)
            labelBillete2_SALDO.config (text = int(textBoxCantidadBille2. get()) + total_billete_2)
            labelBillete3_SALDO.config (text = int(textBoxCantidadBille3. get()) + total_billete_3)
            labelBillete4_SALDO.config (text = int(textBoxCantidadBille4. get()) + total_billete_4)
            labelBillete5_SALDO.config (text = int(textBoxCantidadBille5. get()) + total_billete_5)
            labelBillete_Total_SALDO.config (text = int(textBoxCantidadBille1. get()) + total_billete_1 +
                                             int(textBoxCantidadBille2. get()) + total_billete_2 +
                                             int(textBoxCantidadBille3. get()) + total_billete_3 +
                                             int(textBoxCantidadBille4. get()) + total_billete_4 +
                                             int(textBoxCantidadBille5. get()) + total_billete_5)
            
            labelMonedas1_SALDO_Total .config (text = int(textBoxCantidadMon1. get()) * mon_1 + total_mon_1 * mon_1)
            labelMonedas2_SALDO_Total .config (text = int(textBoxCantidadMon2. get()) * mon_2 + total_mon_2 * mon_2)
            labelMonedas3_SALDO_Total .config (text = int(textBoxCantidadMon3. get()) * mon_3 + total_mon_3 * mon_3)
            labelMonedas_Total_SALDO_Total .config (text = int(textBoxCantidadMon1. get()) * mon_1 + total_mon_1 * mon_1 +
                                                    int(textBoxCantidadMon2. get()) * mon_2 + total_mon_2 * mon_2 +
                                                    int(textBoxCantidadMon3. get()) * mon_3 + total_mon_3 * mon_3 )

            labelBillete1_SALDO_Total.config (text = int(textBoxCantidadBille1. get()) * billete_1 + total_billete_1 * billete_1)
            labelBillete2_SALDO_Total.config (text = int(textBoxCantidadBille2. get()) * billete_2 + total_billete_2 * billete_2)
            labelBillete3_SALDO_Total.config (text = int(textBoxCantidadBille3. get()) * billete_3 + total_billete_3 * billete_3)
            labelBillete4_SALDO_Total.config (text = int(textBoxCantidadBille4. get()) * billete_4 + total_billete_4 * billete_4)
            labelBillete5_SALDO_Total.config (text = int(textBoxCantidadBille5. get()) * billete_5 + total_billete_5 * billete_5)
            labelBillete_Total_SALDO_Total.config (text = int(textBoxCantidadBille1. get()) * billete_1 + total_billete_1 * billete_1 +
                                             int(textBoxCantidadBille2. get()) * billete_2 + total_billete_2 * billete_2 +
                                             int(textBoxCantidadBille3. get()) * billete_3 + total_billete_3 * billete_3 +
                                             int(textBoxCantidadBille4. get()) * billete_4 + total_billete_4 * billete_4 +
                                             int(textBoxCantidadBille5. get()) * billete_5 + total_billete_5 * billete_5)
            labelMonedas_Total_TextBox.config (text = int(textBoxCantidadMon1. get()) + int(textBoxCantidadMon2. get()) +
                                                int(textBoxCantidadMon3. get()))

            labelBillete_Total_TextBox.config (text = int(textBoxCantidadBille1. get())+int(textBoxCantidadBille2. get())
                                                + int(textBoxCantidadBille3. get()) + int(textBoxCantidadBille4. get()) +
                                                int(textBoxCantidadBille5. get()))

            labelMonedas_1_TOTAL_TexBox.config (text = mon_1 * int(textBoxCantidadMon1. get()))
            labelMonedas_2_TOTAL_TexBox.config (text = mon_2 * int(textBoxCantidadMon2. get()))
            labelMonedas_3_TOTAL_TexBox .config ( text = mon_3 * int(textBoxCantidadMon3. get()))
            labelMonedas_Total_TOTAL_TexBox .config ( text =  mon_1 * int(textBoxCantidadMon1. get()) +
                                                      mon_2 * int(textBoxCantidadMon2. get()) +
                                                      mon_3 * int(textBoxCantidadMon3. get()))

            labelBillete_1_TOTAL_TexBox .config (text = billete_1 * int(textBoxCantidadBille1. get()))
            labelBillete_2_TOTAL_TexBox .config ( text = billete_2 * int(textBoxCantidadBille2. get()))
            labelBillete_3_TOTAL_TexBox .config (text = billete_3 * int(textBoxCantidadBille3. get()))
            labelBillete_4_TOTAL_TexBox .config ( text = billete_4 * int(textBoxCantidadBille4. get()))
            labelBillete_5_TOTAL_TexBox .config ( text = billete_5 * int(textBoxCantidadBille5. get()))
            labelBillete_Total_TOTAL_TexBox .config (text = billete_5 * int(textBoxCantidadBille5. get()) +
                                                     billete_1 * int(textBoxCantidadBille1. get()) +
                                                     billete_2 * int(textBoxCantidadBille2. get()) +
                                                     billete_3 * int(textBoxCantidadBille3. get()) +
                                                     billete_4 * int(textBoxCantidadBille4. get()))
            
            labelTotal_del_Cajero.config (text = mon_1 * total_mon_1 + mon_2 * total_mon_2 + mon_3 * total_mon_3 
                                          + billete_5 * total_billete_5 + billete_1 * total_billete_1
                                          + billete_2 * total_billete_2 + billete_3 * total_billete_3
                                          + billete_4 * total_billete_4 )
    except:
        error_2()

#Función para actualizar los datos de la ventana Cargar cajero
def actualizar_cargar_cajero ():
            calcular_total ()
            global c_mon_1, c_mon_2, c_mon_3 ,c_billete_1, c_billete_2, c_billete_3, c_billete_4, c_billete_5
            global mon_1, mon_2, mon_3, billete_1, billete_2, billete_3, billete_4, billete_5, salidas_mon_1, salidas_mon_2, salidas_mon_3
            global salidas_billete_1, salidas_billete_2, salidas_billete_3 ,salidas_billete_4 ,salidas_billete_5, total_mon_1, total_mon_2, total_mon_3
            global total_billete_1, total_billete_2, total_billete_3, total_billete_4, total_billete_5
            c_mon_1 += int(textBoxCantidadMon1. get())
            c_mon_2 += int(textBoxCantidadMon2. get())
            c_mon_3 += int(textBoxCantidadMon3. get())
            
            c_billete_1 += int(textBoxCantidadBille1. get())
            c_billete_2 += int(textBoxCantidadBille2. get())
            c_billete_3 += int(textBoxCantidadBille3. get())
            c_billete_4 += int(textBoxCantidadBille4. get())
            c_billete_5 += int(textBoxCantidadBille5. get())

            calcular_total ()

            labelCMoneda_1.config (text = total_mon_1)
            labelCMoneda_2.config (text = total_mon_2)
            labelCMoneda_3.config (text = total_mon_3)
            labelCMonedaTotal.config(text = total_mon_1 + total_mon_2 +total_mon_3)
            
            labelCBillete_1.config (text = total_billete_1)
            labelCBillete_2.config (text = total_billete_2)
            labelCBillete_3.config (text = total_billete_3)            
            labelCBillete_4.config (text = total_billete_4)            
            labelCBillete_5.config (text = total_billete_5)
            labelCBilleteTotal.config (text = total_billete_1 + total_billete_2 + total_billete_3 +
                                       total_billete_4 + total_billete_5)


            labelMonedas_1_TOTAL.config (text = mon_1 * total_mon_1)
            labelMonedas_2_TOTAL.config (text = mon_2 * total_mon_2)
            labelMonedas_3_TOTAL.config (text = mon_3 * total_mon_3)
            labelMonedas_Total_TOTAL.config (text = mon_1 * total_mon_1 + mon_2 * total_mon_2 + mon_3 * total_mon_3)
            
            labelBillete_1_TOTAL.config (text = billete_1 * total_billete_1)
            labelBillete_2_TOTAL.config (text = billete_2 * total_billete_2)
            labelBillete_3_TOTAL.config (text = billete_3 * total_billete_3)
            labelBillete_4_TOTAL.config (text = billete_4 * total_billete_4)
            labelBillete_5_TOTAL.config (text = billete_5 * total_billete_5)
            labelBillete_Total_TOTAL.config (text = billete_5 * total_billete_5 + billete_1 * total_billete_1
                                             + billete_2 * total_billete_2 + billete_3 * total_billete_3
                                             + billete_4 * total_billete_4)

            labelTotal_del_Cajero.config (text = mon_1 * total_mon_1 + mon_2 * total_mon_2 + mon_3 * total_mon_3 
                                          + billete_5 * total_billete_5 + billete_1 * total_billete_1
                                          + billete_2 * total_billete_2 + billete_3 * total_billete_3
                                          + billete_4 * total_billete_4 )

            
    
#Función para actualizar los datos de la ventana saldo cajero
def actualizar_saldo_cajero ():
            calcular_total ()
            global c_mon_1, c_mon_2, c_mon_3 ,c_billete_1, c_billete_2, c_billete_3, c_billete_4, c_billete_5
            global mon_1, mon_2, mon_3, billete_1, billete_2, billete_3, billete_4, billete_5, salidas_mon_1, salidas_mon_2, salidas_mon_3
            global salidas_billete_1, salidas_billete_2, salidas_billete_3 ,salidas_billete_4 ,salidas_billete_5, total_mon_1, total_mon_2, total_mon_3
            global total_billete_1, total_billete_2, total_billete_3, total_billete_4, total_billete_5

            labelMoneda1_Entradas_Cantidad_s .config ( text = c_mon_1)
            labelMoneda2_Entradas_Cantidad_s .config ( text = c_mon_2)
            labelMoneda3_Entradas_Cantidad_s .config ( text = c_mon_3)
            labelMonedaTotal_Entradas_Cantidad_s .config ( text = c_mon_1 + c_mon_2 + c_mon_3)

            labelBillete1_Entradas_Cantidad_s .config ( text = c_billete_1)
            labelBillete2_Entradas_Cantidad_s .config ( text = c_billete_2)
            labelBillete3_Entradas_Cantidad_s .config ( text = c_billete_3)
            labelBillete4_Entradas_Cantidad_s .config ( text = c_billete_4)
            labelBillete5_Entradas_Cantidad_s .config ( text = c_billete_5)
            labelBilleteTotal_Entradas_Cantidad_s .config ( text = c_billete_1 + c_billete_2 + c_billete_3 + c_billete_4 + c_billete_5 )

            labelMoneda1_Entradas_Total_s .config ( text = mon_1 * c_mon_1)
            labelMoneda2_Entradas_Total_s .config ( text = mon_2 * c_mon_2)
            labelMoneda3_Entradas_Total_s .config ( text = mon_3 * c_mon_3)
            labelMonedaTotal_Entradas_Total_s .config ( text = mon_1 * c_mon_1 + mon_2 * c_mon_2 + mon_3 * c_mon_3)

            labelBillete1_Entradas_Total_s .config ( text = billete_1 * c_billete_1)
            labelBillete2_Entradas_Total_s .config ( text = billete_2 * c_billete_2)
            labelBillete3_Entradas_Total_s .config ( text = billete_3 * c_billete_3)
            labelBillete4_Entradas_Total_s .config ( text = billete_4 * c_billete_4)
            labelBillete5_Entradas_Total_s .config ( text = billete_5 * c_billete_5)
            labelBilleteTotal_Entradas_Total_s .config ( text = billete_1 * c_billete_1 + billete_2 * c_billete_2 +
                                                     billete_3 * c_billete_3 + billete_4 * c_billete_4 +
                                                     billete_5 * c_billete_5 )

            labelMonedas1_Salida_Cantidad_s .config ( text = salidas_mon_1 )
            labelMonedas2_Salida_Cantidad_s .config ( text = salidas_mon_2 )
            labelMonedas3_Salida_Cantidad_s .config ( text = salidas_mon_3 )
            labelMonedasTotal_Salida_Cantidad_s .config ( text = salidas_mon_1 + salidas_mon_2 +
                                                          salidas_mon_3 )

            labelBillete1_Salida_Cantidad_s .config ( text = salidas_billete_1 )
            labelBillete2_Salida_Cantidad_s .config ( text = salidas_billete_2 )
            labelBillete3_Salida_Cantidad_s .config ( text = salidas_billete_3 )
            labelBillete4_Salida_Cantidad_s .config ( text = salidas_billete_4 )
            labelBillete5_Salida_Cantidad_s .config ( text = salidas_billete_5 )
            labelBilleteTotal_Salida_Cantidad_s .config ( text = salidas_billete_1 + salidas_billete_2 +
                                                          salidas_billete_3 + billete_4 +
                                                          salidas_billete_5 )

            labelMonedas1_Salida_Total_s .config ( text = salidas_mon_1 * mon_1)
            labelMonedas2_Salida_Total_s .config ( text = salidas_mon_2 * mon_2)
            labelMonedas3_Salida_Total_s .config ( text = salidas_mon_3 * mon_3)
            labelMonedasTotal_Salida_Total_s .config ( text = salidas_mon_1 * mon_1 + salidas_mon_2 * mon_2 +
                                                          salidas_mon_3 * mon_3)

            labelBillete1_Salida_Total_s .config ( text = salidas_billete_1 * billete_1)
            labelBillete2_Salida_Total_s .config ( text = salidas_billete_2 * billete_2)
            labelBillete3_Salida_Total_s .config ( text = salidas_billete_3 * billete_3)
            labelBillete4_Salida_Total_s .config ( text = salidas_billete_4 * billete_4)
            labelBillete5_Salida_Total_s .config ( text = salidas_billete_5 * billete_5)
            labelBilleteTotal_Salida_Total_s.config ( text = salidas_billete_1 * billete_1 + salidas_billete_2 * billete_2 +
                                                          salidas_billete_3 * billete_3 + salidas_billete_4 * billete_4 +
                                                          salidas_billete_5 * billete_5)
            
            labelMonedas1_SALDO_Cantidad_s .config ( text = total_mon_1)
            labelMonedas2_SALDO_Cantidad_s .config ( text = total_mon_2)
            labelMonedas3_SALDO_Cantidad_s .config ( text = total_mon_3)
            labelMonedasTotal_SALDO_Cantidad_s .config ( text = total_mon_1 + total_mon_2 + total_mon_3)

            labelBillete1_SALDO_Cantidad_s .config ( text = total_billete_1)
            labelBillete2_SALDO_Cantidad_s .config ( text = total_billete_2)
            labelBillete3_SALDO_Cantidad_s .config ( text = total_billete_3)
            labelBillete4_SALDO_Cantidad_s .config ( text = total_billete_4)
            labelBillete5_SALDO_Cantidad_s .config ( text = total_billete_5)
            labelBilleteTotal_SALDO_Cantidad_s .config ( text = total_billete_1 + total_billete_2 +total_billete_3 +
                                                         total_billete_4 + total_billete_1)

            labelMonedas1_SALDO_Total_s .config ( text = total_mon_1 * mon_1)
            labelMonedas2_SALDO_Total_s .config ( text = total_mon_2 * mon_2)
            labelMonedas3_SALDO_Total_s .config ( text = total_mon_3 * mon_3)
            labelMonedasTotal_SALDO_Total_s .config ( text = total_mon_1 * mon_1 + total_mon_2 * mon_2 +
                                                      total_mon_3 * mon_3)
            
            labelBillete1_SALDO_Total_s .config ( text = total_billete_1 * billete_1)
            labelBillete2_SALDO_Total_s .config ( text = total_billete_2 * billete_2)
            labelBillete3_SALDO_Total_s .config ( text = total_billete_3 * billete_3)
            labelBillete4_SALDO_Total_s .config ( text = total_billete_4 * billete_4)
            labelBillete5_SALDO_Total_s .config ( text = total_billete_5 * billete_5)
            labelBilleteTotal_SALDO_Total_s .config ( text = total_billete_1 * billete_1 + total_billete_2 * billete_2 +
                                                      total_billete_3 * billete_3 + total_billete_4 * billete_4 +
                                                      total_billete_5 * billete_5)
    

#Función para calcular el total de billets y monedas de entradas (c_mon_# o c_billete_#) - las salidas
def calcular_total ():
    global c_mon_1, c_mon_2, c_mon_3 ,c_billete_1, c_billete_2, c_billete_3, c_billete_4, c_billete_5
    global salidas_mon_1, salidas_mon_2, salidas_mon_3
    global salidas_billete_1, salidas_billete_2, salidas_billete_3 ,salidas_billete_4 ,salidas_billete_5, total_mon_1, total_mon_2, total_mon_3
    global total_billete_1, total_billete_2, total_billete_3, total_billete_4, total_billete_5

    total_mon_1 = c_mon_1 - salidas_mon_1
    total_mon_2 = c_mon_2 - salidas_mon_2
    total_mon_3 = c_mon_3 - salidas_mon_3

    total_billete_1 = c_billete_1 - salidas_billete_1
    total_billete_2 = c_billete_2 - salidas_billete_2
    total_billete_3 = c_billete_3 - salidas_billete_3
    total_billete_4 = c_billete_4 - salidas_billete_4
    total_billete_5 = c_billete_5 - salidas_billete_5

#Función para cargar la ventana configuración
def configuracion ():
    
    menu_prg.update()
    menu_prg.deiconify()
    p_principal.withdraw()

#Función para cerrar configuración
def cerrar_configuracion ():
    p_principal.update()
    p_principal.deiconify()
    menu_prg.withdraw()

#Función para cerrar cargar cagero
def salir ():
    p_principal.withdraw()
    
#Funcion para cerrar la ventana de cargar el cajero
def cerrar_cargar ():
    p_principal.update()
    p_principal.deiconify()
    cargar_cajero.withdraw()

#Función para cargar la ventana del saldo del cajero
def saldo__cajero ():
    global s_mon_1, s_mon_2, s_mon_3, s_billete_1
    global s_billete_2, s_billete_3, s_billete_4, s_billete_5

    labelMoneda1_Denominacion_s. config (text = "Monedas de " + s_mon_1)  
    labelMoneda2_Denominacion_s. config (text = "Monedas de " + s_mon_2)  
    labelMoneda3_Denominacion_s. config (text = "Monedas de " + s_mon_3)

    labelBilletes1_Denominacion_s.config(text = "Billetes de " + s_billete_1)
    labelBilletes2_Denominacion_s.config(text = "Billetes de " + s_billete_2)
    labelBilletes3_Denominacion_s.config(text = "Billetes de " + s_billete_3)
    labelBilletes4_Denominacion_s.config(text = "Billetes de " + s_billete_4)
    labelBilletes5_Denominacion_s.config(text = "Billetes de " + s_billete_5)
    calcular_total ()
    actualizar_saldo_cajero ()
        
    saldo_cajero.update()
    saldo_cajero.deiconify()
    p_principal.withdraw()

#Función del botón OK de la ventana saldo del cajero
def ok_saldo_cajero ():
    global c_mon_1, c_mon_2, c_mon_3 ,c_billete_1, c_billete_2, c_billete_3, c_billete_4, c_billete_5
    global salidas_mon_1, salidas_mon_2, salidas_mon_3
    global salidas_billete_1, salidas_billete_2, salidas_billete_3 ,salidas_billete_4 ,salidas_billete_5, total_mon_1, total_mon_2, total_mon_3
    global total_billete_1, total_billete_2, total_billete_3, total_billete_4, total_billete_5
    print (VaciarCajero.get())
    if VaciarCajero.get() == 1:
        c_mon_1 = 0
        

    cerrar_saldo ()
        
#Función para sacar la hora actual
def hora_actual():
    hora = time.strftime("%H:%M") + "-" +  time.strftime("%d/%m/%y")
    return hora
    
#Función para cerrar la ventana de saldo del cajero
def cerrar_saldo ():
    p_principal.update()
    p_principal.deiconify()
    saldo_cajero.withdraw()

#Función para mostrar la ventana de ingresos de dinero
def abrir_ingresos ():
    ingreso_dinero.update()
    ingreso_dinero.deiconify()
    p_principal.withdraw()

#Función del botón ok de la ventana ingresos de dinero
def ok_ingreso_dinero ():
    p_principal.update()
    p_principal.deiconify()
    ingreso_dinero.withdraw()

#Función para mostras la ventana de ingreso de vehículo
def entrada_vehiculo():
    global espacios_c, precio_hora, pago_minimo, espacios_ocupados
    labelEspacios_disponibles .config ( text = "Espacios Disponibles      " + str(espacios_c - espacios_ocupados))

    mostrar_campo ()

    labelHora .config ( text = "Hora de entrada     " + hora_actual(),fg = "#66CCFF")

    labelPrecio_Hora .config ( text = "Precio por Hora     " + str(precio_hora),fg = "#66CCFF")

    labelCobroMinimo.config (text = "Cobro minimo de tiempo     " + str(pago_minimo))
                        
    ingreso_vehiculo.update()
    ingreso_vehiculo.deiconify()
    p_principal.withdraw()

#Función del botón asignar el campo en entrada de vehículo
def asignar_campo ():
    global espacios
    c = 0
    v = 0
    for x in espacios:
        if x == [] and v == 0:
            espacios[c] = [str(textBoxPlaca_Entrada.get()),hora_actual(),"",0]
            v = 1
        c += 1

#Función para verificar que el la placa del vehículo no se repita
def verificar_placa ():
    global espacios

    for x in espacios:
        for y in x:
            if y == str(textBoxPlaca_Entrada.get()):
                placa_repe ()
                return False
    return True
        
#Función para mostrar el que se asignaria en entrada de vehículo
def mostrar_campo ():
    global espacios
    if espacios_ocupados - espacios_c == 0:
        labelCampo.config (text = "No hay campos")
        buttonEntrada_vehículo.config(state = "disable")
        no_espacios()
        
    else:
        labelCampo.config (text = "Campo asignado    " + str(espacios.index([]) + 1))
        espacios.index([])
        buttonEntrada_vehículo.config(state = "normal")
        
#Función del botón OK de entrada de vehículo
def ok_entrada ():
    global espacios_ocupados
    if verificar_placa () != False:
        asignar_campo ()
        espacios_ocupados += 1
        p_principal.update()
        p_principal.deiconify()
        ingreso_vehiculo.withdraw()
            

    
#Función del botton cancelar en la ventan entrada de vehículo    
def cancelar_entrada ():
    p_principal.update()
    p_principal.deiconify()
    ingreso_vehiculo.withdraw()

#Función para cargar la ventana de salida de vehículo
def salida ():
    salida_vehiculo.update()
    salida_vehiculo.deiconify()
    p_principal.withdraw()

#Función del botón ok de la ventana de salida de vehículo
def ok_salida ():
    p_principal.update()
    p_principal.deiconify()
    salida_vehiculo.withdraw()

#Función para cargar la ventana acerca de
def acerca ():
    acercade.update()
    acercade.deiconify()
    p_principal.withdraw()

#Función para cerrar la ventana acerca de
def cerrar_acerca ():
    p_principal.update()
    p_principal.deiconify()
    acercade.withdraw()

#Función para abrir el manual de usuario
def abrir_manual ():
    webbrowser.open_new(r'file://D:\2019\Intro\Proyecto\Bryand_Brenes_manual_de_usuario_parqueo.pdf')

    

#Ventana principal
p_principal = tkinter.Tk()
p_principal.title("Ventana Principal")
p_principal.configure(bg = "#273746")
p_principal.geometry("{0}x{1}+0+0".format(p_principal.winfo_screenwidth(), p_principal.winfo_screenheight()))

#Ventanas secundarias

#Ventana de configuración
menu_prg = tkinter.Tk()
menu_prg.withdraw()
menu_prg.title("Configuración")
menu_prg.configure(bg = "#273746")
menu_prg.geometry("{0}x{1}+0+0".format(menu_prg.winfo_screenwidth(), menu_prg.winfo_screenheight()))


#Ventana de Cargar el cajero
cargar_cajero = tkinter.Tk()
cargar_cajero.withdraw()
cargar_cajero.title("Cargar Cajero")
cargar_cajero.configure(bg = "#273746")
cargar_cajero.geometry("{0}x{1}+0+0".format(menu_prg.winfo_screenwidth(), menu_prg.winfo_screenheight()))

#Ventana Saldo del Cajero

saldo_cajero = tkinter.Tk()
saldo_cajero.withdraw()
saldo_cajero.title("Saldo del Cajero")
saldo_cajero.configure(bg = "#273746")
saldo_cajero.geometry("{0}x{1}+0+0".format(menu_prg.winfo_screenwidth(), menu_prg.winfo_screenheight()))

#Ventana INGRESOS DE DINERO

ingreso_dinero = tkinter.Tk()
ingreso_dinero.withdraw()
ingreso_dinero.title("Ingreso de dinero")
ingreso_dinero.configure(bg = "#273746")
ingreso_dinero.geometry("{0}x{1}+0+0".format(menu_prg.winfo_screenwidth(), menu_prg.winfo_screenheight()))

#Ventana de ingresos de vehículos
ingreso_vehiculo = tkinter.Tk()
ingreso_vehiculo.withdraw()
ingreso_vehiculo.title("Entrada de vehículo")
ingreso_vehiculo.configure(bg = "#273746")
ingreso_vehiculo.geometry("{0}x{1}+0+0".format(menu_prg.winfo_screenwidth(), menu_prg.winfo_screenheight()))

#Venta de CAJERO DEL PARQUEO

cajero_parqueo = tkinter.Tk()
cajero_parqueo.withdraw()
cajero_parqueo.title("Cajero del Parqueo")
cajero_parqueo.configure(bg = "#273746")
cajero_parqueo.geometry("{0}x{1}+0+0".format(menu_prg.winfo_screenwidth(), menu_prg.winfo_screenheight()))

#Venta de Salida del vahículo

salida_vehiculo = tkinter.Tk()
salida_vehiculo.withdraw()
salida_vehiculo.title("Salida de vehículo")
salida_vehiculo.configure(bg = "#273746")
salida_vehiculo.geometry("{0}x{1}+0+0".format(menu_prg.winfo_screenwidth(), menu_prg.winfo_screenheight()))

#Ventana Acerca de

acercade = tkinter.Tk()
acercade.withdraw()
acercade.title("Acerca de")
acercade.configure(bg = "#273746")
acercade.geometry("{0}x{1}+0+0".format(menu_prg.winfo_screenwidth(), menu_prg.winfo_screenheight()))




#Label
#Ventana Principal
labelPRINCIPAL = Label(p_principal, text= "PARQUEO", fg = "#66CCFF", font = ("Cooper Black", 50))
labelPRINCIPAL.place(x=525, y= 260)
labelPRINCIPAL.configure(bg = "#273746")


#Configuración
labelEspacios = Label(menu_prg, text= "Cantidad de espacios en el parqueo ", fg = "#66CCFF", font = ("Serif", 14))
labelEspacios.place(x=15, y= 20)
labelEspacios.configure(bg = "#273746")

labelPrecio = Label(menu_prg, text= "Precio por hora", fg = "#66CCFF", font = ("Serif", 14))
labelPrecio.place(x=15, y= 60)
labelPrecio.configure(bg = "#273746")

labelPago = Label(menu_prg, text= "Pago mínimo ", fg = "#66CCFF", font = ("Serif", 14))
labelPago.place(x=15, y= 100)
labelPago.configure(bg = "#273746")


labelRedondeo = Label(menu_prg, text = "Redondear el cobro a los siguientes minutos", fg = "#66CCFF", font = ("Serif", 14))
labelRedondeo.place(x=15, y= 180)
labelRedondeo.configure(bg = "#273746")

labelMinMax = Label (menu_prg, text = "Minutos máximos para salir después del pago", fg = "#66CCFF", font = ("Serif", 14))
labelMinMax.place (x=15, y= 220)
labelMinMax.configure(bg = "#273746")

labelMoneda = Label (menu_prg, text = "TIPOS DE MONEDA", fg = "#66CCFF", font = ("Serif", 14))
labelMoneda .place (x=15, y= 260)
labelMoneda .configure(bg = "#273746")

labelMoneda1 = Label (menu_prg, text = "Moneda 1, la de menor denominación ", fg = "#66CCFF", font = ("Serif", 14))
labelMoneda1 .place (x=15, y= 300)
labelMoneda1 .configure(bg = "#273746")

labelMoneda2 = Label (menu_prg, text = "Moneda 2, denominación siguiente a la anterior ", fg = "#66CCFF", font = ("Serif", 14))
labelMoneda2 .place (x=15, y= 340)
labelMoneda2 .configure(bg = "#273746")

labelMoneda3 = Label (menu_prg, text = "Moneda 3, denominación siguiente a la anterior ", fg = "#66CCFF", font = ("Serif", 14))
labelMoneda3 .place (x=15, y= 380)
labelMoneda3 .configure(bg = "#273746")

labelBilletes = Label (menu_prg, text = "TIPOS DE BILLETES", fg = "#66CCFF", font = ("Serif", 14))
labelBilletes .place (x=15, y= 420)
labelBilletes .configure(bg = "#273746")

labelBilletes1 = Label (menu_prg, text = "Billete 1, el de menor denominación ", fg = "#66CCFF", font = ("Serif", 14))
labelBilletes1 .place (x=15, y= 460)
labelBilletes1 .configure(bg = "#273746")

labelBilletes2 = Label (menu_prg, text = "Billete 2, denominación siguiente a la anterior ", fg = "#66CCFF", font = ("Serif", 14))
labelBilletes2 .place (x=15, y= 500)
labelBilletes2 .configure(bg = "#273746")

labelBilletes3 = Label (menu_prg, text = "Billete 3, denominación siguiente a la anterior ", fg = "#66CCFF", font = ("Serif", 14))
labelBilletes3 .place (x=15, y= 540)
labelBilletes3 .configure(bg = "#273746")

labelBilletes4 = Label (menu_prg, text = "Billete 4, denominación siguiente a la anterior ", fg = "#66CCFF", font = ("Serif", 14))
labelBilletes4 .place (x=15, y= 580)
labelBilletes4 .configure(bg = "#273746")

labelBilletes5 = Label (menu_prg, text = "Billete 5, denominación siguiente a la anterior ", fg = "#66CCFF", font = ("Serif", 14))
labelBilletes5 .place (x=15, y= 620)
labelBilletes5 .configure(bg = "#273746")

#Cargar cajero

labelDenomiacion = Label (cargar_cajero, text = "DENOMINACIÓN", fg = "#66CCFF", font = ("Serif", 12))
labelDenomiacion .place (x=15, y= 50)
labelDenomiacion .configure(bg = "#273746")

labelCantidad = Label (cargar_cajero, text = "CANTIDAD", fg = "#66CCFF", font = ("Serif", 12))
labelCantidad .place (x=200, y= 50)
labelCantidad .configure(bg = "#273746")

labelCantidadTextBox = Label (cargar_cajero, text = "CANTIDAD", fg = "#66CCFF", font = ("Serif", 12))
labelCantidadTextBox .place (x=450, y= 50)
labelCantidadTextBox .configure(bg = "#273746")

labelCantidad = Label (cargar_cajero, text = "TOTAL", fg = "#66CCFF", font = ("Serif", 12))
labelCantidad .place (x=325, y= 50)
labelCantidad .configure(bg = "#273746")

labelCantidad_TextBox = Label (cargar_cajero, text = "TOTAL", fg = "#66CCFF", font = ("Serif", 12))
labelCantidad_TextBox .place (x=625, y= 50)
labelCantidad_TextBox .configure(bg = "#273746")

labelEntradas = Label (cargar_cajero, text = "SALDO ANTES DE LA CARGA", fg = "#66CCFF", font = ("Serif", 12))
labelEntradas .place (x=175, y= 20)
labelEntradas .configure(bg = "#273746")

labelSaldo_Actual = Label (cargar_cajero, text = "CARGA", fg = "#66CCFF", font = ("Serif", 12))
labelSaldo_Actual .place (x=550, y= 20)
labelSaldo_Actual .configure(bg = "#273746")

labelC_TextBox = Label (cargar_cajero, text = "SALDO", fg = "#66CCFF", font = ("Serif", 12))
labelC_TextBox .place (x=850, y= 20)
labelC_TextBox .configure(bg = "#273746")

label_Cantidad_Saldo= Label (cargar_cajero, text = "CANTIDAD", fg = "#66CCFF", font = ("Serif", 12))
label_Cantidad_Saldo .place (x=800, y= 50)
label_Cantidad_Saldo .configure(bg = "#273746")

label_Total_Saldo= Label (cargar_cajero, text = "TOTAL", fg = "#66CCFF", font = ("Serif", 12))
label_Total_Saldo .place (x=925, y= 50)
label_Total_Saldo .configure(bg = "#273746")

labelMoneda_1 = Label (cargar_cajero, text = "Monedas de " + s_mon_1, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda_1 .place (x=15, y= 110)
labelMoneda_1 .configure(bg = "#273746")

labelMoneda_2 = Label (cargar_cajero, text = "Monedas de " + s_mon_2, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda_2 .place (x=15, y= 140)
labelMoneda_2 .configure(bg = "#273746")

labelMoneda_3 = Label (cargar_cajero, text = "Monedas de " + s_mon_3, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda_3 .place (x=15, y= 170)
labelMoneda_3 .configure(bg = "#273746")

labelMonedasTOTAL = Label (cargar_cajero, text = "TOTAL DE MONEDAS", fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTOTAL .place (x=15, y= 200)
labelMonedasTOTAL .configure(bg = "#273746")

labelBilletes_1 = Label (cargar_cajero, text = "Billetes de " + s_billete_1, fg = "#66CCFF", font = ("Serif", 12))
labelBilletes_1 .place (x=15, y= 250)
labelBilletes_1 .configure(bg = "#273746")

labelBilletes_2 = Label (cargar_cajero, text = "Billetes de " + s_billete_2, fg = "#66CCFF", font = ("Serif", 12))
labelBilletes_2 .place (x=15, y= 280)
labelBilletes_2 .configure(bg = "#273746")

labelBilletes_3 = Label (cargar_cajero, text = "Billetes de " + s_billete_3, fg = "#66CCFF", font = ("Serif", 12))
labelBilletes_3 .place (x=15, y= 310)
labelBilletes_3 .configure(bg = "#273746")

labelBilletes_4 = Label (cargar_cajero, text = "Billetes de " + s_billete_4, fg = "#66CCFF", font = ("Serif", 12))
labelBilletes_4 .place (x=15, y= 340)
labelBilletes_4 .configure(bg = "#273746")

labelBilletes_5 = Label (cargar_cajero, text = "Billetes de " + s_billete_5, fg = "#66CCFF", font = ("Serif", 12))
labelBilletes_5 .place (x=15, y= 370)
labelBilletes_5 .configure(bg = "#273746")

labelBilletesTOTAL = Label (cargar_cajero, text = "TOTAL DE BILLETES", fg = "#66CCFF", font = ("Serif", 12))
labelBilletesTOTAL .place (x=15, y= 400)
labelBilletesTOTAL .configure(bg = "#273746")

labelTotal_Cajero = Label (cargar_cajero, text = "TOTAL DEL CAJERO", fg = "#66CCFF", font = ("Serif", 12))
labelTotal_Cajero .place (x=15, y= 460)
labelTotal_Cajero .configure(bg = "#273746")

labelCMoneda_1= Label (cargar_cajero, text = c_mon_1, fg = "#66CCFF", font = ("Serif", 12))
labelCMoneda_1 .place (x=200, y= 110)
labelCMoneda_1 .configure(bg = "#273746")

labelCMoneda_2= Label (cargar_cajero, text = c_mon_2, fg = "#66CCFF", font = ("Serif", 12))
labelCMoneda_2 .place (x=200, y= 140)
labelCMoneda_2 .configure(bg = "#273746")

labelCMoneda_3= Label (cargar_cajero, text = c_mon_3, fg = "#66CCFF", font = ("Serif", 12))
labelCMoneda_3 .place (x=200, y= 170)
labelCMoneda_3 .configure(bg = "#273746")

labelCMonedaTotal= Label (cargar_cajero, text = c_mon_1 + c_mon_2 +c_mon_3, fg = "#66CCFF", font = ("Serif", 12))
labelCMonedaTotal .place (x=200, y= 200)
labelCMonedaTotal .configure(bg = "#273746")

labelCBillete_1= Label (cargar_cajero, text = c_billete_1, fg = "#66CCFF", font = ("Serif", 12))
labelCBillete_1 .place (x=200, y= 250)
labelCBillete_1 .configure(bg = "#273746")

labelCBillete_2= Label (cargar_cajero, text = c_billete_2, fg = "#66CCFF", font = ("Serif", 12))
labelCBillete_2 .place (x=200, y= 280)
labelCBillete_2 .configure(bg = "#273746")

labelCBillete_3= Label (cargar_cajero, text = c_billete_3, fg = "#66CCFF", font = ("Serif", 12))
labelCBillete_3 .place (x=200, y= 310)
labelCBillete_3 .configure(bg = "#273746")

labelCBillete_4= Label (cargar_cajero, text = c_billete_4, fg = "#66CCFF", font = ("Serif", 12))
labelCBillete_4 .place (x=200, y= 340)
labelCBillete_4 .configure(bg = "#273746")

labelCBillete_5= Label (cargar_cajero, text = c_billete_5, fg = "#66CCFF", font = ("Serif", 12))
labelCBillete_5 .place (x=200, y= 370)
labelCBillete_5 .configure(bg = "#273746")

labelCBilleteTotal= Label (cargar_cajero, text = c_billete_1 + c_billete_2 + c_billete_3 + c_billete_4 + c_billete_5 , fg = "#66CCFF", font = ("Serif", 12))
labelCBilleteTotal .place (x=200, y= 400)
labelCBilleteTotal .configure(bg = "#273746")

labelMonedas_1_TOTAL = Label (cargar_cajero, text = mon_1 * c_mon_1, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_1_TOTAL .place (x=325, y= 110)
labelMonedas_1_TOTAL .configure(bg = "#273746")

labelMonedas_2_TOTAL = Label (cargar_cajero, text = mon_2 * c_mon_2, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_2_TOTAL .place (x=325, y= 140)
labelMonedas_2_TOTAL .configure(bg = "#273746")

labelMonedas_3_TOTAL = Label (cargar_cajero, text = mon_3 * c_mon_3, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_3_TOTAL .place (x=325, y= 170)
labelMonedas_3_TOTAL .configure(bg = "#273746")

labelMonedas_Total_TOTAL = Label (cargar_cajero, text = mon_1 * c_mon_1 + mon_2 * c_mon_2 + mon_3 * c_mon_3, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_Total_TOTAL .place (x=325, y= 200)
labelMonedas_Total_TOTAL .configure(bg = "#273746")

labelBillete_1_TOTAL = Label (cargar_cajero, text = billete_1 * c_billete_1, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_1_TOTAL .place (x=325, y= 250)
labelBillete_1_TOTAL .configure(bg = "#273746")

labelBillete_2_TOTAL = Label (cargar_cajero, text = billete_2 * c_billete_2, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_2_TOTAL .place (x=325, y= 280)
labelBillete_2_TOTAL .configure(bg = "#273746")

labelBillete_3_TOTAL = Label (cargar_cajero, text = billete_3 * c_billete_3, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_3_TOTAL .place (x=325, y= 310)
labelBillete_3_TOTAL .configure(bg = "#273746")

labelBillete_4_TOTAL = Label (cargar_cajero, text = billete_4 * c_billete_4, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_4_TOTAL .place (x=325, y= 340)
labelBillete_4_TOTAL .configure(bg = "#273746")

labelBillete_5_TOTAL = Label (cargar_cajero, text = billete_5 * c_billete_5, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_5_TOTAL .place (x=325, y= 370)
labelBillete_5_TOTAL .configure(bg = "#273746")

labelBillete_Total_TOTAL = Label (cargar_cajero, text = billete_5 * c_billete_5 + billete_1 * c_billete_1 + billete_2 * c_billete_2 +
                                  billete_3 * c_billete_3 + billete_4 * c_billete_4, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_Total_TOTAL .place (x=325, y= 400)
labelBillete_Total_TOTAL .configure(bg = "#273746")

labelMonedas_Total_TextBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_Total_TextBox .place (x=450, y= 200)
labelMonedas_Total_TextBox .configure(bg = "#273746")

labelBillete_Total_TextBox= Label (cargar_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete_Total_TextBox .place (x=450, y= 400)
labelBillete_Total_TextBox .configure(bg = "#273746")

labelMonedas_1_TOTAL_TexBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_1_TOTAL_TexBox .place (x=625, y= 110)
labelMonedas_1_TOTAL_TexBox .configure(bg = "#273746")

labelMonedas_2_TOTAL_TexBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_2_TOTAL_TexBox .place (x=625, y= 140)
labelMonedas_2_TOTAL_TexBox .configure(bg = "#273746")

labelMonedas_3_TOTAL_TexBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_3_TOTAL_TexBox .place (x=625, y= 170)
labelMonedas_3_TOTAL_TexBox .configure(bg = "#273746")

labelMonedas_Total_TOTAL_TexBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_Total_TOTAL_TexBox .place (x=625, y= 200)
labelMonedas_Total_TOTAL_TexBox .configure(bg = "#273746")

labelBillete_1_TOTAL_TexBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_1_TOTAL_TexBox .place (x=625, y= 250)
labelBillete_1_TOTAL_TexBox .configure(bg = "#273746")

labelBillete_2_TOTAL_TexBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_2_TOTAL_TexBox .place (x=625, y= 280)
labelBillete_2_TOTAL_TexBox .configure(bg = "#273746")

labelBillete_3_TOTAL_TexBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_3_TOTAL_TexBox .place (x=625, y= 310)
labelBillete_3_TOTAL_TexBox .configure(bg = "#273746")

labelBillete_4_TOTAL_TexBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_4_TOTAL_TexBox .place (x=625, y= 340)
labelBillete_4_TOTAL_TexBox .configure(bg = "#273746")

labelBillete_5_TOTAL_TexBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_5_TOTAL_TexBox .place (x=625, y= 370)
labelBillete_5_TOTAL_TexBox.configure(bg = "#273746")

labelBillete_Total_TOTAL_TexBox = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_Total_TOTAL_TexBox .place (x=625, y= 400)
labelBillete_Total_TOTAL_TexBox .configure(bg = "#273746")

labelMonedas1_SALDO = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12)) 
labelMonedas1_SALDO .place (x=800, y= 110)
labelMonedas1_SALDO .configure(bg = "#273746")

labelMonedas2_SALDO = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas2_SALDO .place (x=800, y= 140)
labelMonedas2_SALDO .configure(bg = "#273746")

labelMonedas3_SALDO = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas3_SALDO .place (x=800, y= 170)
labelMonedas3_SALDO .configure(bg = "#273746")

labelMonedas_Total_SALDO = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_Total_SALDO .place (x=800, y= 200)
labelMonedas_Total_SALDO .configure(bg = "#273746")

labelBillete1_SALDO= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_SALDO .place (x=800, y= 250)
labelBillete1_SALDO .configure(bg = "#273746")

labelBillete2_SALDO= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_SALDO .place (x=800, y= 280)
labelBillete2_SALDO .configure(bg = "#273746")

labelBillete3_SALDO= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_SALDO .place (x=800, y= 310)
labelBillete3_SALDO .configure(bg = "#273746")

labelBillete4_SALDO= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_SALDO .place (x=800, y= 340)
labelBillete4_SALDO .configure(bg = "#273746")

labelBillete5_SALDO= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_SALDO .place (x=800, y= 370)
labelBillete5_SALDO .configure(bg = "#273746")

labelBillete_Total_SALDO= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_Total_SALDO .place (x=800, y= 400)
labelBillete_Total_SALDO .configure(bg = "#273746")

labelMonedas1_SALDO_Total = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas1_SALDO_Total .place (x=925, y= 110)
labelMonedas1_SALDO_Total .configure(bg = "#273746")

labelMonedas2_SALDO_Total = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas2_SALDO_Total .place (x=925, y= 140)
labelMonedas2_SALDO_Total .configure(bg = "#273746")

labelMonedas3_SALDO_Total = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas3_SALDO_Total .place (x=925, y= 170)
labelMonedas3_SALDO_Total .configure(bg = "#273746")

labelMonedas_Total_SALDO_Total = Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas_Total_SALDO_Total .place (x=925, y= 200)
labelMonedas_Total_SALDO_Total .configure(bg = "#273746")

labelBillete1_SALDO_Total= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_SALDO_Total .place (x=925, y= 250)
labelBillete1_SALDO_Total .configure(bg = "#273746")

labelBillete2_SALDO_Total= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_SALDO_Total .place (x=925, y= 280)
labelBillete2_SALDO_Total .configure(bg = "#273746")

labelBillete3_SALDO_Total= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_SALDO_Total .place (x=925, y= 310)
labelBillete3_SALDO_Total .configure(bg = "#273746")

labelBillete4_SALDO_Total= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_SALDO_Total .place (x=925, y= 340)
labelBillete4_SALDO_Total .configure(bg = "#273746")

labelBillete5_SALDO_Total= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_SALDO_Total .place (x=925, y= 370)
labelBillete5_SALDO_Total .configure(bg = "#273746")

labelBillete_Total_SALDO_Total= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete_Total_SALDO_Total .place (x=925, y= 400)
labelBillete_Total_SALDO_Total .configure(bg = "#273746")

labelTotal_del_Cajero= Label (cargar_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelTotal_del_Cajero .place (x=925, y= 460)
labelTotal_del_Cajero .configure(bg = "#273746")



#Saldo_cajero
#Los nombres vienen de la siguiente forma, moneda#/billete#_Columna-Principal_Calumna-Secundaria
#En caso de los casos que se quiere presentar un total en lugar del número (#) viene "Total" 
#En los nombres donde no viene ninguna barra baja ( _ ) es porque no está bajo una conlumna principal
#O es el label donde se crea la colunma principal
#En caso donde solo tiene una barra baja es donde se crean las columnas secundarias
#La s al final reprenseta la saldo, es para no confundir con los nombre de la ventana cargar cajero
#Los nombre de la ventana cargar no siguieron este formato por falta de tiempo para cambialo
#Se puso la s de todas formas pues se tenia planeado cambiarlo en algún momento

labelDenomiacion_s = Label (saldo_cajero, text = "DENOMINACIÓN", fg = "#66CCFF", font = ("Serif", 12))
labelDenomiacion_s .place (x=15, y= 50)
labelDenomiacion_s .configure(bg = "#273746")


#Entradas = Saldo Antes De la Carga

labelEntradas_s = Label (saldo_cajero, text = "Entradas", fg = "#66CCFF", font = ("Serif", 12))
labelEntradas_s .place (x=175, y= 20)
labelEntradas_s .configure(bg = "#273746")

labelCantidad_Entradas_s = Label (saldo_cajero, text = "CANTIDAD", fg = "#66CCFF", font = ("Serif", 12))
labelCantidad_Entradas_s .place (x=200, y= 50)
labelCantidad_Entradas_s .configure(bg = "#273746")

labelTotal_Entradas_s = Label (saldo_cajero, text = "TOTAL", fg = "#66CCFF", font = ("Serif", 12))
labelTotal_Entradas_s .place (x=325, y= 50)
labelTotal_Entradas_s .configure(bg = "#273746")

labelSalida_s = Label (saldo_cajero, text = "SALIDA", fg = "#66CCFF", font = ("Serif", 12))
labelSalida_s .place (x=550, y= 20)
labelSalida_s .configure(bg = "#273746")

labelCargar_Salida_s = Label (saldo_cajero, text = "CANTIDAD", fg = "#66CCFF", font = ("Serif", 12))
labelCargar_Salida_s .place (x=450, y= 50)
labelCargar_Salida_s .configure(bg = "#273746")

labelTotal_Salida_s = Label (saldo_cajero, text = "TOTAL", fg = "#66CCFF", font = ("Serif", 12))
labelTotal_Salida_s .place (x=625, y= 50)
labelTotal_Salida_s .configure(bg = "#273746")

labelSaldo_s = Label (saldo_cajero, text = "SALDO", fg = "#66CCFF", font = ("Serif", 12))
labelSaldo_s .place (x=850, y= 20)
labelSaldo_s .configure(bg = "#273746")

labelCantidad_Saldo_s = Label (saldo_cajero, text = "CANTIDAD", fg = "#66CCFF", font = ("Serif", 12))
labelCantidad_Saldo_s .place (x=800, y= 50)
labelCantidad_Saldo_s .configure(bg = "#273746")

labelTotal_Saldo_s = Label (saldo_cajero, text = "TOTAL", fg = "#66CCFF", font = ("Serif", 12))
labelTotal_Saldo_s .place (x=925, y= 50)
labelTotal_Saldo_s .configure(bg = "#273746")

labelMoneda1_Denominacion_s = Label (saldo_cajero, text = "Monedas de 0", fg = "#66CCFF", font = ("Serif", 12))
labelMoneda1_Denominacion_s .place (x=15, y= 110)
labelMoneda1_Denominacion_s .configure(bg = "#273746")

labelMoneda2_Denominacion_s = Label (saldo_cajero, text = "Monedas de 0" , fg = "#66CCFF", font = ("Serif", 12))
labelMoneda2_Denominacion_s .place (x=15, y= 140)
labelMoneda2_Denominacion_s .configure(bg = "#273746")

labelMoneda3_Denominacion_s = Label (saldo_cajero, text = "Monedas de  0" , fg = "#66CCFF", font = ("Serif", 12))
labelMoneda3_Denominacion_s .place (x=15, y= 170)
labelMoneda3_Denominacion_s .configure(bg = "#273746")

labelMonedasTOTAL_Denominacion_s = Label (saldo_cajero, text = "TOTAL DE MONEDAS", fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTOTAL_Denominacion_s .place (x=15, y= 200)
labelMonedasTOTAL_Denominacion_s .configure(bg = "#273746")

labelBilletes1_Denominacion_s = Label (saldo_cajero, text = "Billetes de 0", fg = "#66CCFF", font = ("Serif", 12))
labelBilletes1_Denominacion_s .place (x=15, y= 250)
labelBilletes1_Denominacion_s .configure(bg = "#273746")

labelBilletes2_Denominacion_s = Label (saldo_cajero, text = "Billetes de 0" , fg = "#66CCFF", font = ("Serif", 12))
labelBilletes2_Denominacion_s .place (x=15, y= 280)
labelBilletes2_Denominacion_s .configure(bg = "#273746")

labelBilletes3_Denominacion_s = Label (saldo_cajero, text = "Billetes de 0" , fg = "#66CCFF", font = ("Serif", 12))
labelBilletes3_Denominacion_s .place (x=15, y= 310)
labelBilletes3_Denominacion_s .configure(bg = "#273746")

labelBilletes4_Denominacion_s = Label (saldo_cajero, text = "Billetes de 0", fg = "#66CCFF", font = ("Serif", 12))
labelBilletes4_Denominacion_s .place (x=15, y= 340)
labelBilletes4_Denominacion_s .configure(bg = "#273746")

labelBilletes5_Denominacion_s = Label (saldo_cajero, text = "Billetes de 0 ", fg = "#66CCFF", font = ("Serif", 12))
labelBilletes5_Denominacion_s .place (x=15, y= 370)
labelBilletes5_Denominacion_s .configure(bg = "#273746")

labelBilletesTOTAL_Denominacion_s = Label (saldo_cajero, text = "TOTAL DE BILLETES", fg = "#66CCFF", font = ("Serif", 12))
labelBilletesTOTAL_Denominacion_s .place (x=15, y= 400)
labelBilletesTOTAL_Denominacion_s .configure(bg = "#273746")

labelMoneda1_Entradas_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda1_Entradas_Cantidad_s .place (x=200, y= 110)
labelMoneda1_Entradas_Cantidad_s .configure(bg = "#273746")

labelMoneda2_Entradas_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda2_Entradas_Cantidad_s .place (x=200, y= 140)
labelMoneda2_Entradas_Cantidad_s .configure(bg = "#273746")

labelMoneda3_Entradas_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda3_Entradas_Cantidad_s .place (x=200, y= 170)
labelMoneda3_Entradas_Cantidad_s .configure(bg = "#273746")

labelMonedaTotal_Entradas_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedaTotal_Entradas_Cantidad_s .place (x=200, y= 200)
labelMonedaTotal_Entradas_Cantidad_s .configure(bg = "#273746")

labelBillete1_Entradas_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_Entradas_Cantidad_s .place (x=200, y= 250)
labelBillete1_Entradas_Cantidad_s .configure(bg = "#273746")

labelBillete2_Entradas_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_Entradas_Cantidad_s .place (x=200, y= 280)
labelBillete2_Entradas_Cantidad_s .configure(bg = "#273746")

labelBillete3_Entradas_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_Entradas_Cantidad_s .place (x=200, y= 310)
labelBillete3_Entradas_Cantidad_s .configure(bg = "#273746")

labelBillete4_Entradas_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_Entradas_Cantidad_s .place (x=200, y= 340)
labelBillete4_Entradas_Cantidad_s .configure(bg = "#273746")

labelBillete5_Entradas_Cantidad_s = Label (saldo_cajero, text =0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_Entradas_Cantidad_s .place (x=200, y= 370)
labelBillete5_Entradas_Cantidad_s .configure(bg = "#273746")

labelBilleteTotal_Entradas_Cantidad_s = Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_Entradas_Cantidad_s .place (x=200, y= 400)
labelBilleteTotal_Entradas_Cantidad_s .configure(bg = "#273746")

labelMoneda1_Entradas_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda1_Entradas_Total_s .place (x=325, y= 110)
labelMoneda1_Entradas_Total_s .configure(bg = "#273746")

labelMoneda2_Entradas_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda2_Entradas_Total_s .place (x=325, y= 140)
labelMoneda2_Entradas_Total_s .configure(bg = "#273746")

labelMoneda3_Entradas_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda3_Entradas_Total_s .place (x=325, y= 170)
labelMoneda3_Entradas_Total_s .configure(bg = "#273746")

labelMonedaTotal_Entradas_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedaTotal_Entradas_Total_s .place (x=325, y= 200)
labelMonedaTotal_Entradas_Total_s .configure(bg = "#273746")

labelBillete1_Entradas_Total_s = Label (saldo_cajero, text =0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_Entradas_Total_s .place (x=325, y= 250)
labelBillete1_Entradas_Total_s .configure(bg = "#273746")

labelBillete2_Entradas_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_Entradas_Total_s .place (x=325, y= 280)
labelBillete2_Entradas_Total_s .configure(bg = "#273746")

labelBillete3_Entradas_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_Entradas_Total_s .place (x=325, y= 310)
labelBillete3_Entradas_Total_s .configure(bg = "#273746")

labelBillete4_Entradas_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_Entradas_Total_s .place (x=325, y= 340)
labelBillete4_Entradas_Total_s .configure(bg = "#273746")

labelBillete5_Entradas_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_Entradas_Total_s .place (x=325, y= 370)
labelBillete5_Entradas_Total_s .configure(bg = "#273746")

labelBilleteTotal_Entradas_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_Entradas_Total_s .place (x=325, y= 400)
labelBilleteTotal_Entradas_Total_s .configure(bg = "#273746")

labelMonedas1_Salida_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas1_Salida_Cantidad_s .place (x=450, y= 110)
labelMonedas1_Salida_Cantidad_s .configure(bg = "#273746")

labelMonedas2_Salida_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas2_Salida_Cantidad_s .place (x=450, y= 140)
labelMonedas2_Salida_Cantidad_s .configure(bg = "#273746")

labelMonedas3_Salida_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas3_Salida_Cantidad_s .place (x=450, y= 170)
labelMonedas3_Salida_Cantidad_s .configure(bg = "#273746")

labelMonedasTotal_Salida_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTotal_Salida_Cantidad_s .place (x=450, y= 200)
labelMonedasTotal_Salida_Cantidad_s .configure(bg = "#273746")

labelBillete1_Salida_Cantidad_s = Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_Salida_Cantidad_s .place (x=450, y= 250)
labelBillete1_Salida_Cantidad_s .configure(bg = "#273746")

labelBillete2_Salida_Cantidad_s = Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_Salida_Cantidad_s .place (x=450, y= 280)
labelBillete2_Salida_Cantidad_s .configure(bg = "#273746")

labelBillete3_Salida_Cantidad_s = Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_Salida_Cantidad_s .place (x=450, y= 310)
labelBillete3_Salida_Cantidad_s .configure(bg = "#273746")

labelBillete4_Salida_Cantidad_s = Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_Salida_Cantidad_s .place (x=450, y= 340)
labelBillete4_Salida_Cantidad_s .configure(bg = "#273746")

labelBillete5_Salida_Cantidad_s = Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_Salida_Cantidad_s .place (x=450, y= 370)
labelBillete5_Salida_Cantidad_s .configure(bg = "#273746")

labelBilleteTotal_Salida_Cantidad_s = Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_Salida_Cantidad_s .place (x=450, y= 400)
labelBilleteTotal_Salida_Cantidad_s .configure(bg = "#273746")

labelMonedas1_Salida_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas1_Salida_Total_s .place (x=625, y= 110)
labelMonedas1_Salida_Total_s .configure(bg = "#273746")

labelMonedas2_Salida_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas2_Salida_Total_s .place (x=625, y= 140)
labelMonedas2_Salida_Total_s .configure(bg = "#273746")

labelMonedas3_Salida_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas3_Salida_Total_s .place (x=625, y= 170)
labelMonedas3_Salida_Total_s .configure(bg = "#273746")

labelMonedasTotal_Salida_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTotal_Salida_Total_s .place (x=625, y= 200)
labelMonedasTotal_Salida_Total_s .configure(bg = "#273746")

labelBillete1_Salida_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_Salida_Total_s .place (x=625, y= 250)
labelBillete1_Salida_Total_s .configure(bg = "#273746")

labelBillete2_Salida_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_Salida_Total_s .place (x=625, y= 280)
labelBillete2_Salida_Total_s .configure(bg = "#273746")

labelBillete3_Salida_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_Salida_Total_s .place (x=625, y= 310)
labelBillete3_Salida_Total_s .configure(bg = "#273746")

labelBillete4_Salida_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_Salida_Total_s .place (x=625, y= 340)
labelBillete4_Salida_Total_s .configure(bg = "#273746")

labelBillete5_Salida_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_Salida_Total_s .place (x=625, y= 370)
labelBillete5_Salida_Total_s .configure(bg = "#273746")

labelBilleteTotal_Salida_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_Salida_Total_s .place (x=625, y= 400)
labelBilleteTotal_Salida_Total_s .configure(bg = "#273746")

labelMonedas1_SALDO_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas1_SALDO_Cantidad_s .place (x=800, y= 110)
labelMonedas1_SALDO_Cantidad_s .configure(bg = "#273746")

labelMonedas2_SALDO_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas2_SALDO_Cantidad_s .place (x=800, y= 140)
labelMonedas2_SALDO_Cantidad_s .configure(bg = "#273746")

labelMonedas3_SALDO_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas3_SALDO_Cantidad_s .place (x=800, y= 170)
labelMonedas3_SALDO_Cantidad_s .configure(bg = "#273746")

labelMonedasTotal_SALDO_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTotal_SALDO_Cantidad_s .place (x=800, y= 200)
labelMonedasTotal_SALDO_Cantidad_s .configure(bg = "#273746")

labelBillete1_SALDO_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_SALDO_Cantidad_s .place (x=800, y= 250)
labelBillete1_SALDO_Cantidad_s .configure(bg = "#273746")

labelBillete2_SALDO_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_SALDO_Cantidad_s .place (x=800, y= 280)
labelBillete2_SALDO_Cantidad_s .configure(bg = "#273746")

labelBillete3_SALDO_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_SALDO_Cantidad_s .place (x=800, y= 310)
labelBillete3_SALDO_Cantidad_s .configure(bg = "#273746")

labelBillete4_SALDO_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_SALDO_Cantidad_s .place (x=800, y= 340)
labelBillete4_SALDO_Cantidad_s .configure(bg = "#273746")

labelBillete5_SALDO_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_SALDO_Cantidad_s .place (x=800, y= 370)
labelBillete5_SALDO_Cantidad_s .configure(bg = "#273746")

labelBilleteTotal_SALDO_Cantidad_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_SALDO_Cantidad_s .place (x=800, y= 400)
labelBilleteTotal_SALDO_Cantidad_s .configure(bg = "#273746")

labelMonedas1_SALDO_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas1_SALDO_Total_s .place (x=925, y= 110)
labelMonedas1_SALDO_Total_s .configure(bg = "#273746")

labelMonedas2_SALDO_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas2_SALDO_Total_s .place (x=925, y= 140)
labelMonedas2_SALDO_Total_s .configure(bg = "#273746")

labelMonedas3_SALDO_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas3_SALDO_Total_s .place (x=925, y= 170)
labelMonedas3_SALDO_Total_s .configure(bg = "#273746")

labelMonedasTotal_SALDO_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTotal_SALDO_Total_s .place (x=925, y= 200)
labelMonedasTotal_SALDO_Total_s .configure(bg = "#273746")

labelBillete1_SALDO_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_SALDO_Total_s .place (x=925, y= 250)
labelBillete1_SALDO_Total_s .configure(bg = "#273746")

labelBillete2_SALDO_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_SALDO_Total_s .place (x=925, y= 280)
labelBillete2_SALDO_Total_s .configure(bg = "#273746")

labelBillete3_SALDO_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_SALDO_Total_s .place (x=925, y= 310)
labelBillete3_SALDO_Total_s .configure(bg = "#273746")

labelBillete4_SALDO_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_SALDO_Total_s .place (x=925, y= 340)
labelBillete4_SALDO_Total_s .configure(bg = "#273746")

labelBillete5_SALDO_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_SALDO_Total_s .place (x=925, y= 370)
labelBillete5_SALDO_Total_s .configure(bg = "#273746")

labelBilleteTotal_SALDO_Total_s = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_SALDO_Total_s .place (x=925, y= 400)
labelBilleteTotal_SALDO_Total_s .configure(bg = "#273746")

#Ingresos del cajero

labelDelDia = Label (ingreso_dinero, text = "Del día", fg = "#66CCFF", font = ("Serif", 14))
labelDelDia .place (x=15, y= 25)
labelDelDia .configure(bg = "#273746")

labelAlDia = Label (ingreso_dinero, text = "Al día", fg = "#66CCFF", font = ("Serif", 14))
labelAlDia .place (x=15, y= 60)
labelAlDia .configure(bg = "#273746")

labelTotal_Ingresos_E = Label (ingreso_dinero, text = "TOTAL DE INGRESOS EN EFECTIVO"
                               , fg = "#66CCFF", font = ("Serif", 14))
labelTotal_Ingresos_E .place (x=15, y= 130)
labelTotal_Ingresos_E .configure(bg = "#273746")

labelTotal_Ingresos_T = Label (ingreso_dinero, text = "TOTAL DE INGRESOS EN TARGETA DE CRÉDITO"
                               , fg = "#66CCFF", font = ("Serif", 14))
labelTotal_Ingresos_T .place (x=15, y= 160)
labelTotal_Ingresos_T .configure(bg = "#273746")

labelTotal_Ingresos = Label (ingreso_dinero, text = "TOTAL DE INGRESOS", fg = "#66CCFF", font = ("Serif", 14))
labelTotal_Ingresos .place (x=15, y= 190)
labelTotal_Ingresos .configure(bg = "#273746")

labelEstimados_Ingresos = Label (ingreso_dinero, text = "ESTIMADOS DE INGRESOS MÍNIMOS POR RESIVIR"
                                 , fg = "#66CCFF", font = ("Serif", 14))
labelEstimados_Ingresos .place (x=15, y= 250)
labelEstimados_Ingresos .configure(bg = "#273746")

labelEstimados_FechaEstimacion = Label (ingreso_dinero, text = "Fecha para la estimación"
                                 , fg = "#66CCFF", font = ("Serif", 14))
labelEstimados_FechaEstimacion .place (x=30, y= 280)
labelEstimados_FechaEstimacion .configure(bg = "#273746")

labelEstimados_HoraEstimacion = Label (ingreso_dinero, text = "Hora para la estimación"
                                 , fg = "#66CCFF", font = ("Serif", 14))
labelEstimados_HoraEstimacion .place (x=30, y= 310)
labelEstimados_HoraEstimacion .configure(bg = "#273746")

#Entrada de vehículo
labelEspacios_disponibles = Label (ingreso_vehiculo, text = "Espacios Disponibles      " + str(espacios_c), fg = "#66CCFF", font = ("Serif", 14))
labelEspacios_disponibles .place (x=15, y= 25)
labelEspacios_disponibles .configure(bg = "#273746")

labelPlaca = Label (ingreso_vehiculo, text = "SU PLACA",fg = "#66CCFF", font = ("Serif", 14))
labelPlaca .place (x=15, y= 100)
labelPlaca .configure(bg = "#273746")

labelCampo = Label (ingreso_vehiculo, text = "Campo asignado",fg = "#66CCFF", font = ("Serif", 14))
labelCampo .place (x=15, y= 175)
labelCampo .configure(bg = "#273746")

labelHora = Label (ingreso_vehiculo, text = "Hora de entrada",fg = "#66CCFF", font = ("Serif", 14))
labelHora .place (x=15, y= 250)
labelHora .configure(bg = "#273746")

labelPrecio_Hora = Label (ingreso_vehiculo, text = "Precio por Hora",fg = "#66CCFF", font = ("Serif", 14))
labelPrecio_Hora .place (x=15, y= 325)
labelPrecio_Hora .configure(bg = "#273746")

labelCobroMinimo = Label (ingreso_vehiculo, text = "Cobro minimo de tiempo",fg = "#66CCFF", font = ("Serif", 14))
labelCobroMinimo .place (x=15, y= 325)
labelCobroMinimo .configure(bg = "#273746")

#Cajero del parqueo


#Salida vehiculo
labelSalida_Placa = Label (salida_vehiculo, text = "Su placa", fg = "#66CCFF", font = ("Serif", 14))
labelSalida_Placa .place (x=15, y= 25)
labelSalida_Placa .configure(bg = "#273746")



#Acerca de

labelParqueo = Label (acercade, text = "Parqueo", fg = "#66CCFF", font = ("Serif", 14))
labelParqueo .place (x=10, y= 15)
labelParqueo .configure(bg = "#273746")

labelVersion = Label (acercade, text = "Versión: 0.7", fg = "#66CCFF", font = ("Serif", 14))
labelVersion .place (x=10, y= 45)
labelVersion .configure(bg = "#273746")

labelV_Fecha = Label (acercade, text = "Fecha del último cambio: 16-4-2019", fg = "#66CCFF", font = ("Serif", 14))
labelV_Fecha .place (x=10, y= 75)
labelV_Fecha .configure(bg = "#273746")

labelCreador = Label (acercade, text = "Creador:   Bryand Brenes Zúñiga", fg = "#66CCFF", font = ("Serif", 14))
labelCreador .place (x=10, y= 105)
labelCreador .configure(bg = "#273746")



#Text BOX

#Configuración
textBoxEspacios = Entry(menu_prg, width = 10, font = ("Serif", 14))
textBoxEspacios.place (x=1100, y= 20)

textBoxPrecio = Entry(menu_prg, width = 10, font = ("Serif", 14))
textBoxPrecio.place (x=1100, y= 60)

textBoxPago = Entry(menu_prg, width = 10, font = ("Serif", 14))
textBoxPago.place (x=1100, y= 100)

textBoxRedondeo = Entry(menu_prg, width = 10, font = ("Serif", 14))
textBoxRedondeo.place (x=1100, y= 180)

textBoxMinMax = Entry(menu_prg, width = 10, font = ("Serif", 14))
textBoxMinMax.place (x=1100, y= 220)

textMoneda1 = Entry(menu_prg, width = 10, font = ("Serif", 14))
textMoneda1.place (x=1100, y= 300)

textMoneda2 = Entry(menu_prg, width = 10, font = ("Serif", 14))
textMoneda2.place (x=1100, y= 340)

textMoneda3 = Entry(menu_prg, width = 10, font = ("Serif", 14))
textMoneda3.place (x=1100, y= 380)

textBilletes1 = Entry(menu_prg, width = 10, font = ("Serif", 14))
textBilletes1.place (x=1100, y= 460)

textBilletes2 = Entry(menu_prg, width = 10, font = ("Serif", 14))
textBilletes2.place (x=1100, y= 500)

textBilletes3 = Entry(menu_prg, width = 10, font = ("Serif", 14))
textBilletes3.place (x=1100, y= 540)

textBilletes4 = Entry(menu_prg, width = 10, font = ("Serif", 14))
textBilletes4.place (x=1100, y= 580)

textBilletes5 = Entry(menu_prg, width = 10, font = ("Serif", 14))
textBilletes5.place (x=1100, y= 620)

#Cargar cajero

textBoxCantidadMon1 = Entry(cargar_cajero, width = 10, font = ("Serif", 14))
textBoxCantidadMon1.place (x=450, y= 110)

textBoxCantidadMon2 = Entry(cargar_cajero, width = 10, font = ("Serif", 14))
textBoxCantidadMon2.place (x=450, y= 140)

textBoxCantidadMon3 = Entry(cargar_cajero, width = 10, font = ("Serif", 14))
textBoxCantidadMon3.place (x=450, y= 170)

textBoxCantidadBille1 = Entry(cargar_cajero, width = 10, font = ("Serif", 14))
textBoxCantidadBille1.place (x=450, y= 250)

textBoxCantidadBille2 = Entry(cargar_cajero, width = 10, font = ("Serif", 14))
textBoxCantidadBille2.place (x=450, y= 280)

textBoxCantidadBille3 = Entry(cargar_cajero, width = 10, font = ("Serif", 14))
textBoxCantidadBille3.place (x=450, y= 310)

textBoxCantidadBille4 = Entry(cargar_cajero, width = 10, font = ("Serif", 14))
textBoxCantidadBille4.place (x=450, y= 340)

textBoxCantidadBille5 = Entry(cargar_cajero, width = 10, font = ("Serif", 14))
textBoxCantidadBille5.place (x=450, y= 370)

#Ingresos del cajero
textBoxDelDia = Entry(ingreso_dinero, width = 10, font = ("Serif", 14))
textBoxDelDia.place (x=100, y= 25)

textBoxAlDia = Entry(ingreso_dinero, width = 10, font = ("Serif", 14))
textBoxAlDia.place (x=100, y= 60)

textBoxEstimados_FechaEstimacion = Entry (ingreso_dinero, width = 10, font = ("Serif", 14))
textBoxEstimados_FechaEstimacion .place (x=270, y= 282)

textBoxEstimados_HoraEstimacion = Entry (ingreso_dinero, width = 4, font = ("Serif", 14))
textBoxEstimados_HoraEstimacion .place (x=270, y= 312)

textBoxEstimados_MinuEstimacion = Entry (ingreso_dinero, width = 4, font = ("Serif", 14))
textBoxEstimados_MinuEstimacion .place (x=335, y= 312)

#CAjero del parqueo


#Salida vehiculo
textBoxPlaca_Salida = Entry(salida_vehiculo, width = 10, font = ("Serif", 14))
textBoxPlaca_Salida.place (x=150, y= 25)

#Entrada de vehículo

textBoxPlaca_Entrada = Entry (ingreso_vehiculo, width = 10, font = ("Serif", 14))
textBoxPlaca_Entrada .place (x=150, y= 100)





#Botones

#Configuracion
buttonOK = Button(menu_prg, text = "OK", activebackground = "white", fg = "black", bg = "white", font = ("Serif", 14), width = 8, heigh = 1,command = remplazar)
buttonOK.place(x=500, y = 665)

buttonCancelar = Button(menu_prg, text = "Cancelar", activebackground = "white", fg = "black", bg = "white",
                        font = ("Serif", 14), width = 8, heigh = 1, command = cerrar_configuracion)
buttonCancelar.place(x=700, y = 665)


#Cargar Cajero
buttonOKCargar =  Button(cargar_cajero, text = "OK", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = ok_cargar)
buttonOKCargar.place(x=500, y = 665)

buttonCancelarCargar =  Button(cargar_cajero, text = "Cancelar", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = cerrar_cargar)
buttonCancelarCargar.place(x=750, y = 665)

buttonRevisar =  Button(cargar_cajero, text = "Revisar Saldo", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 11, heigh = 1, command = revisar_saldo)
buttonRevisar.place(x=610, y = 665)

#Saldo_Cajero
buttonOKSaldo =  Button(saldo_cajero, text = "OK", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = ok_saldo_cajero)
buttonOKSaldo.place(x=500, y = 665)

buttonCancelarSaldo_cajero =  Button(saldo_cajero, text = "Cancelar", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = cerrar_saldo)
buttonCancelarSaldo_cajero.place(x=700, y = 665)

#Ingresos de dinero
buttonCancelarSaldo_cajero =  Button(ingreso_dinero, text = "OK", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = ok_ingreso_dinero)
buttonCancelarSaldo_cajero.place(x=15, y= 350)

#Entrada de vehícilo
buttonEntrada_vehículo =  Button(ingreso_vehiculo, text = "OK", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = ok_entrada)
buttonEntrada_vehículo.place(x=15, y= 400)

buttonCancelarEntrada_vehículo =  Button(ingreso_vehiculo, text = "Cancelar", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = cancelar_entrada)
buttonCancelarEntrada_vehículo.place(x=125, y= 400)

#Salir acerca de
buttonAtras_A =  Button(acercade, text = "Atras", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = cerrar_acerca)
buttonAtras_A.place(x=15, y= 150)

#OK salida de vehículo

buttonOKSaldo =  Button(salida_vehiculo, text = "OK", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = ok_salida)
buttonOKSaldo.place(x=15, y = 100)

 
    
    



#CheckButton

VaciarCajero = IntVar()
checkButtonBinario = Checkbutton(saldo_cajero, text = "Vaciar el Cajero",fg = "#66CCFF",font = ("Serif", 14), activebackground = "#273746",
                                 variable = VaciarCajero, onvalue = 1, offvalue = 0, height=1, width = 13, )
checkButtonBinario.place(x=5, y= 430)
checkButtonBinario .configure(bg = "#273746")



# Crear el menu principal
menubarra = Menu(p_principal)

menubarra.add_command(label="Configuración", command = configuracion, state= "normal")
# Crea menu_prg desplegable
menueditar = Menu(menubarra, tearoff=0)
menueditar.add_command(label="Cargar Cajero", command = cargar)
menueditar.add_command(label="Saldo del Cajero", command=saldo__cajero)
menueditar.add_command(label="Ingresos de dinero", command = abrir_ingresos)
menubarra.add_cascade(label="Dinero del cajero", menu=menueditar, state="disable")

#Crea el resto del menu_prg
menubarra.add_command(label = "Entreda de vehículo", state="disable", command = entrada_vehiculo)
menubarra.add_command(label = "Cajero del Parqueo", state="disable")
menubarra.add_command(label = "Salida de vehículo", state="disable", command = salida)
menubarra.add_command(label = "Ayuda", command = abrir_manual)
menubarra.add_command(label = "Acerca de", command = acerca)
menubarra.add_command(label = "Salir", command = salir)
# Mostrar el menu
p_principal.config(menu=menubarra)








# Inciar el programa
p_principal.mainloop()

