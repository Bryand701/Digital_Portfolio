# Función para calcular la hora de entrada
import time

def hora_actual():
    hora = time.strftime("%H:%M") + "-" +  time.strftime("%d/%m/%y")
    return hora
