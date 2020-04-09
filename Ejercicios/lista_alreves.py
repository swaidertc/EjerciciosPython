continuar = 'si'

while continuar == 'si':

	nombre = input('Introduzca una palabra\n')
	palindromo = nombre[::-1]

	if palindromo == nombre:
		print(nombre, 'es palindromo\n')
	else:
		print(nombre, 'no es un palindromo\n')
	continuar = input('si para continuar\n')

	





