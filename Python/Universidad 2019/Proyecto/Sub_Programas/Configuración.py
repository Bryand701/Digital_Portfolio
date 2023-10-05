#Configuración

def config ():

    global espacios,l_esoacios, p_h, p_m, re, m_m, m_1, m_2, m_3, b_1, b_2, b_3, b_4, b_5

    espacios = 0
    l_espacios = []
    p_h = 0
    p_m = 0
    re = 0
    m_m = 0
    m_1 = 0
    m_2 = 0
    m_3 = 0
    b_1 = 0
    b_2 = 0
    b_3 = 0
    b_4 = 0
    b_5 = 0
    
    
    while True:

        espacios = int (input("Cantidad de espacios en el parqueo "))

        for x in range(espacios):
            l_espacios.append([])
        espacios = int (input("Cantidad de espacios en el parqueo "))
        p_h = int (input("Precio por hora "))
        p_m = int (input("Pago mínimo "))
        re = int (input("Redondear el cobro a los siguientes minutos "))
        m_m = int (input("Minutos máximos para salir después del pago "))
        m_1 = int (input("Moneda 1, la de menor denominación "))
        m_2 = int (input("Moneda 2, denominación siguiente a la anterior "))
        m_3 = int (input("Moneda 3, denominación siguiente a la anterior "))
        b_1 = int (input("Billete 1, el de menor denominación "))
        b_2 = int (input("Billete 2, denominación siguiente a la anterior "))
        b_3 = int (input("Billete 3, denominación siguiente a la anterior "))
        b_4 = int (input("Billete 4, denominación siguiente a la anterior "))
        b_5 = int (input("Billete 5, denominación siguiente a la anterior "))

        if espacios >= 1 and p_h >=0 and p_m >=0 and 0 <= re <= 60 and m_m >=0:
            if m_1 < m_2 < m_3:
                if b_1 < b_2 < b_3 < b_4 < b_5:
                    break
        
