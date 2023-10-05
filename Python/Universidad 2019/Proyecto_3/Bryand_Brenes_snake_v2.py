import tkinter
from tkinter import *
from tkinter import messagebox as mb
import subprocess
import sys,time
import pygame
from pygame.locals import *
import tkinter as tk
import random
from tkinter.colorchooser import askcolor
import pickle
from tkinter.filedialog import askopenfilenames
import os
from PIL import Image, ImageTk
#subprocess.Popen(['3756-701.pdf'],shell=True)

escala = 20

#Globales
global imagen_cabeza_horizontal,imagen_cabeza_vertical,imagen_cuerpo_horizontal,imagen_cuerpo_vertical,imagen_curba,imagen_manzana
global ruta_manzana
global ruta_cabeza_horizontal
global ruta_cabeza_vertical
global ruta_cuerpo_horizontal
global ruta_cuerpo_vertical
global ruta_cuerpo_curba
global n_color_Fondo
global n_color_Pared
global color_fondo, color_paredes,glob_serp
global rand1,rand2
global g_derecha,g_izquierda,g_arriba,g_abajo

g_derecha,g_izquierda,g_arriba,g_abajo = True,False,False,False

rand1,rand2 = 10, 10


global dicc_nombres


if os.path.isfile("usuarios.dat"):
    perfiles = open("usuarios.dat","rb")
    dicc = pickle.load(perfiles)
    dicc_nombres = dicc
    perfiles.close
else:
    perfiles = open("usuarios.dat","wb")
    dicc_nombres = {}
    pickle.dump (dicc_nombres,perfiles)
    perfiles.close()    

global registro_records
if os.path.isfile("records.dat"):
    record = open("records.dat","rb")
    rec = pickle.load(record)
    registro_records = rec
    record.close
else:
    record = open("records.dat","wb")
    lista =[]
    sub_lista = []
    for x in range (10):
        sub_lista.append(["------",[],(0,0,0)])
    for x in range (8):
        lista.append(sub_lista)

    pickle.dump (lista,record)
    registro_records = lista
    record.close()

global multiple
multiple = False

glob_serp =[[1,3],[1,2],[1,1],[1,0]]

color_fondo = (55,200,30)
color_paredes = (255,255,255)


imagen_cabeza_horizontal = pygame.image.load("cabeza horizontal.jpg") #cabeza
imagen_cabeza_horizontal = pygame.transform.scale(imagen_cabeza_horizontal, (escala,escala)) #cambiar el tamaño de la cabeza

imagen_cabeza_vertical = pygame.image.load("cabeza vertical.jpg") #cabeza
imagen_cabeza_vertical = pygame.transform.scale(imagen_cabeza_vertical, (escala,escala))

imagen_cuerpo_horizontal = pygame.image.load("cuerpo horizontal.jpg") #cabeza
imagen_cuerpo_horizontal = pygame.transform.scale(imagen_cuerpo_horizontal, (escala,escala))

imagen_cuerpo_vertical = pygame.image.load("cuerpo vertical.jpg") #cabeza
imagen_cuerpo_vertical = pygame.transform.scale(imagen_cuerpo_vertical, (escala,escala))

imagen_curba = pygame.image.load("curba derecha abajo.jpg") #cabeza
imagen_curba = pygame.transform.scale(imagen_curba, (escala,escala))

imagen_manzana = pygame.image.load("manzana.png") #manzana
imagen_manzana = pygame.transform.scale(imagen_manzana, (escala,escala))

ruta_manzana = "manzana.png"
ruta_cabeza_horizontal = "cabeza horizontal.jpg"
ruta_cabeza_vertical = "cabeza vertical.jpg"
ruta_cuerpo_horizontal = "cuerpo horizontal.jpg"
ruta_cuerpo_vertical = "cuerpo vertical.jpg"
ruta_cuerpo_curba = "curba derecha abajo.jpg"
n_color_Fondo = (55,200,30)
n_color_Pared = (255,255,255)

global imagen_usuario, n_imagen_usuario
imagen_usuario = "Caudro_blanco.png"

n_imagen_usuario = imagen_usuario 


global minutos,horas,segundos,c

minutos = 0
horas = 0
segundos = 0
c = 0


global ancho, altura #Tamño del juego
ancho, altura = 20, 20

global multiple_v
multiple_v = False

global paredes # Si hay o no paredes
paredes = False

global p_paredes
paredes = False

global p_altura, pancho
p_ancho, p_altura = 20, 20

global musica_principal, musica_manzana, musica_ganar
global musica_chocar_cuerpo, musica_pared

musica_principal = "Star Theme.mp3"
musica_manzana = "Mushroom Sound Effect.mp3"
musica_ganar = "Super Mario Bros Win Stage Sound Effect.mp3"
musica_chocar_cuerpo = "Perder.mp3"
musica_pared = "chocar.mp3"

global musica_principal_v, musica_manzana_v, musica_ganar_v
global musica_chocar_cuerpo_v, musica_pared_v

musica_principal_v = musica_principal
musica_manzana_v = musica_manzana
musica_ganar_v = musica_ganar
musica_chocar_cuerpo_v = musica_chocar_cuerpo
musica_pared_v = musica_pared

global musica
musica = True

global musica_v
musica_v = True

global p_cuerpo, p_paredes
p_cuerpo = False
p_paredes = False


global puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20
puntuacion_14 = 0
puntuacion_16 = 0
puntuacion_18 = 0
puntuacion_20 = 0

#Funciones de error
def error():
    r = mb.showwarning("!!ERROR!!","No se ha credo una partida con este usuario, ¡Intenta despues de crear una!")
def error2():
    r = mb.showwarning("!!ERROR!!","Una de las opciones de tamaño o paredes no ha sido seleccionada, ¡Reviselo por favor!")
def error3():
    r = mb.showwarning("!!ERROR!!","La contraseña no es valida, ¡Reviselo por favor!")

def error4():
    r = mb.showwarning("!!ERROR!!","El nombre es demasiado largo, ¡Reviselo por favor!")
def error5():
    r = mb.showwarning("!!ERROR!!","Este perfil ya existe, ¡Reviselo por favor!")
def error6():
    r = mb.showwarning("!!ERROR!!","No hay ningun usuario creado, ¡Intenta despues de crear uno!")
def error7():
    r = mb.showwarning("!!ERROR!!","Contraseña Incorrecta, ¡Reviselo por favor!")
def error8():
    r = mb.showwarning("!!ERROR!!","No a seleccionado ningun usuario, ¡Reviselo por favor!")
#Función para guardar el juego
def guardar_partida():

    global imagen_usuario
    global dicc_nombres
    global usuario_actual
    global contraseña_actual

    
    global glob_serp,minutos,horas ,segundos,c
    global rand1,rand2
    global g_derecha,g_izquierda,g_arriba,g_abajo
    global ruta_manzana ,ruta_cabeza_horizontal , ruta_cabeza_vertical, ruta_cuerpo_horizontal, ruta_cuerpo_vertical, ruta_cuerpo_curba, n_color_Fondo, n_color_Pared
    global ancho, altura, paredes
    global musica_v, musica
    global musica_principal, musica_manzana, musica_ganar
    global musica_chocar_cuerpo, musica_pared
    global multiple
    global puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20
    tupla = (glob_serp,minutos,horas ,segundos,c,rand1,rand2,g_derecha,g_izquierda,g_arriba,g_abajo,ruta_manzana ,ruta_cabeza_horizontal,
                    ruta_cabeza_vertical, ruta_cuerpo_horizontal, ruta_cuerpo_vertical, ruta_cuerpo_curba, n_color_Fondo, n_color_Pared,
                    ancho, altura,paredes,musica_v, musica,musica_principal, musica_manzana, musica_ganar,musica_chocar_cuerpo, musica_pared,
                    multiple,puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20)
    
    dicc_nombres[usuario_actual] = contraseña_actual,imagen_usuario, tupla

    

    partida = open("usuarios.dat","wb")
    pickle.dump (dicc_nombres,partida)
    global p_cuerpo, p_paredes
    p_cuerpo = False
    p_paredes = False
    partida.close()
    cerrar_juego()

