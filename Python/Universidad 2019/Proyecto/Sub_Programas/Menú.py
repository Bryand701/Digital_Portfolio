#Menú

def menu ():


    global espacios,l_esoacios, p_h, p_m, re, m_m, m_1, m_2, m_3, b_1, b_2, b_3, b_4, b_5

    espacios = 0}
    l_esoacios = []
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

    
    print ("1. Configuración")
    print ("2. Denero del cajero")
    
    print ("3. Entrada de vahículo")
    print ("4. Cajero del parqueo")
    print ("5. Salida del parqueo")
    print ("6. Ayuda")
    print ("7. Acerca de")
    opcion = int(input("Digite el número da la opción que desea realizar, segun el texto anterior"))

    if opcion == 2 :
        print ("1. Cargar cajero")
        print ("2. Saldo cajero")
        print ("3. Ingreos de dinero")
        opcion_2 = int(input("Digite el número da la opción que desea realizar, segun el texto anterior"))

        
