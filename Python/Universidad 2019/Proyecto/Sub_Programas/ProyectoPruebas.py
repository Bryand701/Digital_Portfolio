
import tkinter
from tkinter import *
from tkinter import messagebox as mb
import time

open("documentación_parqueo")


#Globales
espacios = []
espacios_c = 0
precio_hora = 0
pago_minimo = 0
redondeo = 0
min_max = 0
mon_1 = 0
mon_2 = 0
mon_3 = 0
billete_1 = 0
billete_2 = 0
billete_3 = 0
billete_4 = 0
billete_5 = 0
v_actaulizaciones = 0
c_mon_1 = 0
c_mon_2 = 0
c_mon_3 = 0
c_billete_1 = 0
c_billete_2 = 0
c_billete_3 = 0
c_billete_4 = 0
c_billete_5 = 0
s_mon_1 = str(mon_1)
s_mon_2 = str(mon_2)
s_mon_3 = str(mon_3)
s_billete_1 = str(billete_1)
s_billete_2 = str(billete_2)
s_billete_3 = str(billete_3)
s_billete_4 = str(billete_4)
s_billete_5 = str(billete_5)




#Funciones
def espacio (c):
    espacios = []
    for x in range (c):
        espacios.append([])
    return espacios
        
def hola():
    
    print ("Hola!")

#Funcion para habilitar las otras opciones del menu_prg despues de meter todos los datos obligatorios
def habilitar ():
    menubarra.entryconfig("Dinero del cajero", state="normal")
    menubarra.entryconfig("Entreda de vahículo", state="normal")
    menubarra.entryconfig("Cajero del Parqueo", state="normal")
    menubarra.entryconfig("Salida de vahículo", state="normal")

#Función para motras un error
def error(x):
    x = str(x)
    r = mb.showwarning("!!ERROR!!", x + " no cumple con las condiciones solicitadas, ¡Reviselo por favor!")	

def error_2():
    r = mb.showwarning("!!ERROR!!","Algo de lo que digitaste no es un número o dejaste un espacio en blanco, ¡Reviselo por favor!")

#Función para verificar que los datos puestos en la configuración esten correctos
def verificar ():

    try:
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
            labelMoneda_1.config(text = "Monedas de " + s_mon_1)
            labelMoneda_2.config(text = "Monedas de " + s_mon_2)
            labelMoneda_3.config(text = "Monedas de " + s_mon_3)
            labelBilletes_1.config(text = "Billetes de " + s_billete_1)
            labelBilletes_2.config(text = "Billetes de " + s_billete_2)
            labelBilletes_3.config(text = "Billetes de " + s_billete_3)
            labelBilletes_4.config(text = "Billetes de " + s_billete_4)
            labelBilletes_5.config(text = "Billetes de " + s_billete_5)
            labelMonedas_1_TOTAL.config (text = mon_1 * c_mon_1)
            labelMonedas_2_TOTAL.config (text = mon_2 * c_mon_2)
            labelMonedas_3_TOTAL.config (text = mon_3 * c_mon_3)
            labelCMonedaTotal.config(text = c_mon_1 + c_mon_2 +c_mon_3)
            labelCBilleteTotal.config(text = c_billete_1 + c_billete_2 + c_billete_3 + c_billete_4 + c_billete_5)
            labelMonedas_Total_TOTAL.config(text = mon_1 * c_mon_1 + mon_2 * c_mon_2 + mon_3 * c_mon_3)

            labelBillete_1_TOTAL.config (text = billete_1 * c_billete_1)

            labelBillete_2_TOTAL.config (text = billete_2 * c_billete_2)

            labelBillete_3_TOTAL.config (text = billete_3 * c_billete_3)

            labelBillete_4_TOTAL.config (text = billete_4 * c_billete_4)

            labelBillete_5_TOTAL.config (text = billete_5 * c_billete_5)

            labelBillete_Total_TOTAL.config (text = billete_5 * c_billete_5 + billete_1 * c_billete_1 + billete_2 * c_billete_2 +
                                              billete_3 * c_billete_3 + billete_4 * c_billete_4)

            habilitar ()
            v_actaulizaciones = 1
            cerrar_configuracion()
    except:
        error_2 ()