#Función para cargar la partida
def cargar_partida():
    try:
        global imagen_usuario
        global dicc_nombres
        global usuario_actual
        global contraseña_actual
        
        global glob_serp,minutos,horas ,segundos,c
        global rand1,rand2
        global g_derecha,g_izquierda,g_arriba,g_abajo
        global imagen_cabeza_horizontal,imagen_cabeza_vertical,imagen_cuerpo_horizontal,imagen_cuerpo_vertical,imagen_curba,imagen_manzana, color_fondo, color_paredes
        global ancho, altura, paredes
        global musica_v, musica
        global musica_principal, musica_manzana, musica_ganar
        global musica_chocar_cuerpo, musica_pared
        global musica_principal_v, musica_manzana_v, musica_ganar_v
        global musica_chocar_cuerpo_v, musica_pared_v
        global multiple
        global puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20
        
        partida = open("usuarios.dat","rb")
        parti = pickle.load(partida)
        part= parti[usuario_actual]
        part = part[2]
        serp = part[0]
        minutos = part[1]
        horas = part[2]
        segundos = part[3]
        c = part[4]
        rand1 = part[5]
        rand2 = part[6]
        g_derecha = part[7]
        g_izquierda = part[8]
        g_arriba = part[9]
        g_abajo = part[10]

        imagen_cabeza_horizontal = pygame.image.load(part[12])
        imagen_cabeza_horizontal = pygame.transform.scale(imagen_cabeza_horizontal, (escala,escala)) #cambiar el tamaño de la cabeza


        imagen_cabeza_vertical = pygame.image.load(part[13])
        imagen_cabeza_vertical = pygame.transform.scale(imagen_cabeza_vertical, (escala,escala))

        imagen_cuerpo_horizontal = pygame.image.load(part[14])
        imagen_cuerpo_horizontal = pygame.transform.scale(imagen_cuerpo_horizontal, (escala,escala))

        imagen_cuerpo_vertical = pygame.image.load(part[15])
        imagen_cuerpo_vertical = pygame.transform.scale(imagen_cuerpo_vertical, (escala,escala))

        imagen_curba = pygame.image.load(part[16])
        imagen_curba = pygame.transform.scale(imagen_curba, (escala,escala))

        imagen_manzana = pygame.image.load(part[11])
        imagen_manzana = pygame.transform.scale(imagen_manzana, (20,20))

        color_fondo = part[17]
        color_paredes = part[18]

        ancho = part[19]
        altura = part[20]
        paredes = part[21]
        musica_v = part[22]
        musica = part[23]

        musica_principal=part[24]
        musica_manzana = part[25]
        musica_ganar = part[26]
        musica_chocar_cuerpo = part[27]
        musica_pared = part[28]
        multiple = part[29]

        puntuacion_14 = part[30]
        puntuacion_16 = part[31]
        puntuacion_18 = part[32]
        puntuacion_20 = part[33]

        parti[1]=imagen_usuario
        parti[0]=contraseña_actual

        glob_serp = serp[:]
        partida.close
        juego()

    except:
        error()


#Funciones en pygame

#Funciones para comparar dos listas de posición
def derecha(A, B): # Si A está a la derecha de B
    return A[1] - 1 == B[1]

def izquierda(A, B): #Si A está a la izquierda de B
    return A[1] + 1 == B[1]

def arriba(A, B): #Si A está a la arriba de B
    return A[0] + 1 == B[0]

def abajo(A, B): #Si A está a la abajo de B
    return A[0] - 1 == B[0]

#Función para analizar una parte de la serpiente

def analizarParte(serpiente, pos):
    posicion_anterior = pos - 1 #Porcicion anterior

    posicion_siguiente = pos + 1 #Siguiente pocición

    if posicion_siguiente >= len(serpiente):
        return "COLA"
    parteAnterior = serpiente[posicion_anterior]

    parteActual = serpiente[pos]

    parteSiguiente = serpiente[posicion_siguiente]

    #CurvaAbajoDerecha
    if derecha(parteSiguiente,parteActual) and abajo(parteAnterior,parteActual):
        return "CURVA ABAJO DERECHA"
    if derecha(parteAnterior, parteActual) and abajo(parteSiguiente,parteActual):
        return "CURVA ABAJO DERECHA"
    #CurvaAbajoIzquierda
    if izquierda(parteSiguiente,parteActual) and abajo(parteAnterior,parteActual):
        return "CURVA ABAJO IZQUIERDA"
    if izquierda(parteAnterior, parteActual) and abajo(parteSiguiente,parteActual):
        return "CURVA ABAJO IZQUIERDA"
    #CurvaArribaDerecha
    if derecha(parteSiguiente,parteActual) and arriba(parteAnterior,parteActual):
        return "CURVA ARRIBA DERECHA"
    if derecha(parteAnterior, parteActual) and arriba(parteSiguiente,parteActual):
        return "CURVA ARRIBA DERECHA"
    #CurvaArribaIzquierda
    if izquierda(parteSiguiente,parteActual) and arriba(parteAnterior,parteActual):
        return "CURVA ARRIBA IZQUIERDA"
    if izquierda(parteAnterior, parteActual) and arriba(parteSiguiente,parteActual):
        return "CURVA ARRIBA IZQUIERDA"

    return "COLA"

#Función para mostrar la puntuación
def puntuacion (puntos,ventana_juego):
    global altura
    fuente_pygame = pygame.font.SysFont("Consola",40)
    texto = fuente_pygame.render("Puntuación: " + str(puntos),0,(0,0,0,0))
    ventana_juego.blit (texto,(0,altura*20+20))

#función para mostrar los contróles
def controles (ventana_juego):
    global altura
    fuente_pygame = pygame.font.SysFont("Consola",40)
    texto = fuente_pygame.render("Precione P para pausar el juego",0,(0,0,0,0))
    ventana_juego.blit (texto,(0,altura*20+50))
    texto2 = fuente_pygame.render("Precione G para guardar el juego",0,(0,0,0,0))
    ventana_juego.blit (texto2,(0,altura*20+80))

#Función para cerrar el juego

def cerrar_juego():
    global minutos,horas,segundos,glob_serp
    global c
    global rand1,rand2
    global g_derecha,g_izquierda,g_arriba,g_abajo
    global p_cuerpo, p_paredes
    global musica_chocar_cuerpo, musica_pared
    global puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20
    puntuacion_14 = 0
    puntuacion_16 = 0
    puntuacion_18 = 0
    puntuacion_20 = 0
    if p_cuerpo:
        if musica:
                pygame.mixer.music.load(musica_chocar_cuerpo)
                pygame.mixer.music.play()
    elif p_paredes:
        if musica:
                pygame.mixer.music.load(musica_pared)
                pygame.mixer.music.play()
        

    g_derecha,g_izquierda,g_arriba,g_abajo = True,False,False,False
    

    rand1,rand2 = 10, 10

    glob_serp =[[1,3],[1,2],[1,1],[1,0]]
    minutos = 0
    horas = 0
    segundos = 0
    c = 0
    pygame.display.quit()
    p_principal.update()
    p_principal.deiconify()

