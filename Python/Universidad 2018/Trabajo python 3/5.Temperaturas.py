"""
La temperatura minima que se utilizara es de 5°
y la maxima es de 18°
"""
import random
def tempe ():
    temp = []
    veces = []
    tomadas= []
    final = []
    x=0
    j =0
    while x in range (20):
        x += 1
        k=random.randint(5, 18)
        tomadas.append (k)
        if k<13 :
            temp. append(k)
            j +=1
    veces.append (j)
    final.append (tomadas)
    final.append (veces)
    final.append (temp)
    return final
def resultados ():
    
    datos= tempe()
    print ("Las temperaturas tomadas en grados fueron: ")
    print (datos[0])
    print ("Las veces que la temperatura fue inferior a 13° fueron:")
    print (datos[1])
    print ("Las temperaturas inferiores a 13° fueron:")
    print (datos[2])
resultados()
