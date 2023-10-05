## A es la cantidad de ventas
## B monto vendido
## C es la cantidad de ventas del 2do mes
## D monto vendido en el segundo mes
def NivelA ( A , B , C, D):
    Z = 150000/2
    E = 150000 + ( B * 0.08)
    L = 150000 + ( D * 0.08)

    if A >= 3 and C >= 3:
        return print (" Su sueldo del primer mes es de", int (E) ,"y su sueldo del segundo mes es de" , int (L))
    
            
    elif A >= 3 and C < 3:
        return print(" Su sueldo del primer mes es de",int (E) ,"y fueron menos de 3 ventas en el segundo mes entonces su sueldo es de", int (Z))

    elif A < 3 and C >= 3:
        return print (" Fueron menos de 3 ventas en el primer mes entonces su sueldo es de ", int (Z) ,"y su sueldo del segundo mes es de" , int (L))
            
    else:
        return print("Fueron menos de 3 ventas en el primer mes entonces su sueldo es de", int(Z) ,"y fueron menos de 3 ventas en el segundo mes entonces su sueldo es de", int (Z) , "y es despedido")
         
def NivelB ( A , B , C, D):
    Z = 210000/2
    E = 210000 + ( B * 0.08)
    L = 210000 + ( D * 0.08)

    if A >= 3 and C >= 3:
        return print( " Su sueldo del primer mes es de", int (E) ,"y su sueldo del segundo mes es de" , int (L))
    
            
    elif A >= 3 and C < 3:
        return print (" Su sueldo del primer mes es de", int (E) ,"y fueron menos de 3 ventas en el segundo mes entonces su sueldo es de", int (Z))

    elif A < 3 and C >= 3:
        return print(" Fueron menos de 3 ventas en el primer mes entonces su sueldo es de ", int (Z) ,"y su sueldo del segundo mes es de" , int (L))
    else:
        return print(" Fueron menos de 3 ventas en el primer mes entonces su sueldo es de", int (Z) ,"y fueron menos de 3 ventas en el segundo mes entonces su sueldo es de", int (Z), "y es despedido")
def NivelC ( A , B , C, D):
    Z = 275000/2
    E = 275000 + ( B * 0.08)
    L = 275000 + ( D * 0.08)

    if A >= 3 and C >= 3:
        return print (" Su sueldo del primer mes es de", int (E) ,"y su sueldo del segundo mes es de" , int (L))
    
            
    elif A >= 3 and C < 3:
        return print (" Su sueldo del primer mes es de", int (E) ,"y fueron menos de 3 ventas en el segundo mes entonces su sueldo es de", int (Z))

    elif A < 3 and C >= 3:
        return print (" Fueron menos de 3 ventas en el primer mes entonces su sueldo es de ", int (Z) ,"y su sueldo del segundo mes es de" , int (L))
            
    else:
        return print(" Fueron menos de 3 ventas en el primer mes entonces su sueldo es de", int (Z) ,"y fueron menos de 3 ventas en el segundo mes entonces su sueldo es de", int (Z), "y es despedido")


