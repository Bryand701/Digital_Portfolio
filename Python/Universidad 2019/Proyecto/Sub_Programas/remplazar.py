def remplazar (lista):
    c = 0
    v = 0
    for x in lista:
        if x == [] and v == 0:
            lista[c] = ["placa","fecha_hora_entrada","",0]
            v = 1
        c +=1
    return lista
