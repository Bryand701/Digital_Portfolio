
def ants(amount,mons):
	print("La cantidad de hormigas inicial es:",amount)
	print("La cantidad de meses a calcular:",mons)
	print("")
	cont=0
	porc=1.40
	flag=1
	while cont<mons:
		if amount>28000:
			porc=1.31	
			amount*=porc
			
		else:
			porc=1.40
			amount*=porc
			
		amount-=7000
		cont+=1
		if amount>0:
			
			print ("En el mes ",cont, "la población de hormigas es: ",int(amount))
			
		if amount<0:
			amount=0
			flag=2
			break
                
	if flag==1:
		return print("Al finalizar los meses la cantidad de hormigas es:",int(amount))
	else:
		return print("Las hormigas no sobrevivieron, en el mes",cont,"las hormigas llegaron a 0.")
ants(10000,2)		

