## X es el cliente y se debe meter con el formato: "Nombre"
## Y Tipo de fumigación
## Z Cantidad de hectareas
def Fumigacion ( X , Y , Z):
    if Y  == 1:
        X = X
        Z = Z * 3000
        if Z > 500:
            Z == Z * 0.95
        if Z > 300000:
            T = Z - 300000
            T = T * 0.90
            Z = T + 300000
        return print (" El monto del cliente " +X+   " es de " +str( Z) + " por la fumigacion de tipo "+ str( Y))
        
    elif Y == 2:
         X = X
         Z = Z * 6000
         if  Z > 500:
             Z == Z * 0.95
         if Z > 300000:
             T = Z - 300000
             T = T * 0.90
             Z = T + 300000
         return print(" El monto del cliente " +X+ " es de "+ str (Z)+ " por la fumigacion de tipo " +str(Y))

    elif Y == 3:
        X = X
        Z = Z * 9000
    if Z > 500:
        Z == Z * 0.95
    if Z > 300000:
        T = Z - 300000
        T = T * 0.90
        Z = T + 300000
    return print(" El monto del cliente "+X+ " es de " + str (Z)+ " por la fumigacion de tipo " +str(Y))

    if Y == 4:
        X = X
        Z = Z * 16000
    if Z > 500:
        Z == Z * 0.95
    if Z > 300000:
        T = Z - 300000
        T = T * 0.90
        Z = T + 300000
    return print(" El monto del cliente "+X+ " es de " + str (Z)+ " por la fumigacion de tipo " +str(Y))
        
Fumigacion("Ricardo", 4,640000)

    
        
    