#Función para analizar una parte del cuerpo de la serpiente
def analizar_cuerpo(serpiente, pos,direccion):
    posicion_anterior = pos - 1 #Porcicion anterior
    posicion_siguiente = pos + 1 #Siguiente pocición
    parteAnterior = serpiente[posicion_anterior]
    parteActual = serpiente[pos]
    if posicion_siguiente >= len(serpiente):

        if izquierda(parteAnterior,parteActual) and direccion == "dere":
            return "DERECHA"
        elif derecha(parteAnterior, parteActual) and direccion == "dere":
            return "DERECHA"
        #CurvaAbajoIzquierda
        elif derecha(parteAnterior,parteActual):
            return "IZQUIERDA"
        elif izquierda(parteAnterior, parteActual):
            return "IZQUIERDA"
        #CurvaArribaDerecha
        elif abajo(parteAnterior,parteActual) and direccion == "aba":
            return "ABAJO "
        elif arriba(parteAnterior, parteActual) and direccion == "aba":
            return "ABAJO "
        #CurvaArribaIzquierda
        elif arriba(parteAnterior,parteActual) :
            return "ARRIBA"
        elif abajo(parteAnterior, parteActual):
            return "ARRIBA"

        return "COLA"

    parteSiguiente = serpiente[posicion_siguiente]

    if derecha(parteSiguiente,parteActual) and izquierda(parteAnterior,parteActual) and direccion == "dere":
        return "DERECHA"
    elif derecha(parteAnterior, parteActual) and izquierda(parteSiguiente,parteActual)and direccion == "dere":
        return "DERECHA"
    #CurvaAbajoIzquierda
    elif izquierda(parteSiguiente,parteActual) and derecha(parteAnterior,parteActual):
        return "IZQUIERDA"
    elif izquierda(parteAnterior, parteActual) and derecha(parteSiguiente,parteActual):
        return "IZQUIERDA"
    #CurvaArribaDerecha
    elif arriba(parteSiguiente,parteActual) and abajo(parteAnterior,parteActual) and direccion == "aba":
        return "ABAJO "
    elif arriba(parteAnterior, parteActual) and abajo(parteSiguiente,parteActual) and direccion == "aba":
        return "ABAJO "
    #CurvaArribaIzquierda
    elif abajo(parteSiguiente,parteActual) and arriba(parteAnterior,parteActual) :
        return "ARRIBA"
    elif abajo(parteAnterior, parteActual) and arriba(parteSiguiente,parteActual) :
        return "ARRIBA"



    if derecha(parteSiguiente,parteActual)  and direccion == "dere":
        return "DERECHA"
    elif  izquierda(parteSiguiente,parteActual)and direccion == "dere":
        return "DERECHA"
    #CurvaAbajoIzquierda
    elif izquierda(parteSiguiente,parteActual) :
        return "IZQUIERDA"
    elif derecha(parteSiguiente,parteActual):
        return "IZQUIERDA"
    #CurvaArribaDerecha
    elif arriba(parteSiguiente,parteActual) and direccion == "aba":
        return "ABAJO "
    elif abajo(parteSiguiente,parteActual) and direccion == "aba":
        return "ABAJO "
    #CurvaArribaIzquierda
    elif abajo(parteSiguiente,parteActual)  :
        return "ARRIBA"
    elif arriba(parteSiguiente,parteActual) :
        return "ARRIBA"

    return "Cola"

#Función para iniciar el juego
def juego():
    pygame.init()
    p_principal.withdraw()
    obtener_nombre.withdraw()
    ventana_juego = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Snake")

    #Velocidad de repeticiones
    ticks = 15



    #Crear repeticiones por tiempo
    tiempo = pygame.time.Clock()

    #función para dibujar a la serpiente

    def dibujar_serpiente(serpiente,derecha, izquierda,arriba,abajo):
        # Cabeza
        rotar_cuerpo = pygame.transform.rotate(imagen_cuerpo_horizontal, 180)
        rotar_cuerpo2 = pygame.transform.rotate(imagen_cuerpo_vertical, 180)

        rotar_curba1 = pygame.transform.rotate(imagen_curba, 90)
        rotar_curba2 = pygame.transform.rotate(imagen_curba, 180)
        rotar_curba3 = pygame.transform.rotate(imagen_curba, 270)
        #Formar las esquinas
        if derecha:
            ventana_juego.blit(imagen_cabeza_horizontal, (serpiente[0][1]*20+10,serpiente[0][0]*20+10))
        elif  izquierda:
            imagen_cabeza = pygame.transform.rotate(imagen_cabeza_horizontal, 180)
            ventana_juego.blit(imagen_cabeza, (serpiente[0][1]*20+10,serpiente[0][0]*20+10))
        elif arriba:
            ventana_juego.blit(imagen_cabeza_vertical, (serpiente[0][1]*20+10,serpiente[0][0]*20+10))
        else:
            imagen_cabeza = pygame.transform.rotate(imagen_cabeza_vertical, 180)
            ventana_juego.blit(imagen_cabeza, (serpiente[0][1]*20+10,serpiente[0][0]*20+10))
        # Colocar la imagen de la cabeza
        # Formar la cola
        for i in range(1,len(serpiente)): # !!
            parte = analizarParte(serpiente, i)

            if parte == "CURVA ABAJO DERECHA":
                ventana_juego.blit(imagen_curba,(serpiente[i][1]*20+10,serpiente[i][0]*20+10,escala,escala))#imagen de la curva abajo derecha
            elif parte == "CURVA ARRIBA IZQUIERDA":
                ventana_juego.blit(rotar_curba2,(serpiente[i][1]*20+10,serpiente[i][0]*20+10,escala,escala))#imagen de la curva arriba izquierda
            elif parte == "CURVA ARRIBA DERECHA":
                ventana_juego.blit(rotar_curba1,(serpiente[i][1]*20+10,serpiente[i][0]*20+10,escala,escala))#imagen de la curva arriba derecha
            elif parte == "CURVA ABAJO IZQUIERDA":
                ventana_juego.blit(rotar_curba3,(serpiente[i][1]*20+10,serpiente[i][0]*20+10,escala,escala))#imagen de la curva abajo izquierda
            else:
                direccion = ""
                if derecha:
                    direccion = "dere"
                elif abajo:
                    direccion = "aba"
                parte_cuerpo = analizar_cuerpo(serpiente, i,direccion)

                if parte_cuerpo == "DERECHA":
                    ventana_juego.blit(imagen_cuerpo_horizontal,(serpiente[i][1]*20+10,serpiente[i][0]*20+10,escala,escala))
                elif  parte_cuerpo == "IZQUIERDA":
                    ventana_juego.blit(rotar_cuerpo,(serpiente[i][1]*20+10,serpiente[i][0]*20+10,escala,escala))
                elif parte_cuerpo=="ARRIBA":
                    ventana_juego.blit(imagen_cuerpo_vertical,(serpiente[i][1]*20+10,serpiente[i][0]*20+10,escala,escala))
                elif parte_cuerpo=="ABAJO":
                    ventana_juego.blit(rotar_cuerpo2,(serpiente[i][1]*20+10,serpiente[i][0]*20+10,escala,escala))
                else:
                    ventana_juego.blit(rotar_cuerpo2,(serpiente[i][1]*20+10,serpiente[i][0]*20+10,escala,escala))

    # Funciones para avansar
    def avanzar (serpiente,nuevapos):
        global p_cuerpo, p_paredes
                    
        if nuevapos[0] >= altura: # Condicion de altura
            if paredes: #Condición de paredes
                p_cuerpo = False
                p_paredes = True
                if multiple:
                    multi_nivel()
                else:
                    cerrar_juego()
            else:
                nuevapos[0] = 0
        elif nuevapos[0] < 0: # Condicion de altura
            if paredes:
                p_cuerpo = False
                p_paredes = True
                if multiple:
                    multi_nivel()
                else:
                    cerrar_juego()
            else:
                nuevapos[0] = altura-1
        elif nuevapos[1] >= ancho: # Condicion de anchura
            if paredes:
                p_cuerpo = False
                p_paredes = True
                if multiple:
                    multi_nivel()
                else:
                    cerrar_juego()
            else:
                nuevapos[1] = 0
        elif nuevapos[1] < 0: # Condicion de anchura
            if paredes:
                p_cuerpo = False
                p_paredes = True
                if multiple:
                    multi_nivel()
                else:
                    cerrar_juego()
            else:
                nuevapos[1] = ancho-1
        #mover el cuerpo
        for i in reversed(range(1,len(serpiente))):
            serpiente[i] = serpiente[i-1]
        serpiente[0]=nuevapos
        return serpiente

    #Función para iniciar el juego
    def iniciarventana():
        
        global ancho, altura
        global minutos,horas,segundos
        global c
        global color_fondo, color_paredes
        global glob_serp
        global rand1,rand2
        global g_derecha,g_izquierda,g_arriba,g_abajo
        global musica_principal, musica_manzana, musica_ganar
        global p_cuerpo, p_paredes
        global multiple
        global puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20

        if musica:
            pygame.mixer.music.load(musica_principal)
            pygame.mixer.music.play(-1)
        pausado = False
        pygame.init()
        ventana_juego = pygame.display.set_mode((escala*ancho+320,escala*altura+120)) #tamaño de la ventana de juego
        serpiente = glob_serp #pocicion de inicio
        derecha,izquierda,arriba,abajo=g_derecha,g_izquierda,g_arriba,g_abajo #Variables para el movimiento

        while True:
            #reproducir musica
            
            #Movimiento de la serpiente
            if derecha == True:
                serpiente=avanzar(serpiente,[serpiente[0][0],serpiente[0][1]+1])
            if izquierda == True:
                serpiente=avanzar(serpiente,[serpiente[0][0],serpiente[0][1]-1])
            if arriba == True:
                serpiente=avanzar(serpiente,[serpiente[0][0]-1,serpiente[0][1]])
            if abajo == True:
                serpiente=avanzar(serpiente,[serpiente[0][0]+1,serpiente[0][1]])

            ventana_juego.fill(color_fondo) #color del fondo de la ventana de juego

            #Dibujar las paredes
            if paredes == True:
                pygame.draw.rect(ventana_juego,(color_paredes),(5,5,20*ancho+9,20*altura+9),5)
            elif paredes == False:
                pygame.draw.rect(ventana_juego,(color_paredes),(10,10,20*ancho,20*altura)) #dibujar la paredes del juego
            dibujar_serpiente(serpiente,derecha, izquierda,arriba,abajo)

            ventana_juego.blit(imagen_manzana,(rand1*20+10,rand2*20+10,escala,escala))

            #Mostrar la puntuación
            puntuacion (len(serpiente)-4,ventana_juego)

            #Mostrar el tiempo

            if c < ticks:
                c += 1
            else:
                c = 0
                segundos += 1

            if segundos == 60:
                minutos += 1
                segundos = 0
            if minutos == 60:
                horas += 1
                minutos = 0
            #Mostrar el tiempo
            fuente_pygame = pygame.font.SysFont("Consola",40)
            fuente_pygame2 = pygame.font.SysFont("Consola",28)
            texto4 = fuente_pygame.render("Tiempo " +str (horas)+ " : "+ str(minutos)
                                          + " : "  + str(segundos),0,(0,0,0,0))
            ventana_juego.blit (texto4,(altura*20+25,10))
            if multiple:
                texto5 = fuente_pygame2.render("Puntuación del nivel 14*14: " + str(puntuacion_14),0,(0,0,0,0))
                ventana_juego.blit (texto5,(altura*20+25,40))
                texto6 = fuente_pygame2.render("Puntuación del nivel 16*16: " + str(puntuacion_16),0,(0,0,0,0))
                ventana_juego.blit (texto6,(altura*20+25,60))
                texto7 = fuente_pygame2.render("Puntuación del nivel 18*18: " + str(puntuacion_18),0,(0,0,0,0))
                ventana_juego.blit (texto7,(altura*20+25,80))
                texto8 = fuente_pygame2.render("Puntuación del nivel 20*20: " + str(puntuacion_20),0,(0,0,0,0))
                ventana_juego.blit (texto8,(altura*20+25,100))
                texto8 = fuente_pygame2.render("Puntuación Total: " + str(puntuacion_20+puntuacion_18+puntuacion_16+puntuacion_14),0,(0,0,0,0))
                ventana_juego.blit (texto8,(altura*20+25,120))
            #Mostrar los controles
            controles (ventana_juego)

            while pausado:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        global p_cuerpo, p_paredes
                        pygame.mixer.music.stop()
                        p_cuerpo = False
                        p_paredes = False
                        cerrar_juego()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            pausado = False
            #obtener los eventos del teclado
            for events in pygame.event.get():
                if events.type == QUIT:
                    pygame.mixer.music.stop()
                    p_cuerpo = False
                    p_paredes = False
                    cerrar_juego()
                elif events.type == KEYDOWN:
                    if events.key==K_DOWN and arriba==False:
                        abajo,arriba,derecha,izquierda=True,False,False,False
                    if events.key==K_UP and abajo==False:
                        arriba,abajo,derecha,izquierda=True,False,False,False
                    if events.key==K_RIGHT and izquierda==False:
                        derecha,abajo,arriba,izquierda=True,False,False,False
                    if events.key==K_LEFT and derecha==False:
                        izquierda,abajo,arriba,derecha=True,False,False,False
                    if events.key==K_p:
                        pausado = True
                    if events.key==K_g:
                        pygame.mixer.music.stop()
                        g_derecha,g_izquierda,g_arriba,g_abajo = derecha,izquierda,arriba,abajo
                        guardar_partida()

            #cohque con la manzana
            if serpiente[0][0]==rand2 and serpiente[0][1]==rand1:

                serpiente.append([0,0]) # crecimiento de la cola
                #musica de la manzana
                if musica:
                        pygame.mixer.music.load(musica_manzana)
                        pygame.mixer.music.play()

                if len(serpiente) == ancho*ancho:
                    if multiple:
                        pygame.display.quit()
                        multi_nivel()
                    else:
                        cerrar_juego()

                #cambio de pocición de la manzan
                rand1,rand2 = random.randint(1,ancho - 1),random.randint(1,altura - 1)
                for x in serpiente:
                    if x[0] == rand1 and x[1] == rand2:
                        rand1,rand2 = random.randint(1,ancho - 1),random.randint(1,altura - 1)

            #choque con el cuerpo
            for i in range(1,len(serpiente)):
                pygame.init()
                if serpiente[0][0] == serpiente[i][0] and serpiente[0][1]== serpiente[i][1]:

                    p_cuerpo = True
                    p_paredes = False                    
                    
                    if multiple:
                        pygame.display.quit()
                        multi_nivel()                        
                    else:
                        cerrar_juego()


            tiempo.tick(ticks)
            pygame.display.update()
    try:
        iniciarventana()
    except pygame.error:
        pass   


