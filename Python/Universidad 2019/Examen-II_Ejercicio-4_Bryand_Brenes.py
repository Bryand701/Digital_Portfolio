"""
Ejercicio 4
Bryand Brenes Zúñiga
2018093347
"""

"""
La función revise cuatro variables
El primero es "busqueda" es la palabra que hay que buscar (valga la redondancia)
en la variable "analizado" que es una oración
Remplazo es la palabra con la que hay que remplazar (valga la redondancia) la palabra de "busqueda"
y cantidad es la cantidad de veces que hay que remplazar la palabra, si es cero se remplaza siempre,
si es un número positivo se remplaza esa cantidad de veces de izquierda a derecha
y si es negativo se remplaza esa cantidad de veces pero analizando la variable "analizado"
de derecha a izquierda
"""
def reemplazar (busqueda, analizado, reemplazo, cantidad):
    espacio = " "
    analizar = analizado.split()
    lista = []
    if cantidad == 0:
        for x in analizar:
            if x != busqueda:
                lista.append(x)
            else:
                lista.append(reemplazo)
        return espacio.join(lista)
    elif cantidad > 0:

        for x in analizar:
            if x != busqueda:
                lista.append(x)
            elif cantidad > 0:
                lista.append(reemplazo)
                cantidad -= 1
            else:
                lista.append(x)
                    
        return espacio.join(lista)

    else:
        analizar.reverse()
        cantidad = abs(cantidad)
        
        for x in analizar:
           if x != busqueda:
               lista.append(x)
           elif cantidad > 0:
               lista.append(reemplazo)
               cantidad -= 1
           else:
               lista.append(x)
        lista.reverse()           
        return espacio.join(lista)


        
