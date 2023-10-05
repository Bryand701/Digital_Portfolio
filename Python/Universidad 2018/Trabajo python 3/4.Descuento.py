def descuento (x):
    import random
    monto = x
    k=random.randint(1, 5)
    if k == 1:
        print ("EL color de la bola que ha sacado es blanca")
        print ("Su descuento es de un 0%, suerte para la proxima :D")
        print ("Su monto a pagar es ", monto)
    elif k == 2:
        print ("EL color de la bola que ha sacado es verde")
        print ("Su descuento es de un 10%")
        descuento = monto*0.1
        print ("Su saldo original es de: ", monto)
        print ("Su monto a pagar es ", monto- descuento)
    elif k ==3:
        print ("EL color de la bola que ha sacado es amarilla")
        print ("Su descuento es de un 25%")
        descuento = monto*0.25
        print ("Su saldo original es de: ", monto)
        print ("Su monto a pagar es ", monto- descuento)
    elif k ==4 : 
        print ("EL color de la bola que ha sacado es azul")
        print ("Su descuento es de un 50%")
        descuento = monto*0.5
        print ("Su saldo original es de: ", monto)
        print ("Su monto a pagar es ", monto- descuento)
    else:
        print ("EL color de la bola que ha sacado es roja")
        print (" Felicidades, su descuento es de un 100%")
        print ("Su saldo original es de: ", monto)
        print ("No tiene que pagar nada :D")
descuento(50000)