#Funciones en takinter

#Funciones para los radiobutton
def tamaño_14 ():
    global  p_ancho, p_altura
    p_ancho, p_altura = 14, 14
    global multiple_v
    multiple_v = False

def tamaño_16 ():
    global  p_ancho, p_altura
    p_ancho, p_altura = 16, 16
    global multiple_v
    multiple_v = False

def tamaño_18 ():
    global  p_ancho, p_altura
    p_ancho, p_altura = 18, 18
    global multiple_v
    multiple_v = False

def tamaño_20 ():
    global  p_ancho, p_altura
    p_ancho, p_altura = 20, 20
    global multiple_v
    multiple_v = False

def con_paredes():
    global p_paredes
    p_paredes = True

def sin_paredes ():
    global p_paredes
    p_paredes = False

def m_opciones ():
    opciones.update()
    opciones.deiconify()
    p_principal.withdraw()

def ac_multiple ():
    global multiple_v
    multiple_v = True
    global  p_ancho, p_altura
    p_ancho, p_altura = 14, 14

#Función para el botón ok de configuracion
def ok_opciones ():
    global imagen_cabeza_horizontal,imagen_cabeza_vertical,imagen_cuerpo_horizontal,imagen_cuerpo_vertical,imagen_curba,imagen_manzana, color_fondo, color_paredes
    global  p_ancho, p_altura
    global p_paredes
    global paredes
    global ancho, altura
    global ruta_manzana
    global ruta_cabeza_horizontal
    global ruta_cabeza_vertical
    global ruta_cuerpo_horizontal
    global ruta_cuerpo_vertical
    global ruta_cuerpo_curba
    global n_color_Fondo
    global n_color_Pared
    global musica_v, musica
    global musica_principal, musica_manzana, musica_ganar
    global musica_chocar_cuerpo, musica_pared
    global musica_principal_v, musica_manzana_v, musica_ganar_v
    global musica_chocar_cuerpo_v, musica_pared_v
    global multiple, multiple_v


    try:
        ancho, altura = p_ancho, p_altura
        paredes = p_paredes

        color_fondo = n_color_Fondo
        color_paredes = n_color_Pared

        imagen_cabeza_horizontal = pygame.image.load(ruta_cabeza_horizontal) #cabeza
        imagen_cabeza_horizontal = pygame.transform.scale(imagen_cabeza_horizontal, (escala,escala)) #cambiar el tamaño de la cabeza

        imagen_cabeza_vertical = pygame.image.load(ruta_cabeza_vertical) #cabeza
        imagen_cabeza_vertical = pygame.transform.scale(imagen_cabeza_vertical, (escala,escala))

        imagen_cuerpo_horizontal = pygame.image.load(ruta_cuerpo_horizontal) #cabeza
        imagen_cuerpo_horizontal = pygame.transform.scale(imagen_cuerpo_horizontal, (escala,escala))

        imagen_cuerpo_vertical = pygame.image.load(ruta_cuerpo_vertical) #cabeza
        imagen_cuerpo_vertical = pygame.transform.scale(imagen_cuerpo_vertical, (escala,escala))

        imagen_curba = pygame.image.load(ruta_cuerpo_curba) #cabeza
        imagen_curba = pygame.transform.scale(imagen_curba, (escala,escala))

        imagen_manzana = pygame.image.load(ruta_manzana) #manzana
        imagen_manzana = pygame.transform.scale(imagen_manzana, (20,20))

        musica_principal = musica_principal_v
        musica_manzana = musica_manzana_v
        musica_ganar = musica_ganar_v
        musica_chocar_cuerpo = musica_chocar_cuerpo_v
        musica_pared = musica_pared_v

        musica = musica_v
        
        multiple = multiple_v

        p_principal.update()
        p_principal.deiconify()
        opciones.withdraw()
    except:
        error2()

