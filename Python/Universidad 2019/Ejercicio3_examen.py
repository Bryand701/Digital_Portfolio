"""
Bryand Brenes Zúñiga
2018093347
"""


"""
Función para contar los digitos de un número
"""

def digitos (n):

    c = 0

    if n == 0: 
        c = 1 
    
    while n != 0:
        n = n //10
        c += 1

    return c

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
