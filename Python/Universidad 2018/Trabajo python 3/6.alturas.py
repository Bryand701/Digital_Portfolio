import random
def alturas ():
    a=[]
    b=[]
    c=[]
    d=[]
    for x in range (500):
        i=random.randint(120, 220)
        if i<=160:
            i = i/100
            a.append(i)
        elif i<=170:
            i = i/100
            b.append(i)
        elif i<=180:
            i = i/100
            c.append(i)
        else:
            i = i/100
            d.append(i)
    final=(a,b,c,d)
    return final
"""
Para imprimir alturas ultilizar:
imp_alturas(alturas ())
"""
def imp_alturas ():
    final=alturas()
    a = final[0]
    b = final[1]
    c = final[2]
    d = final[3]
    print ("Las alturas hasta un metro sesenta centímetros son:")
    print (a)
    print ("La cantidad de personas en este rango son :", len(a))
    print ("Las alturas entre un metro sesenta y un metro setenta son:")
    print (b)
    print ("La cantidad de personas en este rango son :", len(b))
    print ("Las alturas entre un metro setenta y un metro ochenta son:")
    print (c)
    print ("La cantidad de personas en este rango son :", len(c))
    print ("Las alturas mayores a un metro ochenta son:")
    print (d)
    print ("La cantidad de personas en este rango son :", len(d))
imp_alturas ()