#función para el boton salir
def salir ():
    global registro_records
    r = mb.askquestion("Salir!", "¿Seguro que quiere salir?")

    if r == "yes":
        record = open("records.dat","wb")
        pickle.dump (registro_records,record)
        record.close
        p_principal.destroy()
        opciones.destroy()
        tabla.destroy()
        acerca.destroy()
        obtener_nombre.destroy()
        pregutar.destroy()


#abrir la ventana de tabla
def m_tabla ():
    tabla.update()
    tabla.deiconify()
    p_principal.withdraw()

#abrir la ventana de aceca de
def m_acerca ():
    acerca.update()
    acerca.deiconify()
    p_principal.withdraw()

#abrir el pdf
def abrir_pdf ():
    subprocess.Popen(['Bryand_Brenes_manual_de_usuario_snake v2.pdf'],shell=True)

#cerrar la ventaana de opciones
def cerrar_opciones ():
    p_principal.update()
    p_principal.deiconify()
    opciones.withdraw()
#cerrar la ventana de tabla de calificaciones
def cerrar_tabla ():
    p_principal.update()
    p_principal.deiconify()
    tabla.withdraw()
#cerrar la ventana de acerca de
def cerrar_acerca ():
    p_principal.update()
    p_principal.deiconify()
    acerca.withdraw()

def abrir_nombre ():
    obtener_nombre.update()
    obtener_nombre.deiconify()
    pregutar.withdraw()

def preguntar_nombre ():
    pregutar.update()
    pregutar.deiconify()
    p_principal.withdraw()
    
#Funciones para abrir el seleccionador de imagenes
def imagenes_manzana():
    try:
        global ruta_manzana
        ruta_manzana = askopenfilenames()
        ruta_manzana = str(ruta_manzana[0])
    except:
        pass
def imagenes_cabezaH():
    try: 
        global ruta_cabeza_horizontal
        ruta_cabeza_horizontal = askopenfilenames()
        ruta_cabeza_horizontal = str(ruta_cabeza_horizontal[0])
    except:
        pass
def imagenes_cabezaV ():
    try:
        global ruta_cabeza_vertical
        ruta_cabeza_vertical = askopenfilenames()
        ruta_cabeza_vertical = str(ruta_cabeza_vertical[0])
    except:
        pass
def imagenes_cuerpoH ():
    try:
        global ruta_cuerpo_horizontal
        ruta_cuerpo_horizontal = askopenfilenames()
        ruta_cuerpo_horizontal = str(ruta_cuerpo_horizontal[0])
    except:
        pass
def imagenes_cuerpoV():
    try:
        global ruta_cuerpo_horizontal
        ruta_cuerpo_horizontal = askopenfilenames()
        ruta_cuerpo_horizontal = str(ruta_cuerpo_horizontal[0])
    except:
        pass
def imagenes_cuerpoC ():
    try:
        global ruta_cuerpo_curba
        ruta_cuerpo_curba = askopenfilenames()
        ruta_cuerpo_curba = str(ruta_cuerpo_curba[0])
    except:
        pass
#Funciones para elegir el seleccionador de colores
def color_Fondo ():
    try:
        global n_color_Fondo
        n_color_Fondo = askcolor()
        n_color_Fondo = n_color_Fondo[0]
    except:
        pass
def color_Paredes ():
    try:
        global n_color_Pared
        n_color_Pared = askcolor()
        n_color_Pared = n_color_Pared[0]
    except:
        pass

def s_imagen_usuario ():
    try:
        global n_imagen_usuario
        n_imagen_usuario = askopenfilenames()
        n_imagen_usuario = str(n_imagen_usuario[0])
    except:
        pass
#Función para obtener el nombre, contraseña e imagen
def nombre ():
    global r_nombre
    global contraseña
    global dicc_nombres
    global imagen_usuario, n_imagen_usuario
    global dicc_nombres
    global usuario_actual
    global contraseña_actual
    
    
    if validar_contraseña (str(textBoxContraseña.get())) == False:
        error3()
    else:
        if len(str(textBoxNombre.get()))> 50:
            error4()
        else:
            r_nombre =  str(textBoxNombre.get())            
            contraseña = str(textBoxContraseña.get())
            if r_nombre in dicc_nombres:
                error5()
            else:
                if imagen_usuario != n_imagen_usuario:
                    dicc_nombres[r_nombre]=[contraseña,n_imagen_usuario]
                    imagen_usuario = n_imagen_usuario
                    textBoxNombre.delete(0, tk.END)
                    textBoxContraseña.delete(0, tk.END)
                    dicc_nombres[r_nombre] = contraseña,n_imagen_usuario
                else:
                    dicc_nombres[r_nombre]=[contraseña,"Caudro_blanco.png"]
                    textBoxNombre.delete(0, tk.END)
                    textBoxContraseña.delete(0, tk.END)
                    dicc_nombres[r_nombre] = contraseña,"Caudro_blanco.png"
                contraseña_actual = contraseña
                usuario_actual = r_nombre
                perfiles = open("usuarios.dat","wb")
                pickle.dump (dicc_nombres,perfiles)
                perfiles.close    
                obtener_nombre.withdraw()
                juego()

def imagenes_cuerpoC ():
    try:
        global ruta_cuerpo_curba
        ruta_cuerpo_curba = askopenfilenames()
        ruta_cuerpo_curba = str(ruta_cuerpo_curba[0])
    except:
        pass

#Funciones para seleccionar la música
def con_musica ():
    global musica_v
    musica_v = True

def sin_musica ():
    global musica_v
    musica_v = False

def musica_juego ():
    try:
        global musica_principal_v
        musica_principal_v = askopenfilenames()
        musica_principal_v = str(musica_principal_v[0])
    except:
        pass
def selecc_manzana ():
    try:
        global musica_manzana_v
        musica_manzana_v = askopenfilenames()
        musica_manzana_v = str(musica_manzana_v[0])
    except:
        pass
def selecc_ganar ():
    try:
        global  musica_ganar_v
        musica_ganar_v = askopenfilenames()
        musica_ganar_v = str(musica_ganar_v[0])
    except:
        pass
def selecc_cuerpo ():
    try:
        global musica_chocar_cuerpo_v
        musica_chocar_cuerpo_v = askopenfilenames()
        musica_chocar_cuerpo_v = str(musica_chocar_cuerpo_v[0])
    except:
        pass
def selecc_pared ():
    try:
        global musica_pared_v
        musica_pared_v = askopenfilenames()
        musica_pared_v = str(musica_pared_v[0])
    except:
        pass

#Funcion para validar la contraseña   
def validar_contraseña (contraseña):
    if len (contraseña) < 8:
        return False
    condicion1 = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    condicion2 = ("abcdefghijklmnñopqrstuvwxyz")
    condicion3 = ("1234567890")

    return validar_contraseña_aux (contraseña,condicion1,condicion2,condicion3,0,0,0,0)

def validar_contraseña_aux (contraseña,condicion1,condicion2,condicion3,c1,c2,c3,c4):
    if contraseña == "":
        if c1 == 0:
            return False
        elif c2 == 0:
            return False
        elif c3 == 0:
            return False
        elif c4 == 0:
            return False
        return True
    else:        
        if contraseña.count(contraseña[0])>2:
            return False
        contraseña[0]
        if contraseña[0] in condicion1:
            c1 += 1
        elif contraseña[0] in condicion2:
            c2 += 1
        elif contraseña[0] in condicion3:
            c3 += 1
        else:
            c4 += 1
        return validar_contraseña_aux (contraseña[1:],condicion1,condicion2,condicion3,c1,c2,c3,c4)


