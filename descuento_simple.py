


	capital = float()
	interes = float()
	interesganado = float()
	tiempo = int()
	print("Introduce el dinero ganado")
	capital = float(input())
	print("Introduce el porcentaje de interes a ganar")
	interes = float(input())
	print("Introduce los a�os de trabajo")
	tiempo = int(input())
	interes = interes/100
	tiempo = tiempo*12
	interesganado = capital*interes*tiempo
	print("El interes ganado del capital es:",interesganado,", su nuevo capital es:",(interesganado+capital))

