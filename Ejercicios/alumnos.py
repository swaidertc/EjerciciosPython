edadalumnos = 0
cantidadalumnos = 0
contadoredad = 0
prom = 0
continuar = 'si'

while continuar == 'si':

	edadalumnos = int(input('Digite la edad del alumno\n'))

	if edadalumnos < 18:
		contadoredad = contadoredad + edadalumnos
		cantidadalumnos = cantidadalumnos +1
		prom = contadoredad / cantidadalumnos
	elif edadalumnos >= 18:
		contadoredad = contadoredad + edadalumnos
		cantidadalumnos = cantidadalumnos +1
		prom = contadoredad / cantidadalumnos - edadalumnos

	continuar = input('Desea continuar ingre Si o de lo contrario el programa termina\n')
else:		
	print('El numero de alumnos ingresados es:', cantidadalumnos)
	print('El total de las edades es:', contadoredad)
	print('El promedio de edades menor a 18 es:', prom)

	