def selecc_usuario ():
    global dicc_nombres
    global usuario_actual
    global imagen_usuario
    global contraseña_actual
    pregutar.withdraw()
    if dicc_nombres == {}:
        error6()
    else:
        root = Tk()
        iList = Listbox(root, justify = CENTER)
        scroll = Scrollbar(root, command = iList.yview)
        iList.configure(yscrollcommand = scroll.set)
        iList.pack(side = LEFT)
        scroll.pack(side = RIGHT, fill = Y)
        
        for x in dicc_nombres:
            iList.insert(END,x)


        E1 = Entry(root, bd =5, show = "*")
        E1.pack()
        def verificar_contraseña ():
            global dicc_nombres
            global usuario_actual
            global imagen_usuario
            global contraseña_actual
            try:
                contraseña = E1.get()                
                x = iList.curselection()
                i = (x[0])
                if (dicc_nombres[iList.get(i)][0]) == contraseña:
                    contraseña_actual = dicc_nombres[iList.get(i)][0]                    
                    imagen_usuario = dicc_nombres[iList.get(i)][1]
                    usuario_actual = iList.get(i)
                    
                    root.withdraw()
                    root.destroy() 
                    juego()
                                       
                else:
                    error7()
            except:
                error8()


        def display():
            try:
                x = iList.curselection()
                i = (x[0])
                print(dicc_nombres[iList.get(i)][0])
            except:
                error8()

        B1 = Button(root, text = "Verificar contraseña", command = verificar_contraseña)
        B1.pack(side=LEFT)

        B2 = Button(root, text =  "display", command = display)
        #B2.pack(side = RIGHT)
        root.mainloop()

#Función para multiple nivel
def multi_nivel ():
    opciones_multiple = tkinter.Tk()
    #opciones_multiple.withdraw()
    opciones_multiple.title("Opciones del Multiple")
    opciones_multiple.configure(bg = "#1E5F7C")
    opciones_multiple.geometry("300x150")

    #Funcion del boton de cerrar
    def cerrar_multi():
        global glob_serp
        global rand1,rand2
        global g_derecha,g_izquierda,g_arriba,g_abajo
        global p_cuerpo, p_paredes
        global musica_chocar_cuerpo, musica_pared
        global puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20
        global ancho, altura
        global minutos, horas, segundos, c
        ancho = 14
        altura = 14
        puntuacion_14 = 0
        puntuacion_16 = 0
        puntuacion_18 = 0
        puntuacion_20 = 0            

        g_derecha,g_izquierda,g_arriba,g_abajo = True,False,False,False
        
        rand1,rand2 = 10, 10
        glob_serp =[[1,3],[1,2],[1,1],[1,0]]
        minutos = 0
        horas = 0
        segundos = 0
        c = 0
        opciones_multiple.withdraw()
        opciones_multiple.destroy()
        p_principal.update()
        p_principal.deiconify()
        
    global glob_serp
    global rand1,rand2
    global g_derecha,g_izquierda,g_arriba,g_abajo
    global p_cuerpo, p_paredes
    global musica_chocar_cuerpo, musica_pared
    global puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20
    global ancho, altura #Tamño del juego  

    #Función de pasar al nivel anterior    
    def nivel_anterior ():
        global glob_serp
        global rand1,rand2
        global g_derecha,g_izquierda,g_arriba,g_abajo
        global p_cuerpo, p_paredes
        global musica_chocar_cuerpo, musica_pared
        global puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20
        global ancho, altura
        
        ancho -= 2
        altura -= 2     
        g_derecha,g_izquierda,g_arriba,g_abajo = True,False,False,False
        rand1,rand2 = 10, 10
        glob_serp =[[1,3],[1,2],[1,1],[1,0]]
        opciones_multiple.withdraw()
        opciones_multiple.destroy()
        juego()
    #Función de pasar al siguiente nivel  
    def siguiente_nivel ():
        global glob_serp
        global rand1,rand2
        global g_derecha,g_izquierda,g_arriba,g_abajo
        global p_cuerpo, p_paredes
        global musica_chocar_cuerpo, musica_pared
        global puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20
        global ancho, altura
        ancho += 2
        altura += 2     
        g_derecha,g_izquierda,g_arriba,g_abajo = True,False,False,False
        rand1,rand2 = 10, 10
        glob_serp =[[1,3],[1,2],[1,1],[1,0]]
        opciones_multiple.withdraw()
        opciones_multiple.destroy()
        juego()
    #Función de quedarse en el nivel actual 
    def nivel_actual ():
        global glob_serp
        global rand1,rand2
        global g_derecha,g_izquierda,g_arriba,g_abajo
        global p_cuerpo, p_paredes
        global musica_chocar_cuerpo, musica_pared
        global puntuacion_14,puntuacion_16,puntuacion_18,puntuacion_20
        global ancho, altura
        g_derecha,g_izquierda,g_arriba,g_abajo = True,False,False,False
        rand1,rand2 = 10, 10
        glob_serp =[[1,3],[1,2],[1,1],[1,0]]
        opciones_multiple.withdraw()
        opciones_multiple.destroy()
        juego()
        
    buttonAtras = Button(opciones_multiple, text = "Nivel Anterior", activebackground = "#660076", fg = "#919496", bg = "#660076"
                         , font = ("Consola", 14), width = 10, heigh = 1,state = "normal", command = nivel_anterior)
    buttonAtras.place(x=15, y = 15)

    buttonContinuar = Button(opciones_multiple, text = "Nivel Actual", activebackground = "#660076", fg = "#919496", bg = "#660076"
                         , font = ("Consola", 14), width = 10, heigh = 1, command = nivel_actual)
    buttonContinuar.place(x=150, y = 15)

    buttonSiguiente = Button(opciones_multiple, text = "Siguiente Nivel", activebackground = "#660076", fg = "#919496", bg = "#660076"
                         , font = ("Consola", 14), width = 12, heigh = 1,state = "normal", command = siguiente_nivel)
    buttonSiguiente.place(x=15, y = 80)

    buttonSalirJuego = Button(opciones_multiple, text = "Salir", activebackground = "#660076", fg = "#919496", bg = "#660076"
                         , font = ("Consola", 14), width = 10, heigh = 1, command = cerrar_multi)
    buttonSalirJuego.place(x=170, y = 80)

    if ancho == 14:
        puntuacion_14 = len(glob_serp)-4
        buttonAtras.config(state = "disable")
    elif ancho == 16:
        puntuacion_16 = len(glob_serp)-4
        buttonSiguiente.config(state = "normal")
        buttonAtras.config(state = "normal")
    elif ancho == 18:
        puntuacion_18 = len(glob_serp)-4
        buttonSiguiente.config(state = "normal")
        buttonAtras.config(state = "normal")
    elif ancho == 20:
        puntuacion_20 = len(glob_serp)-4
        buttonSiguiente.config(state = "disable")
        
    if p_cuerpo:
        if musica:
                pygame.mixer.music.load(musica_chocar_cuerpo)
                pygame.mixer.music.play()
    elif p_paredes:
        if musica:
                pygame.mixer.music.load(musica_pared)
                pygame.mixer.music.play()
#Función para cargar la partida de multiples usuarios
def selecc_usuario_cargar ():
    global dicc_nombres
    global usuario_actual
    global imagen_usuario
    global contraseña_actual
    p_principal.withdraw()
    if dicc_nombres == {}:
        error6()
    else:
        root = Tk()
        iList = Listbox(root, justify = CENTER)
        scroll = Scrollbar(root, command = iList.yview)
        iList.configure(yscrollcommand = scroll.set)
        iList.pack(side = LEFT)
        scroll.pack(side = RIGHT, fill = Y)
        
        for x in dicc_nombres:
            iList.insert(END,x)


        E1 = Entry(root, bd =5, show = "*")
        E1.pack()
        def verificar_contraseña ():
            global dicc_nombres
            global usuario_actual
            global imagen_usuario
            global contraseña_actual
            try:
                contraseña = E1.get()                
                x = iList.curselection()            
                i = (x[0])
                if (dicc_nombres[iList.get(i)][0]) == contraseña:
                    contraseña_actual = dicc_nombres[iList.get(i)][0]                    
                    imagen_usuario = dicc_nombres[iList.get(i)][1]
                    usuario_actual = iList.get(i)
                    
                    root.withdraw()
                    root.destroy() 
                    cargar_partida()
                                       
                else:
                    error7()
            except:
                error8()


        def display():
            try:
                x = iList.curselection()
                i = (x[0])
                print(dicc_nombres[iList.get(i)][0])
            except:
                error8()

        B1 = Button(root, text = "Verificar contraseña", command = verificar_contraseña)
        B1.pack(side=LEFT)

        B2 = Button(root, text =  "display", command = display)
        #B2.pack(side = RIGHT)
        root.mainloop()

#Ventanas

p_principal = tkinter.Tk()
#p_principal.withdraw()
p_principal.title("Ventana Principal")
p_principal.configure(bg = "#1E5F7C")
p_principal.geometry("1360x768")