def ok_cargar ():
    labelCMoneda_1.config(text = c_mon_1)
    labelCMoneda_2.config(text = c_mon_2)
    labelCMoneda_3.config(text = c_mon_3)
    c_billete_1 = 0
    c_billete_2 = 0
    c_billete_3 = 0
    c_billete_4 = 0
    c_billete_5 = 0

#Función para cargar la ventana de cargar cajero
def cargar ():

    cargar_cajero.update()
    cargar_cajero.deiconify()
    p_principal.withdraw()

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
    
#Funcion para cerrar la ventana de vargar el cajero
def cerrar_cargar ():
    p_principal.update()
    p_principal.deiconify()
    cargar_cajero.withdraw()

#Función para cargar la ventana del saldo del cajero
def saldo__cajero ():
    saldo_cajero.update()
    saldo_cajero.deiconify()
    p_principal.withdraw()

def cerrar_saldo ():
    p_principal.update()
    p_principal.deiconify()
    saldo_cajero.withdraw()


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


#Label
#Ventana Principal
labelEspacios = Label(p_principal, text= "PARQUEO", fg = "#66CCFF", font = ("Cooper Black", 50))
labelEspacios.place(x=525, y= 260)
labelEspacios.configure(bg = "#273746")


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

labelSADC = Label (cargar_cajero, text = "SALDO ANTES DE LA CARGA", fg = "#66CCFF", font = ("Serif", 12))
labelSADC .place (x=175, y= 20)
labelSADC .configure(bg = "#273746")

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

#Saldo_cajero
#Los nombres vienen de la siguiente forma, moneda#/billete#_Columna-Principal_Calumna-Secundaria
#En caso de los casos que se quiere presentar un total en lugar del número (#) viene "Total" 
#En los nombres donde no viene ninguna barra baja ( _ ) es porque no está bajo una conlumna principal
#O es el label donde se crea la colunma principal
#En caso donde solo tiene una barra baja es donde se crean las columnas secundarias

labelDenomiacion = Label (saldo_cajero, text = "DENOMINACIÓN", fg = "#66CCFF", font = ("Serif", 12))
labelDenomiacion .place (x=15, y= 50)
labelDenomiacion .configure(bg = "#273746")

labelSADC = Label (saldo_cajero, text = "SALDO ANTES DE LA CARGA", fg = "#66CCFF", font = ("Serif", 12))
labelSADC .place (x=175, y= 20)
labelSADC .configure(bg = "#273746")

labelCantidad_SADC = Label (saldo_cajero, text = "CANTIDAD", fg = "#66CCFF", font = ("Serif", 12))
labelCantidad_SADC .place (x=200, y= 50)
labelCantidad_SADC .configure(bg = "#273746")

labelTotal_SADC = Label (saldo_cajero, text = "TOTAL", fg = "#66CCFF", font = ("Serif", 12))
labelTotal_SADC .place (x=325, y= 50)
labelTotal_SADC .configure(bg = "#273746")

labelSalida = Label (saldo_cajero, text = "SALIDA", fg = "#66CCFF", font = ("Serif", 12))
labelSalida .place (x=550, y= 20)
labelSalida .configure(bg = "#273746")

labelCargar_Salida = Label (saldo_cajero, text = "CANTIDAD", fg = "#66CCFF", font = ("Serif", 12))
labelCargar_Salida .place (x=450, y= 50)
labelCargar_Salida .configure(bg = "#273746")

labelTotal_Salida = Label (saldo_cajero, text = "TOTAL", fg = "#66CCFF", font = ("Serif", 12))
labelTotal_Salida .place (x=625, y= 50)
labelTotal_Salida .configure(bg = "#273746")

