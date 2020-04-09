#Numero 1

calificaciones = {'calculo': 10, 'dibujo': 2.5}
sumcalificaciones = calificaciones.get('calculo') + calificaciones.get('dibujo')
totalnota = sumcalificaciones / 3
print('\n', 'La nota de calculo es:', calificaciones.get('calculo'), '\n', 
	'La nota de dibujo es:', calificaciones.get('dibujo'), '\n',
	'El promedio total es:', totalnota, '\n')

#Numero2
print('El promedio mayor es:', calificaciones.get('calculo'))

#Numero3




"""if calificaciones.get('calculo') > calificaciones.get('dibujo'):
	print('El promedio mayor es', calificaciones.get('calculo'))
else:
	print(print('El promedio mayor es', calificaciones.get('dibujo')))
"""