#Opciones
opciones = tkinter.Tk()
opciones.withdraw()
opciones.title("Opciones de Configuración")
opciones.configure(bg = "#1E5F7C")
opciones.geometry("1360x768")

#tabla de calificaciones
tabla = tkinter.Tk()
tabla.withdraw()
tabla.title("Tabla de calificaciones")
tabla.configure(bg = "#1E5F7C")
tabla.geometry("1360x768")

#acerca de
acerca = tkinter.Tk()
acerca.withdraw()
acerca.title("Acerca de")
acerca.configure(bg = "#1E5F7C")
acerca.geometry("1360x768")

#obtener nombre
obtener_nombre = tkinter.Tk()
obtener_nombre.withdraw()
obtener_nombre.title("Crear Usuario")
obtener_nombre.configure(bg = "#1E5F7C")
obtener_nombre.geometry("300x300")

##########
pregutar = Tk()
pregutar.withdraw()
pregutar.title("Crear Usuario ó Utilizar uno ya craedo")
pregutar.configure(bg = "#1E5F7C")
pregutar.geometry("300x300")

#Imagenes

fondo = Image.open ("snake_game.jpg")
fondo = fondo.resize((1360,768), Image.ANTIALIAS)
fondo = ImageTk.PhotoImage (fondo)
fondo_Label = Label(p_principal, image= fondo)
fondo_Label.place (x=0, y = 0)

#Text box

#Text box nombre
textBoxNombre = Entry(obtener_nombre, width = 10, font = ("Consola", 20))
textBoxNombre.place (x=15, y= 60)

textBoxContraseña = Entry(obtener_nombre, width = 10, font = ("Consola", 20), show = "*")
textBoxContraseña.place (x=15, y= 125)


#Botones

#Menú
buttonJugar = Button(p_principal, text = "Jugar", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = preguntar_nombre) #juego
buttonJugar.place(x=525, y = 20)

buttonContinuar = Button(p_principal, text = "Continuar juego", activebackground = "#660076", fg = "#919496", bg = "#660076"
                         , font = ("Consola", 20), width = 21, heigh = 1,command = selecc_usuario_cargar)
buttonContinuar.place(x=525, y = 100)

buttonOpciones = Button(p_principal, text = "Opciones de Configuración", activebackground = "#660076", fg = "#919496", bg = "#660076"
                        , font = ("Consola", 20), width = 21, heigh = 1,command = m_opciones)
buttonOpciones.place(x=525, y = 180)

buttonTabla = Button(p_principal, text = "Tabla de calificaciones", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1,command = m_tabla)
buttonTabla.place(x=525, y = 260)

buttonAyuda = Button(p_principal, text = "Ayuda", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = abrir_pdf)
buttonAyuda.place(x=525, y = 340)

buttonAcerca = Button(p_principal, text = "Acerca de", activebackground = "#660076", fg = "#919496", bg = "#660076"
                      , font = ("Consola", 20), width = 21, heigh = 1,command = m_acerca)
buttonAcerca.place(x=525, y = 420)

buttonSalir = Button(p_principal, text = "Salir", activebackground = "#660076", fg = "#919496"
                     , bg = "#660076", font = ("Consola", 20), width = 21, heigh = 1,command = salir)
buttonSalir.place(x=525, y = 500)

buttonOKOpciones =  Button(opciones, text = "OK", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = ok_opciones)
buttonOKOpciones.place(x=550, y = 665)

buttonCancelarOpciones =  Button(opciones, text = "Cancelar", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = cerrar_opciones)
buttonCancelarOpciones.place(x=700, y = 665)

buttonCancelarTabla =  Button(tabla, text = "Atrás", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = cerrar_tabla)
buttonCancelarTabla.place(x=600, y = 665)

buttonCancelarAcerca =  Button(acerca, text = "Atrás", activebackground = "white", fg = "black", bg = "white",
                               font = ("Serif", 14), width = 8, heigh = 1, command = cerrar_acerca)
buttonCancelarAcerca.place(x=600, y = 665)

#Escribir nombre

buttonNombreOK= Button(obtener_nombre, text = "OK", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 16), width = 3, heigh = 1, command = nombre)
buttonNombreOK.place(x=15, y = 250)

buttonNombreImagen= Button(obtener_nombre, text = "Elegir la imagen", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 16), width = 13, heigh = 1, command = s_imagen_usuario)
buttonNombreImagen.place(x=15, y = 180)
#Configuraciones
buttonManzana = Button(opciones, text = "Imagen de la manzana", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = imagenes_manzana)
buttonManzana.place(x=525, y = 20)

buttonCabezaHorizontal = Button(opciones, text = "Imagen Cabeza Horizontal ", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = imagenes_cabezaH)
buttonCabezaHorizontal.place(x=525, y = 80)

buttonCabezaVertical = Button(opciones, text = "Imagen Cabeza Vertical", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = imagenes_cabezaV)
buttonCabezaVertical.place(x=525, y = 140)

buttonCuerpoHorizontal = Button(opciones, text = "Imagen Cuerpo Horizontal", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = imagenes_cuerpoH)
buttonCuerpoHorizontal.place(x=525, y = 200)

buttonCuerpoVertical = Button(opciones, text = "Imagen Cuerpo Vertical", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = imagenes_cuerpoV)
buttonCuerpoVertical.place(x=525, y = 260)

buttonCuerpoCurba = Button(opciones, text = "Imagen Curba", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = imagenes_cuerpoC)
buttonCuerpoCurba.place(x=525, y = 320)

buttonColorFondo = Button(opciones, text = "Color Fondo", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = color_Fondo)
buttonColorFondo.place(x=525, y = 380)

buttonColorParedes = Button(opciones, text = "Color Paredes", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = color_Paredes)
buttonColorParedes.place(x=525, y = 440)

buttonMusicaJuego = Button(opciones, text = "Música durante el juego", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = musica_juego)
buttonMusicaJuego.place(x=925, y = 20)

buttonMusicaManzana = Button(opciones, text = "Sonido comer manzana", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = selecc_manzana)
buttonMusicaManzana.place(x=925, y = 80)

buttonMusicaGanar = Button(opciones, text = "Sonido ganar", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = selecc_ganar)
buttonMusicaGanar.place(x=925, y = 140)

buttonMusicaCuerpo = Button(opciones, text = "Chocar con cuerpo", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = selecc_cuerpo)
buttonMusicaCuerpo.place(x=925, y = 200)

buttonMusicaPared = Button(opciones, text = "Chocar con pared", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 20), width = 21, heigh = 1, command = selecc_pared)
buttonMusicaPared.place(x=925, y = 260)

#pregutar

buttonCraerUsuario = Button(pregutar, text = "Crear nuevo Usuario", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 18), width = 18, heigh = 1, command = abrir_nombre)
buttonCraerUsuario.place(x=15, y = 50)

buttonSeleccionarUsuario = Button(pregutar, text = "Seleccionar Usuario", activebackground = "#660076", fg = "#919496", bg = "#660076"
                     , font = ("Consola", 18), width = 18, heigh = 1, command = selecc_usuario)
buttonSeleccionarUsuario.place(x=15, y = 150)




#label

#Tabla de calidicaciones