labelSaldo = Label (saldo_cajero, text = "SALDO", fg = "#66CCFF", font = ("Serif", 12))
labelSaldo .place (x=850, y= 20)
labelSaldo .configure(bg = "#273746")

labelCantidad_Saldo= Label (saldo_cajero, text = "CANTIDAD", fg = "#66CCFF", font = ("Serif", 12))
labelCantidad_Saldo .place (x=800, y= 50)
labelCantidad_Saldo .configure(bg = "#273746")

labelTotal_Saldo= Label (saldo_cajero, text = "TOTAL", fg = "#66CCFF", font = ("Serif", 12))
labelTotal_Saldo .place (x=925, y= 50)
labelTotal_Saldo .configure(bg = "#273746")

labelMoneda1_Denominacion = Label (saldo_cajero, text = "Monedas de " + s_mon_1, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda1_Denominacion .place (x=15, y= 110)
labelMoneda1_Denominacion .configure(bg = "#273746")

labelMoneda2_Denominacion = Label (saldo_cajero, text = "Monedas de " + s_mon_2, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda2_Denominacion .place (x=15, y= 140)
labelMoneda2_Denominacion .configure(bg = "#273746")

labelMoneda3_Denominacion = Label (saldo_cajero, text = "Monedas de " + s_mon_3, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda3_Denominacion .place (x=15, y= 170)
labelMoneda3_Denominacion .configure(bg = "#273746")

labelMonedasTOTAL_Denominacion = Label (saldo_cajero, text = "TOTAL DE MONEDAS", fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTOTAL_Denominacion .place (x=15, y= 200)
labelMonedasTOTAL_Denominacion .configure(bg = "#273746")

labelBilletes1_Denominacion = Label (saldo_cajero, text = "Billetes de " + s_billete_1, fg = "#66CCFF", font = ("Serif", 12))
labelBilletes1_Denominacion .place (x=15, y= 250)
labelBilletes1_Denominacion .configure(bg = "#273746")

labelBilletes2_Denominacion = Label (saldo_cajero, text = "Billetes de " + s_billete_2, fg = "#66CCFF", font = ("Serif", 12))
labelBilletes2_Denominacion .place (x=15, y= 280)
labelBilletes2_Denominacion .configure(bg = "#273746")

labelBilletes3_Denominacion = Label (saldo_cajero, text = "Billetes de " + s_billete_3, fg = "#66CCFF", font = ("Serif", 12))
labelBilletes3_Denominacion .place (x=15, y= 310)
labelBilletes3_Denominacion .configure(bg = "#273746")

labelBilletes4_Denominacion = Label (saldo_cajero, text = "Billetes de " + s_billete_4, fg = "#66CCFF", font = ("Serif", 12))
labelBilletes4_Denominacion .place (x=15, y= 340)
labelBilletes4_Denominacion .configure(bg = "#273746")

labelBilletes5_Denominacion = Label (saldo_cajero, text = "Billetes de " + s_billete_5, fg = "#66CCFF", font = ("Serif", 12))
labelBilletes5_Denominacion .place (x=15, y= 370)
labelBilletes5_Denominacion .configure(bg = "#273746")

labelBilletesTOTAL_Denominacion = Label (saldo_cajero, text = "TOTAL DE BILLETES", fg = "#66CCFF", font = ("Serif", 12))
labelBilletesTOTAL_Denominacion .place (x=15, y= 400)
labelBilletesTOTAL_Denominacion .configure(bg = "#273746")

labelMoneda1_SADC_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda1_SADC_Cantidad .place (x=200, y= 110)
labelMoneda1_SADC_Cantidad .configure(bg = "#273746")

labelMoneda2_SADC_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda2_SADC_Cantidad .place (x=200, y= 140)
labelMoneda2_SADC_Cantidad .configure(bg = "#273746")

labelMoneda3_SADC_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda3_SADC_Cantidad .place (x=200, y= 170)
labelMoneda3_SADC_Cantidad .configure(bg = "#273746")

labelMonedaTotal_SADC_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedaTotal_SADC_Cantidad .place (x=200, y= 200)
labelMonedaTotal_SADC_Cantidad .configure(bg = "#273746")

labelBillete1_SADC_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_SADC_Cantidad .place (x=200, y= 250)
labelBillete1_SADC_Cantidad .configure(bg = "#273746")

labelBillete2_SADC_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_SADC_Cantidad .place (x=200, y= 280)
labelBillete2_SADC_Cantidad .configure(bg = "#273746")

labelBillete3_SADC_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_SADC_Cantidad .place (x=200, y= 310)
labelBillete3_SADC_Cantidad .configure(bg = "#273746")

labelBillete4_SADC_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_SADC_Cantidad .place (x=200, y= 340)
labelBillete4_SADC_Cantidad .configure(bg = "#273746")

labelBillete5_SADC_Cantidad= Label (saldo_cajero, text =0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_SADC_Cantidad .place (x=200, y= 370)
labelBillete5_SADC_Cantidad .configure(bg = "#273746")

labelBilleteTotal_SADC_Cantidad= Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_SADC_Cantidad .place (x=200, y= 400)
labelBilleteTotal_SADC_Cantidad .configure(bg = "#273746")

labelMoneda1_SADC_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda1_SADC_Total .place (x=325, y= 110)
labelMoneda1_SADC_Total .configure(bg = "#273746")

labelMoneda2_SADC_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda2_SADC_Total .place (x=325, y= 140)
labelMoneda2_SADC_Total .configure(bg = "#273746")

labelMoneda3_SADC_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMoneda3_SADC_Total .place (x=325, y= 170)
labelMoneda3_SADC_Total .configure(bg = "#273746")

labelMonedaTotal_SADC_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedaTotal_SADC_Total .place (x=325, y= 200)
labelMonedaTotal_SADC_Total .configure(bg = "#273746")

labelBillete1_SADC_Total = Label (saldo_cajero, text =0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_SADC_Total .place (x=325, y= 250)
labelBillete1_SADC_Total .configure(bg = "#273746")

labelBillete2_SADC_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_SADC_Total .place (x=325, y= 280)
labelBillete2_SADC_Total .configure(bg = "#273746")

labelBillete3_SADC_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_SADC_Total .place (x=325, y= 310)
labelBillete3_SADC_Total .configure(bg = "#273746")

labelBillete4_SADC_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_SADC_Total .place (x=325, y= 340)
labelBillete4_SADC_Total .configure(bg = "#273746")

labelBillete5_SADC_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_SADC_Total .place (x=325, y= 370)
labelBillete5_SADC_Total .configure(bg = "#273746")

labelBilleteTotal_SADC_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_SADC_Total .place (x=325, y= 400)
labelBilleteTotal_SADC_Total .configure(bg = "#273746")

labelMonedas1_Salida_Cantidad = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas1_Salida_Cantidad .place (x=450, y= 110)
labelMonedas1_Salida_Cantidad .configure(bg = "#273746")

labelMonedas2_Salida_Cantidad = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas2_Salida_Cantidad .place (x=450, y= 140)
labelMonedas2_Salida_Cantidad .configure(bg = "#273746")

labelMonedas3_Salida_Cantidad = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas3_Salida_Cantidad .place (x=450, y= 170)
labelMonedas3_Salida_Cantidad .configure(bg = "#273746")

labelMonedasTotal_Salida_Cantidad = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTotal_Salida_Cantidad .place (x=450, y= 200)
labelMonedasTotal_Salida_Cantidad .configure(bg = "#273746")

labelBillete1_Salida_Cantidad= Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_Salida_Cantidad .place (x=450, y= 250)
labelBillete1_Salida_Cantidad .configure(bg = "#273746")

labelBillete2_Salida_Cantidad= Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_Salida_Cantidad .place (x=450, y= 280)
labelBillete2_Salida_Cantidad .configure(bg = "#273746")

labelBillete3_Salida_Cantidad= Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_Salida_Cantidad .place (x=450, y= 310)
labelBillete3_Salida_Cantidad .configure(bg = "#273746")

labelBillete4_Salida_Cantidad= Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_Salida_Cantidad .place (x=450, y= 340)
labelBillete4_Salida_Cantidad .configure(bg = "#273746")

labelBillete5_Salida_Cantidad= Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_Salida_Cantidad .place (x=450, y= 370)
labelBillete5_Salida_Cantidad .configure(bg = "#273746")

labelBilleteTotal_Salida_Cantidad= Label (saldo_cajero, text = 0 , fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_Salida_Cantidad .place (x=450, y= 400)
labelBilleteTotal_Salida_Cantidad .configure(bg = "#273746")

labelMonedas1_Salida_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas1_Salida_Total .place (x=625, y= 110)
labelMonedas1_Salida_Total .configure(bg = "#273746")

labelMonedas2_Salida_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas2_Salida_Total .place (x=625, y= 140)
labelMonedas2_Salida_Total .configure(bg = "#273746")

labelMonedas3_Salida_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas3_Salida_Total .place (x=625, y= 170)
labelMonedas3_Salida_Total .configure(bg = "#273746")

labelMonedasTotal_Salida_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTotal_Salida_Total .place (x=625, y= 200)
labelMonedasTotal_Salida_Total .configure(bg = "#273746")

labelBillete1_Salida_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_Salida_Total .place (x=625, y= 250)
labelBillete1_Salida_Total .configure(bg = "#273746")

labelBillete2_Salida_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_Salida_Total .place (x=625, y= 280)
labelBillete2_Salida_Total .configure(bg = "#273746")

labelBillete3_Salida_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_Salida_Total .place (x=625, y= 310)
labelBillete3_Salida_Total .configure(bg = "#273746")

labelBillete4_Salida_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_Salida_Total .place (x=625, y= 340)
labelBillete4_Salida_Total .configure(bg = "#273746")

labelBillete5_Salida_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_Salida_Total .place (x=625, y= 370)
labelBillete5_Salida_Total.configure(bg = "#273746")

labelBilleteTotal_Salida_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_Salida_Total .place (x=625, y= 400)
labelBilleteTotal_Salida_Total .configure(bg = "#273746")

labelMonedas1_SALDO_Cantidad = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas1_SALDO_Cantidad .place (x=800, y= 110)
labelMonedas1_SALDO_Cantidad .configure(bg = "#273746")

labelMonedas2_SALDO_Cantidad = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas2_SALDO_Cantidad .place (x=800, y= 140)
labelMonedas2_SALDO_Cantidad .configure(bg = "#273746")

labelMonedas3_SALDO_Cantidad = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas3_SALDO_Cantidad .place (x=800, y= 170)
labelMonedas3_SALDO_Cantidad .configure(bg = "#273746")

labelMonedasTotal_SALDO_Cantidad = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTotal_SALDO_Cantidad .place (x=800, y= 200)
labelMonedasTotal_SALDO_Cantidad .configure(bg = "#273746")

labelBillete1_SALDO_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_SALDO_Cantidad .place (x=800, y= 250)
labelBillete1_SALDO_Cantidad .configure(bg = "#273746")

labelBillete2_SALDO_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_SALDO_Cantidad .place (x=800, y= 280)
labelBillete2_SALDO_Cantidad .configure(bg = "#273746")

labelBillete3_SALDO_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_SALDO_Cantidad .place (x=800, y= 310)
labelBillete3_SALDO_Cantidad .configure(bg = "#273746")

labelBillete4_SALDO_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_SALDO_Cantidad .place (x=800, y= 340)
labelBillete4_SALDO_Cantidad .configure(bg = "#273746")

labelBillete5_SALDO_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_SALDO_Cantidad .place (x=800, y= 370)
labelBillete5_SALDO_Cantidad .configure(bg = "#273746")

labelBilleteTotal_SALDO_Cantidad= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_SALDO_Cantidad .place (x=800, y= 400)
labelBilleteTotal_SALDO_Cantidad .configure(bg = "#273746")

labelMonedas1_SALDO_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas1_SALDO_Total .place (x=925, y= 110)
labelMonedas1_SALDO_Total .configure(bg = "#273746")

labelMonedas2_SALDO_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas2_SALDO_Total .place (x=925, y= 140)
labelMonedas2_SALDO_Total .configure(bg = "#273746")

labelMonedas3_SALDO_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedas3_SALDO_Total .place (x=925, y= 170)
labelMonedas3_SALDO_Total .configure(bg = "#273746")

labelMonedasTotal_SALDO_Total = Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelMonedasTotal_SALDO_Total .place (x=925, y= 200)
labelMonedasTotal_SALDO_Total .configure(bg = "#273746")

labelBillete1_SALDO_Total= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete1_SALDO_Total .place (x=925, y= 250)
labelBillete1_SALDO_Total .configure(bg = "#273746")

labelBillete2_SALDO_Total= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete2_SALDO_Total .place (x=925, y= 280)
labelBillete2_SALDO_Total .configure(bg = "#273746")

labelBillete3_SALDO_Total= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete3_SALDO_Total .place (x=925, y= 310)
labelBillete3_SALDO_Total .configure(bg = "#273746")

labelBillete4_SALDO_Total= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete4_SALDO_Total .place (x=925, y= 340)
labelBillete4_SALDO_Total .configure(bg = "#273746")

labelBillete5_SALDO_Total= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBillete5_SALDO_Total .place (x=925, y= 370)
labelBillete5_SALDO_Total .configure(bg = "#273746")

labelBilleteTotal_SALDO_Total= Label (saldo_cajero, text = 0, fg = "#66CCFF", font = ("Serif", 12))
labelBilleteTotal_SALDO_Total .place (x=925, y= 400)
labelBilleteTotal_SALDO_Total .configure(bg = "#273746")






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



#Botones

#Configuracion
buttonOK = Button(menu_prg, text = "OK", activebackground = "white", fg = "black", bg = "white", font = ("Serif", 14), width = 8, heigh = 1,command = remplazar)
buttonOK.place(x=500, y = 665)

buttonCancelar = Button(menu_prg, text = "Cancelar", activebackground = "white", fg = "black", bg = "white",
                        font = ("Serif", 14), width = 8, heigh = 1, command = cerrar_configuracion)
buttonCancelar.place(x=700, y = 665)


#Cargar Cajero
buttonCancelarCargar =  Button(cargar_cajero, text = "Cancelar", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = cerrar_cargar)
buttonCancelarCargar.place(x=700, y = 665)


#Saldo_Cajero
buttonCancelarSaldo_cajero =  Button(saldo_cajero, text = "Cancelar", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = cerrar_saldo)
buttonCancelarSaldo_cajero.place(x=700, y = 665)


# Crear el menu principal
menubarra = Menu(p_principal)

menubarra.add_command(label="Configuración", command = configuracion)
# Crea menu_prg desplegable
menueditar = Menu(menubarra, tearoff=0)
menueditar.add_command(label="Cargar Cajero", command = cargar)
menueditar.add_command(label="Saldo del Cajero", command=saldo__cajero)
menueditar.add_command(label="Ingresos de dinero")
menubarra.add_cascade(label="Dinero del cajero", menu=menueditar, state="normal")

#Crea el resto del menu_prg
menubarra.add_command(label = "Entreda de vahículo", state="normal")
menubarra.add_command(label = "Cajero del Parqueo", state="normal")
menubarra.add_command(label = "Salida de vahículo", state="normal")
menubarra.add_command(label = "Ayuda")
menubarra.add_command(label = "Acerca de")
menubarra.add_command(label = "Salir", command = salir)
# Mostrar el menu
p_principal.config(menu=menubarra)








# Inciar el programa
p_principal.mainloop()

