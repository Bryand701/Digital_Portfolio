[es

def asignar_campo (espacios):
    verificar = str(input("placa "))
    voleano = verificar_placa (verificar)
    c = 0
    v = 0
    for x in espacios:
        if x == [] and v == 0:
            if verificar_placa () == False:
                pass
            else:
                espacios[c] = [str(textBoxPlaca_Entrada.get()),hora_actual(),"",0]
            v = 1
        c += 1

def verificar_placa (placa):
    global espacios

    for x in espacios:

        for y in espacios:
            if y == str(textBoxPlaca_Entrada.get()):
                placa_repe ()
                return False
    return True