labelTabla = Label(tabla, text = "Tabla de calificaciones", font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelTabla.place(x = 525, y = 15)

labelTamañoTabla = Label(tabla, text = "Tamaño", font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelTamañoTabla.place(x = 30, y = 15)

labelModoTabla = Label(tabla, text = "Modo", font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelModoTabla.place(x = 30, y = 215)

labelParametros = Label(tabla, text = "Pocición".center(16) + "|" +  "Nombre".center(16) + "|" +
                    "Puntuación".center(16) + "|" +"Tiempo" .center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelParametros.place(x = 300, y = 80)

labelPrimero = Label(tabla, text = "1.".center(20) + "|" +  registro_records[0][0][0].center(16) + "|" +
                    str(len(registro_records[0][0][1])).center(22) + "|" +
                    (str(registro_records[0][0][2][0]) + " : " + str(registro_records[0][0][2][1]) + " : "
                    + str(registro_records[0][0][2][2])).center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelPrimero.place(x = 300, y = 120)

labelSegundo = Label(tabla, text = "2.".center(20) + "|" +  registro_records[0][1][0].center(16) + "|" +
                    str(len(registro_records[0][1][1])).center(22) + "|" +
                    (str(registro_records[0][1][2][0]) + " : " + str(registro_records[0][1][2][1]) + " : "
                    + str(registro_records[0][1][2][2])).center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelSegundo.place(x = 300, y = 160)

labelTercero = Label(tabla, text = "3.".center(20) + "|" +  registro_records[0][2][0].center(16) + "|" +
                    str(len(registro_records[0][2][1])).center(22) + "|" +
                    (str(registro_records[0][2][2][0]) + " : " + str(registro_records[0][2][2][1]) + " : "
                    + str(registro_records[0][2][2][2])).center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelTercero.place(x = 300, y = 200)

labelCuarto = Label(tabla, text = "4.".center(20) + "|" +  registro_records[0][3][0].center(16) + "|" +
                    str(len(registro_records[0][3][1])).center(22) + "|" +
                    (str(registro_records[0][3][2][0]) + " : " + str(registro_records[0][3][2][1]) + " : "
                    + str(registro_records[0][3][2][2])).center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelCuarto.place(x = 300, y = 240)

labelQuinto = Label(tabla, text = "5.".center(20) + "|" +  registro_records[0][4][0].center(16) + "|" +
                    str(len(registro_records[0][4][1])).center(22) + "|" +
                    (str(registro_records[0][4][2][0]) + " : " + str(registro_records[0][4][2][1]) + " : "
                    + str(registro_records[0][4][2][2])).center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelQuinto.place(x = 300, y = 280)

labelSexto = Label(tabla, text = "6.".center(20) + "|" +  registro_records[0][5][0].center(16) + "|" +
                    str(len(registro_records[0][5][1])).center(22) + "|" +
                    (str(registro_records[0][5][2][0]) + " : " + str(registro_records[0][5][2][1]) + " : "
                    + str(registro_records[0][5][2][2])).center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelSexto.place(x = 300, y = 320)

labelSeptimo = Label(tabla, text = "7.".center(20) + "|" +  registro_records[0][6][0].center(16) + "|" +
                    str(len(registro_records[0][6][1])).center(22) + "|" +
                    (str(registro_records[0][6][2][0]) + " : " + str(registro_records[0][6][2][1]) + " : "
                    + str(registro_records[0][6][2][2])).center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelSeptimo.place(x = 300, y = 360)

labelOctavo = Label(tabla, text = "8.".center(20) + "|" +  registro_records[0][7][0].center(16) + "|" +
                    str(len(registro_records[0][7][1])).center(22) + "|" +
                    (str(registro_records[0][7][2][0]) + " : " + str(registro_records[0][7][2][1]) + " : "
                    + str(registro_records[0][7][2][2])).center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelOctavo.place(x = 300, y = 400)

labelNoveno = Label(tabla, text = "9.".center(20) + "|" +  registro_records[0][8][0].center(16) + "|" +
                    str(len(registro_records[0][8][1])).center(22) + "|" +
                    (str(registro_records[0][8][2][0]) + " : " + str(registro_records[0][8][2][1]) + " : "
                    + str(registro_records[0][8][2][2])).center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelNoveno.place(x = 300, y = 440)

labelDecimo = Label(tabla, text = "10.".center(19) + "|" +  registro_records[0][9][0].center(16) + "|" +
                    str(len(registro_records[0][9][1])).center(22) + "|" +
                    (str(registro_records[0][9][2][0]) + " : " + str(registro_records[0][9][2][1]) + " : "
                    + str(registro_records[0][9][2][2])).center(16),
                    font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelDecimo.place(x = 300, y = 480)

#Nombre
labelNombre = Label(obtener_nombre, text = "Escriba su nombre", font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelNombre.place(x = 15, y = 15)

labelContraseña = Label(obtener_nombre, text = "Escriba su contraseña", font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelContraseña.place(x = 15, y = 90)


#Opciones

labelTamaño = Label(opciones, text = "Tamaño", font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelTamaño.place(x = 30, y = 15)

labelModo = Label(opciones, text = "Modo", font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelModo.place(x = 30, y = 215)

labelMusica = Label(opciones, text = "Musica", font = ("Consola", 20), bg = "#1E5F7C", fg = "white")
labelMusica.place(x = 30, y = 365)

#Acerca de

labelParqueo = Label (acerca, text = "Snake v2", fg = "white", font = ("Consola", 20))
labelParqueo .place (x=10, y= 15)
labelParqueo .configure(bg = "#1E5F7C")

labelVersion = Label (acerca, text = "Versión: 1.9", fg = "white", font = ("Consola", 20))
labelVersion .place (x=10, y= 50)
labelVersion .configure(bg = "#1E5F7C")

labelV_Fecha = Label (acerca, text = "Fecha del último cambio: 05-06-2019", fg = "white", font = ("Consola", 20))
labelV_Fecha .place (x=10, y= 85)
labelV_Fecha .configure(bg = "#1E5F7C")

labelCreador = Label (acerca, text = "Creador:   Bryand Brenes Zúñiga", fg = "white", font = ("Consola", 20))
labelCreador .place (x=10, y= 120)
labelCreador .configure(bg = "#1E5F7C")


#Botones radiobutton

#Configuracion
radiobuttonTamaño1 = Radiobutton(opciones, text = "14x14", font = ("Consola", 18), value = 1, variable = 1,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C", command = tamaño_14  )
radiobuttonTamaño1.place(x = 15, y = 75)

radiobuttonTamaño2 = Radiobutton(opciones, text = "16x16", font = ("Consola", 18), value = 2, variable = 1,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C", command = tamaño_16  )
radiobuttonTamaño2.place(x = 15, y = 105)

radiobuttonTamañoMultiple = Radiobutton(opciones, text = "Multiple", font = ("Consola", 18), value = 5, variable = 1,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C", command = ac_multiple  )
radiobuttonTamañoMultiple.place(x = 130, y = 115)

radiobuttonTamaño3 = Radiobutton(opciones, text = "18x18", font = ("Consola", 18), value = 3, variable = 1,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C", command = tamaño_18  )
radiobuttonTamaño3.place(x = 15, y = 135)


radiobuttonTamaño4 = Radiobutton(opciones, text = "20x20", font = ("Consola", 18), value = 4, variable = 1,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C", command = tamaño_20  )
radiobuttonTamaño4.place(x = 15, y = 165)

radiobuttonConParedes = Radiobutton(opciones, text = "Con Paredes", font = ("Consola", 18), value = 1, variable = 2,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C", command = con_paredes)
radiobuttonConParedes.place(x = 15, y = 275)

radiobuttonSinParedes = Radiobutton(opciones, text = "Sin Paredes", font = ("Consola", 18), value = 2, variable = 2,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C", command = sin_paredes)
radiobuttonSinParedes.place(x = 15, y = 305)

radiobuttonConMusica = Radiobutton(opciones, text = "Con Música", font = ("Consola", 18), value = 1, variable = 3,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C", command = con_musica)
radiobuttonConMusica.place(x = 15, y = 415)

radiobuttonSinMusica = Radiobutton(opciones, text = "Sin Música", font = ("Consola", 18), value = 2, variable = 3,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C", command = sin_musica)
radiobuttonSinMusica.place(x = 15, y = 445)

#Tabla
radiobuttonTamaño1Tabla = Radiobutton(tabla, text = "14x14", font = ("Consola", 18), value = 1, variable = 1,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C")
radiobuttonTamaño1Tabla.place(x = 15, y = 75)

radiobuttonTamaño2Tabla = Radiobutton(tabla, text = "16x16", font = ("Consola", 18), value = 2, variable = 1,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C")
radiobuttonTamaño2Tabla.place(x = 15, y = 105)


radiobuttonTamaño3Tabla = Radiobutton(tabla, text = "18x18", font = ("Consola", 18), value = 3, variable = 1,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C")
radiobuttonTamaño3Tabla.place(x = 15, y = 135)


radiobuttonTamaño3Tabla = Radiobutton(tabla, text = "20x20", font = ("Consola", 18), value = 4, variable = 1,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C")
radiobuttonTamaño3Tabla.place(x = 15, y = 165)

radiobuttonConParedesTabla = Radiobutton(tabla, text = "Con Paredes", font = ("Consola", 18), value = 1, variable = 2,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C")
radiobuttonConParedesTabla.place(x = 15, y = 275)

radiobuttonSinParedesTabla = Radiobutton(tabla, text = "Sin Paredes", font = ("Consola", 18), value = 2, variable = 2,
                                 bg = "#1E5F7C", activebackground = "#1E5F7C")
radiobuttonSinParedesTabla.place(x = 15, y = 305)

p_principal.mainloop()
