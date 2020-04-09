estatura = float(input('Digite su estatura\n'))
acumuladorestatura = 0
contadorpersonas = 0
promedio = 0

while estatura >= 1.0 and estatura <= 3.0:

	estatura = float(input('Digite su estatura\n'))

	contadorpersonas = contadorpersonas + 1
	acumuladorestatura = acumuladorestatura + estatura
	promedio = acumuladorestatura / contadorpersonas

else:
	print('El promedio de las estaturas es:', promedio)
